# Q.2 Python object ko json data main convert karne ka program likho?
import json
d={
    "name": "David", 
    "class": "I", 
    "age": 6
}
d1=json.dumps(d)
print(d1)
print(type(d1))