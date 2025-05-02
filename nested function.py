108.Math Operations: Write a Python function called `math_operations` that takes three numbers and a string representing an operation (‘add’, ‘subtract’, ‘multiply’, or ‘divide’). The function should return the result of the specified operation on the three numbers. Implement the math operations as nested functions.
def math_operations(a, b, c, operation):
    def add(x, y, z):
        return x + y + z

    def subtract(x, y, z):
        return x - y - z

    def multiply(x, y, z):
        return x * y * z

    def divide(x, y, z):
        try:
            return x / y / z
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

    if operation == 'add':
        return add(a, b, c)
    elif operation == 'subtract':
        return subtract(a, b, c)
    elif operation == 'multiply':
        return multiply(a, b, c)
    elif operation == 'divide':
        return divide(a, b, c)
    else:
        return "Error: Invalid operation."

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    op = input("Enter the operation (add, subtract, multiply, divide): ").lower()

    result = math_operations(num1, num2, num3, op)
    print("Result:", result)
except ValueError:
    print("Error: Please enter valid numbers.")

109. Greeting Generator: Write a Python function called `greeting_generator` that takes a name as input and returns a greeting message using nested functions. The greeting message should be customizable (e.g., “Hello, {name}! How are you today?”).
def greeting_generator(name):
    def create_greeting():
        return f"Hello, {name}! How are you today?"
    return create_greeting()
user_name = input("Enter your name: ")
message = greeting_generator(user_name)
print(message)

110. Temperature Converter: Write a Python function called `temperature_converter` that takes a temperature value and a string representing the scale (‘C’ for Celsius or ‘F’ for Fahrenheit) as input. The function should convert the temperature from one scale to the other using nested functions and return the converted value.
def temperature_converter(value, scale):
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

    if scale.upper() == 'C':
        return celsius_to_fahrenheit(value)
    elif scale.upper() == 'F':
        return fahrenheit_to_celsius(value)
    else:
        return "Error: Scale must be 'C' or 'F'."
try:
    temp = float(input("Enter the temperature value: "))
    scale = input("Enter the scale ('C' for Celsius or 'F' for Fahrenheit): ")
    result = temperature_converter(temp, scale)
    print("Converted temperature:", result)
except ValueError:
    print("Error: Please enter a valid number.")