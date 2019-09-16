# if else statements
# balance = 100
# withdraw = 20
# name = "Said"
# if withdraw <= balance and name == "Said":
#     print("withdraw success")
# else:
#     print("insufficient funds or not Said")

# if - elif -else statements
# score = "Good"
# if score == "Excellent":
#     print("Green label")
# elif score == "Good":
#     print("Blue label")
# elif score == "Poor":
#     print("Red label")
# else:
#     print("unrecognised")

# task
# # ask a user to enter the following marks
# # math hint (use input function)
# # eng
# # kisw
# # ssr
# # sci
# calculate the total of the marks
# # # calculate the average
# # # using the average, give grade to the student
# 80 - 100 = "A"
# 70 - <80 = "B"
# 60 - <70 = "C"
# 50 - <60 = "D"
# <50 = "E"

math = input("enter the marks for math")
eng = input("enter the marks for eng")
kisw = input("enter the marks for kisw")
ssr = input("enter the marks for ssr")
sci = input("enter the marks for sci")

total_marks = int(math) + int(eng) + int(kisw) + int(ssr) + int(sci)
print(total_marks)
average = total_marks/5
print(average)

if average >=80 and average ==100:
    print("A")
elif average <80 and average >=70:
    print("B")
elif average <70 and average >=60:
    print("C")
elif average <60 and average >=50:
    print("D")
elif average>=0 and average<50:
    print("E")
else:
    print("unrecognised")