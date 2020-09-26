from flask import Flask,render_template,request,url_for,redirect
import speech_recognition as sr
import sqlparser2
import nltk
import os
import pickle
import json
import pymysql
import database_config
from nltk.stem import WordNetLemmatizer 
import csv
import time
import threading
import sweet
import queries
from queries import query
app = Flask(__name__)

app.config['File_uploads']=database_config.file_path+"static"
database = ''
dic1 = {}
csv_list = []
@app.route('/home')
def home():
    return render_template("start.html")

@app.route('/bot')
@app.route('/bot', methods=['POST']) 
def hello():
    global dic1
    l=[]
    i = 1
    if request.method == "POST":
        uploaded_file = request.files['userfile']
        if uploaded_file.filename.split(".")[1]=="sql":
            uploaded_file.save(os.path.join(app.config['File_uploads'],uploaded_file.filename))
            print(uploaded_file.filename)
    
    for file in os.listdir(app.config['File_uploads']):
        if file.split(".")[1]=="sql":
            l.append(str(file.split(".")[0]))
            dic1[str(i)] = str(file.split(".")[0])
            i += 1
    return render_template("home.html",file_list=l)
    # return redirect(url_for('home'))	

@app.route("/get_database",methods=['POST'])
def set_database():
    global database
    global dic1
    print(dic1)
    sample_text = request.form['post_id']
    database = dic1[sample_text]
    print(sample_text)
    # if sample_text=='1':
    #     database="university"
    # elif sample_text=='2':
    #     database='smart_bot'
    sqlparser2.parser(database+'.sql')
    #os.system('python sqlparser2.py '+database+'.sql')
    sql="Database loaded"
    return '<span> ' + sql +'<br>'+database+ ' </span>'    

@app.route("/record",methods=['POST'])
def record():
    re = request.form['rec']
    if re == 'Start Recording: ':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Speak anything: ')
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print('\nYou said: {}\n'.format(text))
            except:
                text = 'Sorry could not recognize your file'
    return text 

