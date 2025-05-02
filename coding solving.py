1.Variable Swap: Write a Python program to swap the values of two variables without using a temporary variable
a=int(input('input 1st number:'))
b=int(input('input 2nd number:'))
a,b=b,a
print(a,b)

2.Even or Odd: Write a Python program that takes an integer as input and prints whether it is even or odd.
x=int(input('input number:'))
if x%2==0:
    print('even')
else:
    print('odd')

3.String Reverse: Write a Python function to reverse a given string and return the reversed string.
def reverse_string(s):
     return s[::-1]
y= input("enter the input line: ")
print("reversed strings:", reverse_string(y))
# connected y into function called in print

4.Type Conversion: Given a list of integers, write a Python program to convert each element of the list to a string.
numbers =(input('input numbers:'))
string_numbers=[str(num) for num in numbers]
print(string_numbers)

5. Temperature Converter: Write a Python program that converts a temperature in Celsius to Fahrenheit.
Take the Celsius temperature as input from the user.

celsius=float(input('enter the celsius:'))
fahreneit=(celsius * 1.8)+ 32
print(fahreneit)

6. Data Type Checker: Write a Python function that takes a variable as input and
returns the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.).
def check_var_type(variable):
    return type(variable)
print(check_var_type(12))
print(check_var_type(12.0))

7.String Palindrome: Write a Python function to check if a given string is a palindrome or not.
def pallin(string):
  if (string== string[::-1]):
    return 'the string is pallindrome'
  else:
    return "the string is not pallindrome"
string= input('enter the line:')
print(pallin(string))

8.write 2 string line and join them without '+' operator

string1 = (input('enter the line:'))
string2= (input('enter the line:'))

string3= "".join([string1,string2])
print (string3)

9. Given three variables: `a = ‘100’`, `b = 25`, and `c = ‘10.5’`, write a Python program to perform the following operations and print the results:
– Convert `a` to an integer and add it to `b`. – Convert `c` to a float and subtract it from the result of the first operation.
– Convert the final result to a string and concatenate it with the string ” is the answer.”

a='100'
b=25
c='10.5'

result1= int(a)+b
print(result1)
result2=result1 - float(c)
print(result2)
final_result=(str(result2))
print(final_result)


