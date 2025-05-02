49.Tuple Concatenation: Write a Python program to concatenate two tuples and create a new tuple.
Define two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenate the tuples
concatenated_tuple = tuple1 + tuple2

# Print the result
print("First Tuple:", tuple1)
print("Second Tuple:", tuple2)
print("Concatenated Tuple:", concatenated_tuple)
50. Tuple Unpacking: Given a tuple with three elements (x, y, z), write a Python program to unpack the tuple and assign the values to three variables.# Define a tuple with three elements
coordinates = (5, 10, 15)

# Unpack the tuple into variables
x, y, z = coordinates

# Display the unpacked values
print("x =", x)
print("y =", y)
print("z =", z)

51.Tuple Sorting: Write a Python program to sort a tuple of integers in ascending order.


original_tuple = (23, 11, 45, 5, 78, 32)

Sort the tuple by converting it to a list, then back to a tuple
sorted_tuple = tuple(sorted(original_tuple))
Sort in descending order
sorted_desc_tuple = tuple(sorted(original_tuple, reverse=True))


print("Original Tuple:", original_tuple)
print("Sorted Tuple (Ascending Order):", sorted_tuple)
print("Sorted Tuple (Descending Order):", sorted_desc_tuple)


52.Tuple Frequency Count: Given a tuple containing various elements, write a Python program to count the frequency of a specific element in the tuple.
sample_tuple = (1, 2, 3, 2, 4, 2, 5, 3, 1, 2)

# Element to count
element = int(input('number to count:'))

# Count the frequency using count() method
frequency = sample_tuple.count(element)

# Display the result
print("Tuple:", sample_tuple)
print(f"Frequency of element {element}:", frequency)

53.Tuple to List: Write a Python program to convert a tuple into a lis
sample_tuple = (1, 2, 3, 2, 4, 2, 5, 3, 1, 2)

new_tuple=list(sample_tuple)

print('new_tuple:',new_tuple)

54. Tuple Reversal: Write a Python program to reverse a tuple without using any built-in functions.# Define the original tuple
original_tuple = (10, 20, 30, 40, 50)

# Convert to list manually
temp_list = []
for item in original_tuple:
    temp_list.append(item)

# Reverse the list manually
reversed_list = []
for i in range(len(temp_list) - 1, -1, -1):
    reversed_list.append(temp_list[i])

# Convert back to tuple
reversed_tuple = tuple(reversed_list)

# Display the results
print("Original Tuple:", original_tuple)
print("Reversed Tuple:", reversed_tuple)

55. Tuple Slicing: Given a tuple, write a Python program to extract a slice of elements from it.# Define the tuple
original_tuple = (10, 20, 30, 40, 50, 60, 70, 80)

# Extract a slice from index 2 to 5 (index 5 is not included)
sliced_tuple = original_tuple[2:6]

# Display the results
print("Original Tuple:", original_tuple)
print("Sliced Tuple (from index 2 to 5):", sliced_tuple)

56.Tuple Operations: Given two tuples of integers, write a Python program to perform element-wise addition, subtraction, and multiplication and create new tuples for each operation.

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (5, 4, 3, 2, 1)

add=tuple(x+y for x,y in zip(tuple1,tuple2))
subtract=tuple(x-y for x,y in zip(tuple1,tuple2))
multi=tuple(x*y for x,y in zip(tuple1,tuple2))

print('add:',add)
print('subtraction', subtract)
print('multiplication:',multi)



57.Tuple Membership Test: Write a Python program that takes an element as input and checks if it exists in a given tuple.sample_tuple = (10, 20, 30, 40, 50)

Take input from the user
element = int(input("Enter an element to check: "))

# Check if the element is in the tuple
if element in sample_tuple:
    print(f"The element {element} exists in the tuple.")
else:
    print(f"The element {element} does not exist in the tuple.")



58.Tuple Packing: Write a Python program to pack three variables into a single tuple and print the tuple.

var1 = 10
var2 = 20
var3 = 30

# Pack the variables into a tuple
packed_tuple = (var1, var2, var3)

# Print the packed tuple
print("Packed Tuple:", packed_tuple)