value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1
    

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))
    

# for x in names:
#     print(x)
    
# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Sarah":
#         break
#     print(x)

# for x in names:
#     if x == "Sarah":
#         continue
#     print(x)
    
# for x in range(4):
#     print(x)

# for x in range(2, 4): # includes the number you start on but not the number you end on
#     print(x)
    
for x in range(5,101,5):
    print(x)
else:
    print("Glad that\'s over!")

names = ["Dave", "Sarah", "John"]
actions = ["codes", "eats", "sleeps"]

# for name in names:        
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:        
    for name in names:
        print(name + " " + action + ".")