fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
for x in fruits:
    if 'a' in x:
        print(x)    
    
newlist = [x for x in fruits if 'ap' not in x]
print(newlist)

newlist = [x if x!= 'banana' else 'orange' for x in fruits]
print(newlist)