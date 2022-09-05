# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?
import json
d={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
# d1=json.dumps(d,indent=2,sort_keys=True)
d1=json.dumps(d,indent=4,separators=("."," = "))
print(d1)
print(type(d1))