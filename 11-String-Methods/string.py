apple = 20
orange = 30
berry = 10
cost = 60

message = 'The cost of {2}, {3} and {1} is {0}'

print('\n' + message.format(cost, apple, orange, berry))

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apepl")

print(x)

txt = "I could eat bananas all day bananas and Kolas"

x = txt.partition("bananas")

print(x)

x = txt.rpartition("bananas")
print(x)

print('\n')
