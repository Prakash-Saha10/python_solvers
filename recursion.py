111. Factorial Calculation: Write a recursive Python function called `factorial` that takes a non-negative integer as input and returns its factorial.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
try:
    number = int(input("Enter a non-negative integer: "))
    if number < 0:
        print("Error: Please enter a non-negative integer.")
    else:
        print(f"Factorial of {number} is {factorial(number)}")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")

112. Fibonacci Series: Write a recursive Python function called `Fibonacci` that takes an integer N as input and returns the Nth number in the Fibonacci series. The Fibonacci series is defined as follows: F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
try:
    N = int(input("Enter a non-negative integer N: "))
    if N < 0:
        print("Error: Please enter a non-negative integer.")
    else:
        print(f"The {N}th Fibonacci number is: {Fibonacci(N)}")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")

113. The sum of Digits: Write a recursive Python function called `sum_of_digits` that takes an integer as input and returns the sum of its digits.
def sum_of_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
# n % 10:
# The modulus operator (%) returns the last digit of the number n.
# For example, if n = 123, then n % 10 will return 3 (the last digit).
# sum_of_digits(n // 10):
# The floor division operator (//) divides the number n by 10 and discards the decimal part, effectively removing the last digit of n.
# For example, if n = 123, then n // 10 will return 12 (after removing the last digit).
# The function then recursively calls sum_of_digits(n // 10) to find the sum of the digits of the remaining part of the number.
try:
    number = int(input("Enter an integer: "))
    print("Sum of digits:", sum_of_digits(number))
except ValueError:
    print("Error: Please enter a valid integer.")

114. Binary Search: Write a recursive Python function called `binary_search` that takes a sorted list and a target value as input and returns the index of the target value in the list using binary search. If the target value is not in the list, return -1.

def binary_search(arr, target, low=0, high=None):
    # Initialize high on the first call if not provided.
    if high is None:
        high = len(arr) - 1
    # Base case: if the search region is empty, the target isn't present.
    if low > high:
        return -1
    # Find the midpoint of the current search range.
    mid = (low + high) // 2
    # If the middle element is the target, return its index.
    if arr[mid] == target:
        return mid
    # If the middle element is greater than the target,
    # search recursively in the left half.
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    # Otherwise, search recursively in the right half.
    else:
        return binary_search(arr, target, mid + 1, high)
sorted_list = [2, 4, 6, 8, 10, 12, 14]
target_value = 10
result = binary_search(sorted_list, target_value)
if result != -1:
    print(f"Target {target_value} found at index {result}.")
else:
    print(f"Target {target_value} not found in the list.")

115. Power Calculation: Write a recursive Python function called `power` that takes two positive integers, base and exponent, as input and returns the value of base raised to the exponent.
def power(base, exponent):
    """Recursively calculates base^exponent."""
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print(f"{base}^{exponent} =", power(base, exponent))


