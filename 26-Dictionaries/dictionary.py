dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(dict)

# Accessing Items
print(dict["name"])
print(dict.get("age"))

x = dict.keys()
print(x)

y = dict.values()
print(y)

dict["name"] = "Kishor"
dict.update({"age" : "24"})
print(dict)

dict["address"] = "Dhaka"
print(dict)

dict.pop("city")
print(dict)

print(len(dict))
print(dict.items())

for x,y in dict.items():
    print(x + " : " + y)