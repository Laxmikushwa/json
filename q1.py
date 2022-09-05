# Q.1 Json data ko python object main convert karne ka program likho?.
import json
d='{"a":"laxmi","b":"rohini","c":"nishu"}'
d1=json.loads(d)
print(d1)
print(type(d1))