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