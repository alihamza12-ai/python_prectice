import pandas as pd
from typing import Union, Dict

key = Union[str, int, tuple, set, list]
value = Union[str, int, tuple, set, list]

data: Dict[key, value] = {
    "Name": "Ali Hamza",
    "fname": "zakaullah",
    "Education": "metric",
    "list": {"a": 2, "b": 4},
    (1, 2, 3): "Pakistan"
}

data["Name"] = "Ali Hamza"  # Updating the value for the key "Name"
print(data)
# Output: {'Name': 'Ali Hamza', 'fname': 'zakaullah', 'Education': 'metric', 'list': {'a': 2, 'b': 4}, (1, 2, 3): 'Pakistan'}

print(data["list"])
# Output: {'a': 2, 'b': 4}

print(data["list"]["a"])
# Output: 2

print(data.get("pakistan", "NA"))
# Output: NA (since 'pakistan' key is not present in data)

print(data.pop("fname"))
# Output: zakaullah (removes and returns the value associated with 'fname' key)

print(data.popitem())
# Output: ((1, 2, 3), 'Pakistan') (removes and returns the last key-value pair from data)

print(data.setdefault("pakistan", "zinndabad"))
# Output: zinndabad (sets the value 'zinndabad' for the key 'pakistan' since key 'pakistan' was not found)

# DataFrame creation
# collection: Dict[key, value] = {
#     "Name": "ali hamza",
#     "fname": "zakaullah",
#     "Education": "metric",
#     "Roll num": "csb19"
# }
# df: pd.DataFrame = pd.DataFrame(collection)
# print(df)
collection = {
    "Name": ["ali hamza"],
    "fname": ["zakaullah"],
    "Education": ["metric"],
    "Roll num": ["csb19"]
}
df = pd.DataFrame(collection)
print(df)