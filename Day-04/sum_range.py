# Day 04 - Sum of Numbers in a Given Range

# Method 1: Using for loop (Brute Force)
num1, num2 = 3, 6
total_sum = 0

for i in range(num1, num2 + 1):
    total_sum += i

print("Sum using loop:", total_sum)


# Method 2: Using formula
# Formula:
# Sum = (n2 * (n2 + 1)) // 2 - (n1 * (n1 + 1)) // 2 + n1
num1, num2 = 3, 6
formula_sum = (num2 * (num2 + 1)) // 2 - (num1 * (num1 + 1)) // 2 + num1
print("Sum using formula:", formula_sum)


# Method 3: Using recursion
def recursive_sum(current, end):
    if current > end:
        return 0
    return current + recursive_sum(current + 1, end)

num1, num2 = 3, 6
print("Sum using recursion:", recursive_sum(num1, num2))
