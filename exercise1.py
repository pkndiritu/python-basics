taskList = [23,"Jane",["Lesson 23", 560, {"Currency":"KES"}],987,(76,"John")]

# 1. determine the type of variable in tasklist using an inbuilt syntax
# 2. print KES
# 3. print 560
# 4. use a function to determine the length of tasklist
# 5. Change 987 to 789 using indexing only
# 6. Change the name John to Jane(solution is n/a since variable 5 is a tuple)

a = type(taskList)
print(a)

print(taskList[2][2]["Currency"])
print(taskList[2][1])
print(len(taskList))

z = taskList[3]
z = str(z)
z = z[::-1]
print(z)


