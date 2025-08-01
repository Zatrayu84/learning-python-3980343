# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop
# while x < 5:
#   print(x)
#   x = x+1

# answer = input("Should I stop?")
# while answer != "yes":
#   print(answer)
#   answer = input("Should I stop?")

# define a for loop
days = ["Mon", "Tue", "Wed", "Thurs", "Friday", "Sat", "Sun"]
# for d in days:
#   print(d)

# use a for loop over a collection


# use the break and continue statements
# for d in days:
#   if(d == "Thurs"):
#     continue
#   print(d)

# using the enumerate() function to get an index and an item
for i, d in enumerate(days):
  print(i, d)