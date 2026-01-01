# Day 1 - Check whether a number is Positive, Negative or Zero

# Method 1: Using if-elif-else
num = 15

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Method 2: Using nested if-else
num = -15

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")


# Method 3: Using ternary operator
num = 15
print("Positive" if num > 0 else "Negative")
