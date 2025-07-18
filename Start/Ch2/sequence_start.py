# LinkedIn Learning Python course by Joe Marini

# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
myList = [0,1,"two",3.2,False]
# print(len(myList))

# to access a member of a sequence type, use []
# print(myList[2])
# print(myList[-1])
# myList[0] = 10
# print(myList[0])

# add a list to another list
# anotherList = [6,7,8]
# myList = myList + anotherList
# print(myList)

# use slices to get parts of a sequence
#print(myList[::2])

# you can use slices to reverse a sequence - this allows you to reverse the list or string.
# print(myList[::-1])

# test_str = "Monkey"
# print(test_str[::-1])

# Tuples are like lists, but they are immutable
myTuple = (0,1,2,"three")
# print(myTuple[1])

# Sets are also sequences, but they contain unique values
myset = {1,2,3,2,4, "hey"}   #this will remove the 2nd 2 to keep each item in list is unique
#print(myset)

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
# to test for membership, or the existence of items in a list set or tuple, just ask
print(1 in myList)
print(3 in myTuple)
print(5 in myset)