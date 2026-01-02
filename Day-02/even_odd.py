# Day 02 - Check Even or Odd Number

# Method 1: Using Modulus Operator
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Given number is Even")
else:
    print("Given number is Odd")


# Method 2: Using Ternary Operator
num = 17
print("Even" if num % 2 == 0 else "Odd")


# Method 3: Using Bitwise Operator
def is_even(num):
    return not num & 1

num = 13
if is_even(num):
    print("Even")
else:
    print("Odd")