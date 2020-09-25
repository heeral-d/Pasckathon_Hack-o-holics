import nltk
from nltk.stem import WordNetLemmatizer 
sample_text=input("Question: ")
def isWhere(pos):
        for i in range(len(pos)):
            if(pos[i][1]=='WP$' or pos[i][1]=='WRB'):
                return i
        return -1
def checkPrep(pos):
    for i in range(len(pos)):
        if(pos[i][1]=='IN' and (pos[i][0]=='with' or pos[i][0]=='in')):
            return i
    return -1

def getAttributes(second_part,Where=True):
    if Where:
        gr=r"Chunk1: {<CC>?(<NN.?><VB.?>(<JJ.?>*|<IN>)*(<NN.?>|<CD>))*}"
    else:
        gr=r"Chunk1: {<CC>?(<NN.?><NN.?>|<CD>)*}"
    chunkParser=nltk.RegexpParser(gr)
    chunked=chunkParser.parse(second_part)
    chunked=str(chunked)
    print(chunked)
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
    print("First_part: ",first_part)
    print("second_part: ",second_part)
    attr_list=getAttributes(second_part)
    # print(attr_list)
    # tname,map_schema=findTable(first_part[-1][0],attr_list)
    # #print(first_part)
    # print("ahdkjd")
    #print(second_part)
    # print(attr_list)
    # print(tname)
    # print(map_schema)
else:
    p=checkPrep(pos)
    if p!=-1:
        first_part=pos[0:p]
        second_part=pos[p+1:]
        print("First_part: ",first_part)
        print("second_part: ",second_part)
        attr_list=getAttributes(second_part,False)