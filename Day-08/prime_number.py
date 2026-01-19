# Day 08 - Check Prime Number

# Method 1: Simple iterative approach
num = 15
flag = 0

if num < 2:
    flag = 1
else:
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break

if flag == 1:
    print("Not Prime")
else:
    print("Prime")


# Method 2: Optimized check (up to n/2)
num = 15
flag = 0

for i in range(2, (num // 2) + 1):
    if num % i == 0:
        flag = 1
        break

print("Prime" if flag == 0 and num > 1 else "Not Prime")


# Method 3: Optimized using square root
import math

num = 15
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

print("Prime" if is_prime else "Not Prime")


# Method 4: Using recursion
def check_prime(num, i=2):
    if num < 2:
        return False
    if i > num // 2:
        return True
    if num % i == 0:
        return False
    return check_prime(num, i + 1)

num = 15
print("Prime" if check_prime(num) else "Not Prime")
