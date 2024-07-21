#Dictionary

import pandas as pd
from typing import Union
from typing import Dict

key=Union[str,int,tuple,set,list]
value=Union[str,int,tuple,set,list]

data : Dict[key,value] = {"Name":"ali hamza",
                      "fname":"zakaullah",
                      "Education":"metric",
                      "list":{"a":2,"b":4},
                      (1,2,3):"Pakistan"}#tuple data type is used to key
                    #   [1,1,1]:"zindabad",#list data type is not used to key
                    #   {2,2,2}:"paindabad"}#set data type is used to key
data["Name"] = "Ali Hamza"
print(data) 
print(data["list"])
print(data["list"]["a"])
print(data.get("pakistan","NA"))#get function is used to run time error not show if we write pakistan if it was not then
                              #error is not showed NA is write because if pakistan is not found then write NA anything
print(data.pop("fname"))
print(data.popitem())#popitem function is used to remove last value
print(data.setdefault("pakistan","zinndabad"))#this function is used to adding key and value
#DataFrame functiion

collection : Dict[key,value] = {"Name":"ali hamza",
                               "fname":"zakaullah",
                               "Education":"metric",
                               "Roll num":"csb19"}
df : pd.DataFrame=pd.DataFrame(collection)
print(df)