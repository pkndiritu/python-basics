# from functions import add_two_numbers
# We use while when we don't have a defined end for a loop
# A for loop is a kind of loop that repeats unitil maximum number of times

# for a in range(10,100):
#     print(a)

# fruits = ["Mango","Apple","Bananas","Pineapple","Avocado","Strawberry"]
#
# for each in fruits:
#     each = each + "a"
#     print(each)

# adding numbers in a range (list)
# sum = 0
# for each in range(10):
#     sum = each + sum
#
# print(sum)

# name = "PAUL"
# # for each in range(101):
# #     print(name)

# name = "Paul Kirira"
# count = 0
# for each in range(101):
#
#     print(str(count),name)
#     count = count + 1

# the first number is the lower limit and the second number is the upper limit and 3 is the distance
# for each in range(8,89,3):
#
#     print(each)
#
# for each in range (1,21):
#     eachbyeach = each**2
#     print(each,"---", eachbyeach)

# first_number = eval(input("Enter first number"))
# second_number = eval(input("Enter second number"))
#
# result = add_two_numbers(first_number,second_number)
# print(result)

from functions import add_three_names

First = "Paul"
Second = "Kirira"
Third = "Ndiritu"

result = add_three_names("Paul","Kirira","Ndiritu")
print(result)