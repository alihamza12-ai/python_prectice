a=2
b=3
print(a+b)

a=2
b=3
print(a==b)
print("hillow world")
from typing import Dict
# Dictionary
# first variable is key and second is value
#aading in dict line 16
data : Dict[str,str] ={"Name":"ali hamza",
                      "fname":"zakaullah",
                      "Education":"metric"}
data['class']="first year"
print(data)
# Dict indexing  always write in ""      
print(data["Name"])
# set data type 
abc : set= {4,9,0,5,0,3,4,9,0}
print(abc)#return unique value
#.get function is used to stop error if key is not available

data : Dict[str,str] ={"Name":"ali hamza",
                      "fname":"zakaullah",
                      "Education":"metric"}
print(data.get("pakistan"))
#key function is used to find keys in program and value is used to find values in program
print(data.keys())
#if we write dictionary in for loop then we cannot write data in abc we can write abc in data.value() and data.key()
for abc in data.values():
    print(abc)
#item function
for k,v in data.items():
    print(k,v)
#commprihinsive style
{v:k for k,v in data.items()}
print(data.items())
#fromkeys function
data : list[str] = ["id","name","fname"]
boy : Dict[str,int] = {}
print(data)
print(boy.fromkeys(data))