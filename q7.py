# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
import json
lx="f1.txt"
file1=open(lx,"r")
d={}
for i in file1:
    key1,value1=i.strip().split(None,1)
    d[key1]=value1
# print(d)

with open("ck.json","w") as laxmi:
    json.dump(d,laxmi,indent=4)



