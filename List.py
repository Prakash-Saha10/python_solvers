35.List Sum: Write a Python program to find the sum of all elements in a given list of integers.

numbers=[3,4,5,7,8,8]

total=0

for num in numbers:
    total +=num
print('sum of all numbers' ,total)

36.List Average: Write a Python program to calculate the average of all elements in a given list of integers.
numbers=[3,4,5,7,8,8]
total=0

for num in (numbers):
     total+=num
avg=total/len(numbers)
print('average', avg)
36.List Max and Min: Write a Python program to find the maximum and minimum values in a given list of integers.

numbers=[2,34,5,43,54,76,1213]

maximum=max(numbers)
minimum=min(numbers)

print('numbers',numbers)
print('maximum number',maximum)
print('minimum number',minimum)


37.List Sorting: Write a Python program to sort a list of integers in ascending order.

numbers=[2,34,5,43,54,76,1213]

sorted_list=sorted(numbers)

print('sort numbers:',sorted_list)

Bubble Sort in Python with Comments

Define a list of unsorted integers
numbers = [12, 5, 23, 1, 89, 45]

Get the number of elements in the list
n = len(numbers)

# Outer loop: Runs n-1 times
for i in range(n):
    # Inner loop: Goes through the list and compares adjacent items
    for j in range(0, n - i - 1):
        # Compare two adjacent elements
        if numbers[j] > numbers[j + 1]:
            # Swap if the left element is greater than the right
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

        # Print the list after each inner loop iteration (optional)
        # print(f"Step {i}-{j}: {numbers}")

# Print the sorted list
print("Sorted list in ascending order:", numbers)

38.List Filtering: Given a list of integers, write a Python program to create a new list that contains only the even numbers from the original list.

numbers=[3,4,5,2,6,8,10]
for num in numbers:

    if num %2 == 0:
       print('even',num)
    else:
       print('not even',num)
39. List Reversal: Write a Python program to reverse a given list without using any built-in functions.
numbers=[3,4,5,2,6,8,10]
reverse_list=[]

for i in range (len(numbers)-1,-1,-1):
    reverse_list.append (numbers[i])

print('reverse list',reverse_list)

40.List Manipulation: Given two lists of integers, write a Python program to create a new list that contains elements common to both lists.
numbers1 =[3,4,5,2,6,8,10]
numbers2 = [12,5,23,1,10,89,45]

numbers3=list(set(numbers1)& set(numbers2))

print('common number',numbers3)

41. List Element Count: Write a Python program to count the occurrences of a specific element in a given list.
# Function to count occurrences of a specific element in a list
def counting(lst, elements):
    return lst.count(elements)
my_list = [1, 2, 3, 4, 3, 2, 5, 6, 3, 2]
# Taking user input and converting it to an integer
element_to_count = int(input('Enter the element to count: '))

# Calling the function
count = counting(my_list, element_to_count)

# Displaying the result
print(f"List: {my_list}")
print(f"The element {element_to_count} appears {count} times.")
42. List Duplicates Removal: Write a Python program to remove duplicates from a given list while preserving the order of the elements.
def remove_duplicates(my_list):
    seen = set() #set() helps us check for duplicates quickly.
    result = []  # Use list instead of tuple

    for item in my_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Test list
my_list = [2, 3, 2, 3, 4, 5, 6, 7]

# Function call
unique_list = remove_duplicates(my_list)

# Output the result
print(unique_list)

43. List Comprehension: Given a list of integers, write a Python program to create a new list that contains the squares of the elements using list comprehension.
#Original list of integers
numbers = [1, 2, 3, 4, 5]

# Create a new list with squares using list comprehension
squares = [x**2 for x in numbers]

# Print the result
print("Original list:", numbers)
print("List of squares:", squares)