# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user

number = int(input("Value number"))
if number % 2 == 0 and number !=0:
    print("Even number")
elif number == 0:
    print("Zero is neither even, nor odd")
else:
    print("Odd number")
