92. Prime Number Checker: Write a Python program that takes a number as input and determines if it is a prime number or not. Use a `for` loop to check for factors. If a factor is found, `break` out of the loop.

num = int(input("Enter a number: "))

# Handle special cases
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    # Assume the number is prime
    is_prime = True
    # Check for factors from 2 to sqrt(num)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break  # Exit the loop if a factor is found
(If num = 29,
then int(29**0.5) = int(5.38) = 5
So we check: range(2, 6) → 2, 3, 4, 5
If no number in that range divides 29, it’s prime.)_
((If a number n has a factor greater than √n,
it must have a smaller factor less than √n.))

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

93. Even Number Printer: Write a Python program to print all even numbers from 1 to 20. Use a `for` loop and `continue` to skip odd numbers.

for num in range(1, 21):  # Loop from 1 to 20
    if num % 2 != 0:  # Check if the number is odd
        continue  # Skip the odd numbers
    print(num)  # Print only even numbers

94.Password Validator: Write a Python program that takes a password as input and checks if it meets the following criteria: at least 8 characters long, contains both uppercase and lowercase letters, and has at least one digit. If the password is valid, print “Password accepted.” If not, use `continue` to prompt the user to enter a valid password.

while True:
    password = input("Enter a password: ")

    # Check conditions
    if len(password) < 8 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit() for char in password):
        print("Invalid password. Try again.")
        continue  # Prompt user again without moving forward

    print("Password accepted.")
    break  # Exit loop when a valid password is entered
while use here to continue if you entered invalid password,

95. Divisible by 3 or 5: Write a Python program to print all numbers from 1 to 50 that are divisible by either 3 or 5. Use a `for` loop and `continue` to skip numbers that are not divisible by either 3 or 5.

for num in range(1, 51):  # Loop from 1 to 50
    if num % 3 != 0 and num % 5 != 0:  # Check if the number is NOT divisible by 3 or 5
        continue  # Skip numbers that do not meet the condition
    print(num)  # Print numbers that are divisible by 3 or 5

96.Positive Number Sum: Write a Python program that takes positive numbers as input until a negative number is entered. Then, calculate and print the sum of all positive numbers entered. Use a `while` loop and `break` to exit the loop when a negative number is encountered.

total = 0  # Initialize the accumulator to zero

while True:
    # Get the user's input; converting it to an integer.
    number = int(input("Enter a positive number (or negative to quit): "))

    # If the user enters a negative number, break out of the loop.
    if number < 0:
        break

    # Add the positive number to the total.
    total += number

# After the loop ends, print the accumulated sum.
print("Sum of positive numbers:", total)

97. Word Palindrome Checker: Write a Python program that takes a word as input and checks if it is a palindrome (reads the same forwards and backward). Use `continue` to skip checking the word if its length is less than 3 characters.
while True:
    word = input("Enter a word: ")

    # Skip checking if the word is too short
    if len(word) < 3:
        print("Word must have at least 3 characters, please try again.")
        continue  # Immediately go back to the start of the loop

    # Check if the word is a palindrome by comparing it with its reverse
    if word == word[::-1]:
        print("The word is a palindrome.")
    else:
        print("The word is not a palindrome.")

    break  # Exit the loop after checking a valid word

98. Odd Number Finder: Write a Python program to find the first odd number from a list of integers. Use a `for` loop and `break` to stop the loop when the first odd number is found.

numbers = [4, 8, 10, 15, 22, 31]  # Example list of integers

for num in numbers:
    if num % 2 == 1:  # Check if the number is odd
        print("First odd number found:", num)
        break  # Exit the loop after finding the first odd number


99.Number Guessing Game: Write a Python program that generates a random number between 1 and 100 and lets the user guess the number. Use a `while` loop, `break` when the correct number is guessed, and `continue` to keep prompting the user until they guess correctly.
import random

# Generate a random number between 1 and 100
target = random.randint(1, 100)

print("Guess the number (between 1 and 100)!")

while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < 1 or guess > 100:
            print("Please guess a number within the range!")
            continue  # Prompts the user again without checking correctness

        if guess == target:
            print("Congratulations! You guessed the correct number.")
            break  # Exit the loop when the correct number is guessed
        elif guess < target:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")

print("Game Over!")

100.Vowel Counter: Write a Python program that takes a string as input and counts the number of vowels (a, e, i, o, u) in it. Use a `for` loop and `continue` to skip counting non-vowel characters.
input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for char in input_string:
    if char not in vowels:
        continue
    else:
       vowel_count += 1
print("Number of vowels in the string:", vowel_count)

101.Unique Characters: Write a Python program that takes a string as input and checks if it contains all unique characters (no character repeats). Use a `for` loop and `break` when a character repeats.
input_string = input("Enter a string: ")
# Initialize an empty set to track characters that have been seen
seen_characters = set()
# Assume the string is unique until a duplicate is found
unique = True
# Iterate through each character in the string
for char in input_string:
    if char in seen_characters:
        print(f"Duplicate character found: {char}")
        unique = False
        break  # Exit the loop immediately upon finding a duplicate
    seen_characters.add(char)
if unique:
    print("All characters in the string are unique.")

