import json

obj = {
    "name": "John",
    "age": 30,
    "married": True,
}

print(obj["name"])

x = json.dumps(obj) 
print(x)

y = json.loads(x)
y.update({"city": "Dhaka"})
print(y)

z = json.dumps(y)
print(z)

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

