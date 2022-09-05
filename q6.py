# Q6.Python object key unique key value ko access karne ka program likho?
import json
d='{"a":  1,"a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print("original_object\n",d)
x=json.loads(d)
print("unique_value===\t",x)

