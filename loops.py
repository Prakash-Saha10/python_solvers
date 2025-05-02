20.Sum of N Numbers: Write a Python program using a for loop to
calculate the sum of the first N natural numbers, where N is taken as input from the user.

N=int(input('number :'))
total_sum=0     #sum varirable
for i in range(1,N+1): #loop from 1 to N
    total_sum += i #Add each number

    print('the value:' ,N ,'and the number',total_sum)

Sum of N natural numbers using a for loop
Take input from the user
N = int(input("Enter a positive integer N: "))
# Initialize sum
total_sum = 0
# Use for loop to calculate the sum
for i in range(1, N + 1):
    total_sum += i
# Display the result
print("The sum of the first", N, "natural numbers is:", total_sum)
21.Factorial Calculator: Write a Python program using a while loop to calculate the factorial of a given number N.
N= int(input('give the number: '))

factorial =1
i=1

if N<0:
    print('dont put neg number or zero')
else:
    while i <= N:
        factorial *= i
        i += 1
    print(f"The factorial of {N} is: {factorial}")

22.Table of a Number: Write a Python program using a for loop to print the multiplication table of a given number N.
n=int(input('print the number: '))
for i in range (1,11):
     print(f'{n} x {i} ={n * i}')

23. Count Digits in a Number: Write a Python program using a while loop to count the number of digits in a given integer N.
N=int(input('count the number: '))
num=abs(N)
if num ==0:
    count =1
else:
    count=0
    while num > 0:
        num //= 10
        count += 1
print(f'print the digit count: {count}')
24. Fibonacci Sequence: Write a Python program using a for loop to generate the Fibonacci sequence up to a given limit N.
N= int(input('print the number: '))
a,b=0,1
for _ in range(N):
    if a>N:
        break
    print(a,end= " ")
    a, b = b , a+b

25.Sum of Even Numbers: Write a Python program using a while loop to calculate the
sum of all even numbers between 1 and N, where N is taken as input from the user.
N=int(input('print the number: '))
i=1
sum_even =0

while i<=N:
    if i % 2 == 0:
        print(f'{i} is even')
        sum_even +=i
    i +=1
print(f'the sum of all even number between 1 to {N} is : {sum_even}')

26.Print Patterns: Write a Python program using nested for loops to print various patterns,
such as a right-angled triangle, an inverted right-angled triangle, and so on.

# Number of rows for the patterns
rows = 5

# 1. Right-angled triangle
print("1. Right-angled triangle:")
# Outer loop for rows
for i in range(1, rows + 1):
    # Inner loop for printing stars
    for j in range(i):
        print("*", end=" ")
    print()  # New line after each row
# 2. Inverted right-angled triangle
print("\n2. Inverted right-angled triangle:")
# Outer loop for rows (in reverse)
for i in range(rows, 0, -1):
    # Inner loop for printing stars
    for j in range(i):
        print("*", end=" ")
    print()  # New line after each row
# 3. Pyramid pattern
print("\n3. Pyramid pattern:")
# Outer loop for rows
for i in range(1, rows + 1):
    # Print spaces to align stars in center
    print(" " * (rows - i), end="")
    # Print stars with space
    print("* " * i)
# 4. Inverted pyramid pattern
print("\n4. Inverted pyramid pattern:")
# Outer loop for rows (in reverse)
for i in range(rows, 0, -1):
    # Print spaces for alignment
    print(" " * (rows - i), end="")
    # Print stars
    print("* " * i)
# 5. Diamond pattern
print("\n5. Diamond pattern:")
# Top half of the diamond
for i in range(1, rows + 1):
    # Print spaces for alignment
    print(" " * (rows - i), end="")
    # Print stars
    print("* " * i)
# Bottom half of the diamond
for i in range(rows - 1, 0, -1):
    # Print spaces for alignment
    print(" " * (rows - i), end="")
    # Print stars
    print("* " * i)

27.Prime Number Checker: Write a Python program using a while loop to check if a given number N is prime or not.

N= int(input('print a number:'))

if N<=1:
    print('this is not Prime Number')
else:
    i=2   #the shortest prime
    is_prime=True    #is prime works variable here

    while i<= N //2:
        if N%i ==0:
            is_prime = False
        break
       # i +=1

    if is_prime:
        print(f'{N} is a prime number')
    else:
        print('this is not prime')


28.List Manipulation: Given a list of integers,
write a Python program using a for loop to find the sum, average, maximum, and minimum values in the list.

N =[6,6,5,3,7,8,9]
#initialize variables
total=0
maximum = N[0]
minimum=N[0]
for num in N:
    total += num

    if num > maximum:
        maximum= num
    if num < minimum:
        minimum= num

average =total/len(N)

print('Numbers:',N)
print('Sum:',total)
print('Maximum:',maximum)
print('Minimum:',minimum)
print('Average:',average)

29. Reverse String: Write a Python program using a while loop to reverse a given string.

N=str(input("write your line: "))
reverse_string =""
index = len(N) -1  #len(string) tells how many charecters not last index
#so we subtract 1 to get the correct position as string

while index >= 0: #untill we move to 0
    reverse_string += N[index] #+ add it to the reverse string
    index -= 1   #move to previous letter

print('reversed string:',reverse_string)