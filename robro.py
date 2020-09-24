from flask import Flask,render_template,request,url_for,redirect
import speech_recognition as sr
import sqlparser2
import nltk
import os
import pickle
import json
import MySQLdb
from nltk.stem import WordNetLemmatizer 
app = Flask(__name__)

app.config['File_uploads']="C:\\Users\\Admin\\Desktop\\paskathon\\static"
database = ''
dic1 = {}

@app.route('/home')
def home():
    return render_template("start.html")

@app.route('/bot',methods=["POST"])
def hello():
    global dic1
    l=[]
    i = 1
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
    return redirect(url_for('home'))	

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

@app.route("/getsql",methods=["POST"])
def getsql():
    global database
    sample_text = request.form['post_id']
    print(sample_text)
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
    
    result=""
    # def mysqlconnect(sql): 
    #     try: 
    #         db_connection= MySQLdb.connect("localhost","root","","smart_bot") 
    #     except: 
    #         print("Can't connect to database") 
    #         return 0
    #     print("Connected")  
    #     cursor=db_connection.cursor() 
    #     cursor.execute(sql) 
    #     m = cursor.fetchall() 
    #     print('---------------------')
    #     for row in m:
    #         result+=row+"<br>" 
    #     db_connection.close() 



    def isWhere(pos):
        for i in range(len(pos)):
            if(pos[i][1]=='WP$' or pos[i][1]=='WRB'):
                return i
        return -1

    def getAttributes(second_part):
        gr=r"Chunk1: {<CC>?(<NN.?><VB.?>(<JJ.?>*|<IN>)*(<NN.?>|<CD>))*}"

        chunkParser=nltk.RegexpParser(gr)
        chunked=chunkParser.parse(second_part)
        chunked=str(chunked)

        chunked=chunked[3:len(chunked)-1]
        chunked=chunked.split("\n")
        l=[]
        ll=[]
        dic={}

        for line in chunked:
            temp=line[3:len(line)-1].split(" ")
            for j in range(len(temp)):
                l.append(temp[j].split(",")[0])

            ll.append(l[1:])
            l=[]

        #print(chunked)
        #print(ll)
        return ll
        
    def findTable(match,attr_list):
        best_match_list=[]
        for i in tables:
            if i.find(match)!=-1:
                q=[]
                diff=len(i)-len(match)   
                q.append(i)
                q.append(diff)
                best_match_list.append(q)
        best_match_list.sort(key = lambda x: x[1])
        # print(best_match_list)
        p=""
        map_schema={}
        # print(attr_list)
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
                    print("verb",verb)
                    for k in mapping.keys():
                        if p.lower() in mapping[k]:
                            print("k",k)
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

    lemmatizer = WordNetLemmatizer()
    #sample_text=input("Enter your question: ")
    tokenized=nltk.word_tokenize(sample_text)
    l=[]
    for i in tokenized:
        l.append(lemmatizer.lemmatize(i))
    pos=nltk.pos_tag(l)
    print(pos)
    tname=""
    p=isWhere(pos)
    sql = ''
    if(p!=-1):
        first_part=pos[0:p]
        second_part=pos[p+1:]
        attr_list=getAttributes(second_part)
        print(attr_list)
        tname,map_schema=findTable(first_part[-1][0],attr_list)
        #print(first_part)
        # print("ahdkjd")
        #print(second_part)
        # print(attr_list)
        # print(tname)
        # print(map_schema)
        
    if sample_text.find("What is")!=-1 or sample_text.find("What are")!=-1 or sample_text.find("How many")!=-1:
        for i in range(len(pos)):
            if pos[i][0] == 'of':
                attr=pos[i-1][0]
                tname=pos[i+1][0]
                for j in range(0,i):
                    for k in mapping.keys():
                        if pos[j][0].lower() in mapping[k]:
                            agg=k
                            if agg=="count":
                                attr='*'
    if agg=="":
        sql="SELECT * FROM "+tname+" WHERE"
    else:
        sql="SELECT "+agg+"("+attr+") FROM "+tname+" WHERE";
    sql += condition_args(attr_list,map_schema)+" ;"
    print(sql)
        # mysqlconnect(sql)
         
    try: 
        db_connection= MySQLdb.connect("localhost","root","",database) 
    except: 
        print("Can't connect to database") 
        return 0
    print("Connected")  
    cursor=db_connection.cursor() 
    try:
        cursor.execute(sql) 
        m = cursor.fetchall() 
        print('---------------------')
        for row in m:
            result+=str(row)+"<br>" 
    except:
        result = 'Try Again'

        db_connection.close()

    return ('<span> ' + sql +'<br>'+result+ ' </span>')

if __name__ == '__main__':
    app.run(debug=True)