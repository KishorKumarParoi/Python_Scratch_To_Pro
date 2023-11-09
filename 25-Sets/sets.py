# Set is unordered, unchangeable (add, remove), unindexed, and do not allow duplicates

# Create a set
my_set = {"apple", "banana", "cherry" , False, 0, 0.0, None, "apple"}
print(my_set)
print(len(my_set ))

my_set.add("orange")
print(my_set)

my_set.update(["orange", "mango", "grapes"])
print(my_set)

my_set.remove("banana")
print(my_set)

my_set.discard("banana")
print(my_set)

my_set.pop()
print(my_set)

# remove raise error if not found but discard doesn't
# pop() return deleted item and delete random number

