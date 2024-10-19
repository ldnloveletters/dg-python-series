person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coin left.")

message = "\n%s has %s coins left." %(person, coins) # %s is a placeholder for the variable person and coins
print(message)

message = "\n{} has {} coins left.".format(person, coins) # another way to format the string
print(message)

message = "\n{1} has {0} coins left.".format(coins, person) # using indexing instead
print(message)

message = "\n{person} has {coins} coins left.".format(coins=coins, person=person) # another way to pass variables
print(message)

player = {'person': 'Dave', 'coins': 3}
message = "\n{person} has {coins} coins left.".format(**player) # using dictionary unpacking
print(message)

###########
# f-strings! This is the way.

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2*5} coins left."
print(message)

message = f"\n{person.lower()} has {2*5} coins left."
print(message)

message = f"\n{player['person']} has {2*5} coins left."
print(message)

######
# You can pass formatting options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1,11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1,11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")