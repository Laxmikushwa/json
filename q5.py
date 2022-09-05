# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?
import json 
def lx(object):
    if '_complex_'in object:
        print(complex(object["real"],object["img"]))
    else:
        print(object)
a='{"_complex_":true,"real":3,"img":13}'
b='{"real":3,"img":13}'
x=json.loads(a)
lx(x)
x=json.loads(b)
lx(x)