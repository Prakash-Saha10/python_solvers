102.Factorial Calculator: Write a Python function called `factorial` that takes an integer as input and returns its factorial. Test the function with different values.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Getting user input only once (optional)
num = int(input("Enter a number to calculate factorial: "))
print(f"Factorial of {num}: {factorial(num)}")
# Other test cases
print("Factorial of 0:", factorial(0))
print("Factorial of 1:", factorial(1))
print("Factorial of 5:", factorial(5))
print("Factorial of 10:", factorial(10))

103. Palindrome Checker: Write a Python function called `is_palindrome` that takes a string as input and returns `True` if it is a palindrome and `False` otherwise. Test the function with different words.
def is_palindrome(s):
    # Normalize: lowercase and remove spaces
    s = s.lower().replace(" ", "")
    return s == s[::-1]
user_input = input("Enter a word or sentence: ")
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

104. Even or Odd Checker: Write a Python function called `even_or_odd` that takes an integer as input and returns “Even” if the number is even and “Odd” if the number is odd. Test the function with different numbers.
def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number: "))
print(f"The number {num} is", even_or_odd(num))


105. List Sum Calculator: Write a Python function called `list_sum` that takes a list of integers as input and returns the sum of all elements in the list. Test the function with different lists.
def list_sum(numbers):
    return sum(numbers)

# User input
user_input = input("Enter a list of numbers separated by commas: ")
# Convert input string to a list of integers
number_list = [int(num.strip()) for num in user_input.split(',')]
print("Sum of the list is:", list_sum(number_list))

#another_version
def list_sum(numbers):
    return sum(numbers)

try:
    user_input = input("Enter numbers separated by commas: ")
    number_list = [int(num.strip()) for num in user_input.split(',')]
    print("Sum of the list is:", list_sum(number_list))
except ValueError:
    print("Please enter only valid integers separated by commas.")


106. Greatest Common Divisor (GCD) Calculator: Write a Python function called `gcd` that takes two integers as input and returns their greatest common divisor. Test the function with different pairs of numbers.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)  # Ensure GCD is positive

# User input
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print(f"GCD of {x} and {y} is:", gcd(x, y))

107. Leap Year Checker: Write a Python function called `is_leap_year` that takes a year as input and returns `True` if it is a leap year and `False` otherwise. Test the function with different years.

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# User input
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")