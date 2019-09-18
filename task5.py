# With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), write a program to print the first half values in one line and the last half values in one line

height = (4,6,8,5,9,8,7,6,5,9,4)
lst = []
for each in range (0,10,5):
    lst.append(height[each:each+5])
print(lst)

