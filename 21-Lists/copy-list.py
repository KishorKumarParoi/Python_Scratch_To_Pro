list1 = [1, 2, 3, 4, 5]
list2 = list1
list1.append(100)
print(list2)
list3 = list2.copy()
list2.pop()
print(list3)
print(list2)
