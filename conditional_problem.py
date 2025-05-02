11.Positive, Negative, or Zero: Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.

x=float(input("Enter the input: "))
if x>0:
    print('positive')
elif x==0:
    print('zero')
else:
    print('negative')

12.Largest of Three Numbers: Write a Python program that takes three numbers as input and prints the largest among them.
a=int(input("the number1: "))
b=int(input("the number2: "))
c=int(input('the number3: '))
#
if a>b and a>c:
    print("a is the largest")
elif b>a and b>c:
    print('b is the largest')
else:
    print('c is the largest')

13.Leap Year Checker: Write a Python program that takes a year as input and determines if it is a leap year or not.

year=int(input('enter the year: '))

if (year%400==0) or (year%100!=0 and year%4==0):
    print ('leap year')
else:
    print('not leap year')
14. Grades Classification: Write a Python program that takes a student’s percentage
as input and prints their corresponding grade according to the following criteria:
– 90% or above: A+ – 80-89%: A – 70-79%: B – 60-69%: C – Below 60%: Fail

marks=float(input("tell the mark: "))

if marks>=90:
    print('A+')
elif marks>=80:
    print('A')
elif marks>=70:
    print('B')
elif marks>=60:
    print('C')
else:
    print('Fail')
15. Vowel or Consonant: Write a Python program that takes a single character as input and determines
whether it is a vowel or a consonant.

word=str(input('tell your word:' ' ').lower())
if word in ['a','e','i','o','u']:
    print("vowel")
elif word.isalpha() :
    print('constant')
else:
    print('invalid input')
16. Time Classification: Write a Python program that takes the time in hours (24-hour format) as input and
prints “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night” based on the time.

hour=int(input("say your time:" ))

if 5 <= hour < 12:
    print("Good Morning")
elif 12 <= hour <17:
    print("Good Afternoon")
elif 17 <= hour <21:
    print('Good Evening')
else:
    print("Good Night")
17.Triangle Type Checker: Write a Python program that takes three sides of a triangle as input and determines
whether it forms an equilateral, isosceles, or scalene triangle.

a=float(input('say the side1:'))
b=float(input('say the side2:'))
c=float(input('say the side3:'))

Check if it's a valid triangle
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or c == a:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid triangle")

8.Quadratic Equation Solver: Write a Python program that takes the coefficients (a, b, c) of a quadratic equation as input and calculates
and prints the real roots (if they exist) or a message indicating the complex roots.
import math

a=int(input("the number1: "))
b=int(input("the number2: "))
c=int(input('the number3: '))

d= b**2-4*a*c #calculate discriminant

if d>0:
    root1=(-b+math.sqrt(d)) /(2*a)
    root2=(-b-math.sqrt(d)) /(2*a)
    print(f'two real roots: {root1} and {root2}')
elif d==0:
    root =-b /(2*a)
    print(f'one real root: {root}')
else:
    print('complex roots:no real solution')

19.Number Ranges: Write a Python program that takes an integer as input
and prints whether the number falls within the ranges: 0-50, 51-100, 101-150, or above 150.

x=int(input('tell your input number:'))

if 0 <= x <= 50:
    print('i am in 50')
elif 51 <= x <= 100:
    print('i am in 100')
elif 101 <= x <=150:
    print('i am in 150')
else:
    print('150 above')

