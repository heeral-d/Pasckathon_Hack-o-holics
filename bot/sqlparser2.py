import nltk
nltk.download('punkt')
from nltk.stem import WordNetLemmatizer
import re

from nltk.tokenize import word_tokenize
class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 

def action_PK(tables_pk,table_name,line):
    y=line.split("(")[1].split(")")[0]
    #print(y+" "+table_name)
    y=y.replace("`","")
    l=y.split(",")
    tables_pk.add(table_name,l)
def action_constraint(tables_relation,table_name,line):
    y=line.split("FOREIGN KEY (")[1].split(")")[0]
    y=y.replace("`","")
    t2=line.split("REFERENCES `")[1].split("`")[0]
    # print(t2)
    # print(y)
    p=[]
    p.append(table_name)
    p.append(t2)
    p.append(y)
    tables_relation.append(p)



file1=open("college_db.sql")
lines=file1.readlines()
s="CREATE TABLE"
a="ALTER TABLE"
pk="ADD PRIMARY KEY"
constraint="ADD CONSTRAINT"
isKey=False
tables=[]
table_attributes={}
tables_pk=my_dictionary()
tables_relation=[]
table_name=""
for i in range(len(lines)):
    #print(line)
    if(isKey):
        if(lines[i].find(pk)!=-1):
            action_PK(tables_pk,table_name,lines[i])
        elif(lines[i].find(constraint)!=-1):
            action_constraint(tables_relation,table_name,lines[i])
        else:
            isKey=False
    else:
        x = re.findall("\A"+s+"",lines[i])
        x1 = re.findall(r'^CREATE TABLE [A-Za-z_`()0-9]*',lines[i])
        # if(x):
        #     #print(x)
        #     y=word_tokenize(str(lines[i]))
        #     tables.append(y[3])
        if(x1):
            size=len(x1[0])-1
            x1=x1[0][14:size]
            tables.append(x1)
            table_attributes[x1]=[]
            for j in range(i+1,len(lines)):
                if(not re.findall(r';$',lines[j])):
                    s=lines[j].split()[0]
                    s=s[1:len(s)-1]
                    table_attributes[x1].append(s)
                else:
                    break
        else:
            y=re.findall("\A"+a+"",lines[i])
            if(y):
                p=word_tokenize(str(lines[i]))
                table_name=p[3]
                isKey=True 
                    

# x1=input("enter your query")
# y1=x1.split(" ")
# for d in y1:
#     if(d in tables):
#         sql="select * from "+str(d)
#         print(sql)
print(tables)
print()
print(tables_pk)
print("\n\n")
print(table_attributes)  
print()
print(tables_relation)
import json
import pickle
with open('table_attributes.json', 'w') as f:
    json.dump(table_attributes, f)
with open('tables_pk.json', 'w') as f:
    json.dump(tables_pk, f)
# elsewhere...
pickle.dump( tables_relation, open( "tables_relation.p", "wb" ))
pickle.dump(tables,open("tables.p","wb"))
# with open('my_dict.json') as f:
#     my_dict = json.load(f)
# print(my_dict)


