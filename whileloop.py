# a while loop runs until a certain condition is false

# a = 1
# if a< 11:
#     print("Paul "*a)
#     a = a+1

# Atm authentication program

savedpin = "0000"
trials = 3
enteredpin = input("Enter your pin")
trials = trials - 1
while savedpin != enteredpin and trials>0:
    enteredpin = input("Enter your pin")
    trials = trials - 1
else:
    if trials<1 and enteredpin != savedpin:
        print("Card swallowed")
    else:
        print("Successful login")