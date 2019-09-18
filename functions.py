# a function is a named, reusable block of code used to perform an operation
# add_two_numbers is the name of our function
# def is the keyword for creating a new function in python
# a and b are the parameters of the function
# c is the return value

# def add_two_numbers(a,b):
#     c = a+b
#     return c

# def add_three_names(First,Second,Third):
#     full_name = First+Second+Third
#     return full_name





# student1 = [12,23,34,45,65]
# student2 = [22,23,34,45,65]
# student3 = [32,23,34,45,65]
# student4 = [42,23,34,45,65]
# def find_total(math,eng,kis,ssr,sci):
#     alama = math+eng+kis+ssr+sci
#     return alama
#
# def find_average(tot):
#     return tot/5
#
# marks = find_total(12,23,34,45,65)
# mean_score = find_average(marks)
#
# print(marks,mean_score)
# total1= student1[0]+student1[1]+student1[2]+student1[3]+student1[4]
# total2= student2[0]+student2[1]+student2[2]+student2[3]+student2[4]
# total3= student3[0]+student3[1]+student3[2]+student3[3]+student3[4]
# total4= student4[0]+student4[1]+student4[2]+student4[3]+student4[4]
#
# average1 = total1/5
# average2 = total2/5
# average3 = total4/5
# average4 = total4/5


def sum_digits(num):
    sum_of_digits = 0
    num = str(num)
    for each in num:
        sum_of_digits = sum_of_digits + int(each)
    return sum_of_digits

res = sum_digits(12345)
print(res)



