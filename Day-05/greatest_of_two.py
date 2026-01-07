# Day 05 - Greatest of Two Numbers

# Method 1: Using if-else
num1, num2 = 20, 30

if num1 > num2:
    print("Greatest number:", num1)
else:
    print("Greatest number:", num2)


# Method 2: Using ternary operator
num1, num2 = 20, 30
print("Greatest number:", num1 if num1 > num2 else num2)


# Method 3: Using inbuilt max() function
num1, num2 = 20, 30
print("Greatest number:", max(num1, num2))
