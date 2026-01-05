# Day 03 - Sum of First N Natural Numbers

# Method 1: Using for loop
num = 5
total_sum = 0

for i in range(1, num + 1):
    total_sum += i

print("Sum using for loop:", total_sum)


# Method 2: Using formula
# Formula: n * (n + 1) // 2
num = 5
print("Sum using formula:", num * (num + 1) // 2)


# Method 3: Using recursion
def get_sum(n):
    if n == 1:
        return 1
    return n + get_sum(n - 1)

num = 5
print("Sum using recursion:", get_sum(num))