@app.route("/download",methods=['POST'])
def download():
    global csv_list
    re = request.form['download']
    if re == 'CSV downloading: ':
        with open(database_config.file_path+'static\\output.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in csv_list[-1].get():
                csvwriter.writerow(row)
    #csv_list = []
    sweet.analysis()
    

@app.route("/getsql",methods=["POST"])
def getsql():
    global database
    sample_text = request.form['post_id']
    sample_text=sample_text.replace(',',' ')
    # print('sample',sample_text)

    with open('static/table_attributes.json') as f:
        table_attributes = json.load(f)
    with open('static/mapping.json') as f:
        mapping = json.load(f)
    # print(table_attributes) 
    with open('static/tables_pk.json') as f:
        tables_pk = json.load(f)
    # print(tables_pk)
    tables= pickle.load( open( "static/tables.p", "rb" ) )
    # print(tables)
    tables_relation= pickle.load( open( "static/tables_relation.p", "rb" ) )
    # print(tables_relation)
    map_schema={}
    agg=''
    #

    def isWhere(pos):
            for i in range(len(pos)):
                if(pos[i][1]=='WP$' ):#or pos[i][1]=='WRB'):
                    return i
            return -1
    def checkPrep(pos):
        for i in range(len(pos)):
            if(pos[i][1]=='IN' and (pos[i][0]=='with' or pos[i][0]=='in')):
                return i
        return -1

    def getAttributes(second_part,Where=True):
        if Where:
            gr=r"Chunk1: {<CC>?(<NN.?><VB.?>?(<JJ.?>*|<IN>)*(<NN.?>|<CD>))*}"
        else:
            gr=r"Chunk1: {<CC>?(<NN.?>(<JJ.?>*|<IN>)*(<NN.?>|<CD>))*}"
            print('with *'+gr+'*')
            # gr=r"Chunk1: {<CC>?(<NN.?>(<NN.?>|<CD>))*}"
        chunkParser=nltk.RegexpParser(gr)
        chunked=chunkParser.parse(second_part)
        # chunked=str(chunked)
        print('chunked',chunked,len(chunked))
        # chunked=chunked[3:len(chunked)-1]
        # print('chunked',chunked,len(chunked))
        # chunked=chunked.split("\n")
        # print('chunked',chunked,len(chunked))
        l=[]
        ll=[]
        dic={}

        for line in chunked:
            line=str(line)
            temp=line[8:len(line)-1].split(" ")
            # for j in range(len(temp)):
            #     l.append(temp[j].split(",")[0])
            ll.append(temp)
        # print("l",ll)
            # ll.append(l[1:])
            # l=[]

        #print(chunked)
        #print(ll)
        return ll
        
    def findTable(first_part,attr_list):
        best_match_list=[]
        for match in first_part:
            for i in tables:
                if i.find(match[0])!=-1:
                    q=[]
                    diff=len(i)-len(match[0])   
                    q.append(i)
                    q.append(diff)
                    best_match_list.append(q)
        best_match_list.sort(key = lambda x: x[1])
        # print("best",best_match_list)
        p=""
        map_schema={}
        # print("attr",attr_list)
        for i in best_match_list:
            count=0
            for j in attr_list:
                for k in j:
                    if(k.find("/N")!=-1):
                        p=k.split("/")[0]
                        break
                    
                for q in table_attributes[i[0]]:
                    if(q.find(p)!=-1):
                        map_schema[p]=q
                        count+=1
                        # print(q+" "+str(count)+" "+str(j)+" "+str(i))
                if(count==len(attr_list)):
                    return i[0],map_schema
        return '',{}
                
    def condition_args(attr_list,map_schema):
        s1=''
        for i in attr_list:
            flag=False
            vflag=False
            for k in i:
                if(k.find("/N")!=-1 and flag==False):
                    flag=True
                    p=k.split("/")[0]
                    s1+=" "+map_schema[p]
                elif k.find("/CC")!=-1:
                    p=k.split("/")[0]
                    s1+=" "+p.upper()
                elif(k.find("/V")!=-1):
                    vflag=True
                    p=k.split("/")[0]
                    for k in mapping.keys():
                        if p.lower() in mapping[k]:
                            # s1+=" "+k
                            verb=k
                            break
                elif(k.find("/J")!=-1 or k.find("/IN")!=-1):
                    p=k.split("/")[0]
                    # print("p",p)
                    for k in mapping.keys():
                        if p.lower() in mapping[k]:
                            # print("k",k)
                            if vflag==True:
                                # s1=s1.replace(verb,k)
                                s1+=" "+k
                                print("s1",s1)
                                vflag=False
                            else:
                                s1+=" "+k
                            break
                    # if vflag==True:
                    #     s1.replace(verb,p.lower())
                    # else:
                    #     s1+=" "+p.lower()
                elif(k.find("/N")!=-1 and flag==True):
                    p=k.split("/")[0]
                    if vflag==True:
                        s1+=" "+verb
                    s1+=" '"+p+"'"
                elif(k.find("/CD")!=-1):
                    p=k.split("/")[0]
                    if vflag==True:
                        s1+=" "+verb
                    s1+=" "+p
        return s1


    def condition_args_for(attr_list,map_schema):
        s1=''
        count=0
        for i in attr_list:
            flag=False
            vflag=False
            prev=0
            for k in i:
                # print('Noun flag',flag)
                if(k.find("/N")!=-1 and flag==False):
                    flag=True
                    p=k.split("/")[0]
                    s1+=" "+map_schema[p]
                elif k.find("/CC")!=-1:
                    p=k.split("/")[0]
                    s1+=" "+p.upper()
                elif(k.find("/V")!=-1):
                    vflag=True
                    p=k.split("/")[0]
                    for k in mapping.keys():
                        if p.lower() in mapping[k]:
                            # s1+=" "+k
                            verb=k
                            break
                elif(k.find("/J")!=-1 or k.find("/IN")!=-1):
                    p=k.split("/")[0]
                    for k in mapping.keys():
                        if p.lower() in mapping[k]:
                            if vflag==True:
                                # s1=s1.replace(verb,k)
                                s1+=" "+k
                                print("s1",s1)
                                vflag=False
                            else:
                                s1+=" "+k
                            break
                    # if vflag==True:
                    #     s1.replace(verb,p.lower())
                    # else:
                    #     s1+=" "+p.lower()
                elif(k.find("/N")!=-1 and flag==True):
                    # print('dama pro')
                    p=k.split("/")[0]
                    if vflag==True:
                        s1+=" "+verb
                    else:
                        # print('in else')
                        s1+=" ="
                    s1+=" '"+p+"'"
                elif(k.find("/CD")!=-1):
                    p=k.split("/")[0]
                    if vflag==True:
                        s1+=" "+verb
                    elif prev==1:
                        s1+=" ="
                    s1+=" "+p
                if (k.find("/N")!=-1):
                    prev=1
                else:
                    prev=0
        return s1

    def selected_attr(table,first_part):
        possible_candidate=[]
        aggr=''
        for data in first_part:
            if data[1].find('NN')!=-1 and data[0]!=tname and data[0] in table_attributes[table]:
                possible_candidate.append(data[0])
            if (data[1].find('NN')!=-1 and data[0] in mapping['COUNT']):
                aggr='COUNT'
            elif data[1].find('JJ')!=-1:
                for k,v in mapping.items():
                    if data[0] in v:
                        aggr=k
                        break 

        return possible_candidate,aggr



    lemmatizer = WordNetLemmatizer()
    #sample_text=input("Enter your question: ")
    tokenized=nltk.word_tokenize(sample_text)
    temp_pos=nltk.pos_tag(tokenized)
    pos=[]
    for i in range(len(temp_pos)):
        if temp_pos[i][1].find('NN')!=-1:
            pos.append((lemmatizer.lemmatize(temp_pos[i][0]),temp_pos[i][1]))
        else:
            pos.append((temp_pos[i][0],temp_pos[i][1]))
    # for i in tokenized:
    #     l.append(lemmatizer.lemmatize(i))

    print(pos)
    tname=""
    where_condition_string=''
    aggr=''
    p=isWhere(pos)
    sql = ''
    if(p!=-1):
        first_part=pos[0:p]
        second_part=pos[p+1:]
        print("First_part: ",first_part)
        print("second_part: ",second_part)
        attr_list=getAttributes(second_part)
        print(attr_list)
        tname,map_schema=findTable(first_part,attr_list)
        #print(first_part)
        print("ahdkjd")
        print(second_part)
        print(attr_list)
        print(tname)
        print(map_schema)
        where_condition_string=condition_args(attr_list,map_schema)

    else:
        p=checkPrep(pos)
        if p!=-1:
            first_part=pos[0:p]
            second_part=pos[p+1:]
            print("First_part: ",first_part)
            print("second_part: ",second_part)
            attr_list=getAttributes(second_part)
            print(attr_list)
            tname,map_schema=findTable(first_part,attr_list)
            #print(first_part)
            print("ahdkjd")
            print(second_part)
            print(attr_list)
            print(tname)
            print(map_schema)
            where_condition_string=condition_args(attr_list,map_schema)
        else:
            first_part=pos
            for data in first_part:
                if data[1].find('NN')!=-1 and data[0] in tables:
                    tname=data[0]

    if where_condition_string!='':
        where_condition_string=" WHERE"+condition_args(attr_list,map_schema)

    possible_candidate,aggr=selected_attr(tname,first_part)

    # print('AGGR',aggr)

    if len(possible_candidate)==0:
        if aggr=='':
            possible_candidate='*'
        else:
            possible_candidate=aggr+'(*)'
    else:
        if aggr=='':
            possible_candidate=','.join(possible_candidate)
        else:
            possible_candidate=aggr+'('+','.join(possible_candidate)+')'

    sql='SELECT '+possible_candidate+' FROM '+tname+where_condition_string+';' 
    print('SQL query:',sql)

        # mysqlconnect(sql)
         
    # try: 
    #     db_connection= MySQLdb.connect("localhost","root","",database) 
    # except: 
    #     print("Can't connect to database") 
    #     return 0
    # print("Connected")  
    # cursor=db_connection.cursor() 
    # try:
    #     cursor.execute(sql) 
    #     m = cursor.fetchall() 
    #     print('---------------------')
    #     for row in m:
    #         result+=str(row)+"<br>" 
    # except:
    #     result = 'Try Again'

    #     db_connection.close()
    try:
        print(database)
        connection = pymysql.connect(host=database_config.hostname, user=database_config.user, passwd=database_config.passwd, database=database)
        cursor = connection.cursor()
        cursor.execute(sql)
        rows=cursor.fetchall()
        global csv_list
        col_name = []
        csv_list2 = []
        for c1 in cursor.description:
            col_name.append(c1[0])
        csv_list2.append(col_name)
        result="<br><table style='border: 1px black; background-color: white; opacity:0.8;'>"
        for l in col_name:
            result+="<th style='border: 1px black; color: black;'>"+l+"</th>"

        for row in rows:
            csv_list2.append(row)

        count = 0
        for row in rows:
            if count <= 3:
                result+="<tr style='border: 1px black;'>"    
                for col in row:
                    result+="<td style='border: 1px black; color: black;'>"+str(col)+"</td>"
                result+="</tr>"
            count += 1 
        result+="</table><br>"
        csv_list.append(query(csv_list2))
        # print(result)
        
        print(csv_list)

    except:
        result="Try Again"
    finally:
        connection.close()
    return ('<span> ' + sql +'<br>'+result+ ' </span>')

if __name__ == '__main__':
    app.run(debug=True)