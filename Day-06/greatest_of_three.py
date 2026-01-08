# Day 06 - Greatest of Three Numbers

# Method 1: Using if-elif-else
num1, num2, num3 = 10, 20, 30

if num1 >= num2 and num1 >= num3:
    print("Greatest number:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Greatest number:", num2)
else:
    print("Greatest number:", num3)


# Method 2: Using nested if-else
num1, num2, num3 = 10, 350, 50

if num1 >= num2:
    if num1 >= num3:
        print("Greatest number:", num1)
    else:
        print("Greatest number:", num3)
else:
    if num2 >= num3:
        print("Greatest number:", num2)
    else:
        print("Greatest number:", num3)


# Method 3: Using ternary operator
num1, num2, num3 = 10, 30, 20

maximum = num1 if num1 > num2 else num2
maximum = num3 if num3 > maximum else maximum

print("Greatest number:", maximum)
