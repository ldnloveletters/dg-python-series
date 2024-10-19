# creating lists

users = ['Dave', 'John', 'Sarah']

data = ['Dave', 42, True]

emptylist = []

print("Dave" in data)

# finding an item in the list
print(users[0])
print(users[-2])

print(users.index('Sarah'))

print(users[0:2])
print(users[-3:-1])

# printng the length of the list
print(len(data))

# add news items to a list, various methods
users.append('Elsa')
print(users)

users += ['Jason'] #needs brackets, otherwise will include every letter
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

# add lists together
# users.extend(data)
# print(users)

# inserting an item to a specific position
users.insert(0, "Bob")
print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)

# replace values using a slice
users[1:3] = ['Robert', 'JPJ']
print(users)

# remove values
users.remove('Bob')
print(users)

print(users.pop()) # removes and returns the last item
print(users)

del users[0] # removes the item at the specified index
print(users)

# del data #removes the entire list
data.clear()
print(data)

users[1:2] = ['dave']
# sorting a list
users.sort()
print(users)
users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5] #new list
nums.reverse() #flips the list
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True)) # does not modify - will sort the list in the print function
print(nums)

# make a copy of the list - 3 methods
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

# check types of lists
print(type(nums))

# using list constructor for new list
mylist = list([1, 'Neil', True])
print(mylist)

#  tuples

mytuple = tuple(['Dave', 42, True])
anothertuple = (1,4,2,8,2,2) # packing the tuple

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# appending a value to a tuple to create a new tuple
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

#  tuple unpacking
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2)) # count the number of occurrences of an item