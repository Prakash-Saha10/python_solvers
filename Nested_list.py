44. Matrix Addition: Write a Python program to add two matrices represented as nested lists.

Function to add two matrices
def add_matrices(matrix1, matrix2):
    Check if matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions")
    # Create a new matrix with summed elements using list comprehensions
    result = [[matrix1[i][j] + matrix2[i][j]
               for j in range(len(matrix1[0]))]
              for i in range(len(matrix1))]
    return result
# Define the first matrix
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Define the second matrix
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
# Perform matrix addition by calling the function
result_matrix = add_matrices(matrix1, matrix2)
# Print the result row by row
for row in result_matrix:
    print(row)  # Output each row of the resulting matrix

matrix1[0] refers to the first row of matrix1, which is a list of numbers.
len(matrix1[0]) gives the number of columns in matrix1.
range(len(matrix1[0])) creates a loop that runs from 0 to the number of columns minus one.
j represents the column index, iterating over every column.

45. Flatten Nested List: Write a Python program to flatten a given nested list and convert it into a single-dimensional list.
Function to flatten a nested list
def flatten_list(nested_list):
    flat_list = []  # Initialize an empty list to store flattened elements

    for element in nested_list:  # Loop through each element in the nested list
        if isinstance(element, list):  # Check if the element is a list
            flat_list.extend(flatten_list(element))  # Recursively flatten the sublist and add its elements
        else:
            flat_list.append(element)  # If it's not a list, add it directly

    return flat_list  # Return the fully flattened list
# Example nested list
nested_list = [[1, 2, [3, 4]], [5, 6], [7, [8, 9]]]

# Flatten the list
flat_list = flatten_list(nested_list)

# Print the flattened list
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

What’s Happening Here?
Looping Through the Nested List
for element in nested_list: → This goes through each item in nested_list one by one.
If nested_list is something like [[1, 2, [3]], [4, 5]], the loop will process:
[1, 2, [3]]
[4, 5]
Checking if an Item is Another List
if isinstance(element, list): → This checks whether the current item (element) is a list.
If it's a number, we don't need to flatten it, so we skip to the next step.
If it’s another list, we need to break it down further.
Flattening the Sublist Recursively
flat_list.extend(flatten_list(element))
What is happening here?
The function calls itself (flatten_list(element)), meaning it will repeat the process for element if it’s another list.
The extend() function adds all elements from the sublist directly to flat_list instead of adding the list itself.

First iteration → element = [1, 2, [3]] (a list)
Calls flatten_list([1, 2, [3]])
1 and 2 get added to flat_list
flatten_list([3]) is called → adds 3 to flat_list
Second iteration → element = [4, 5] (a list)
Calls flatten_list([4, 5])
Adds 4 and 5 to flat_list
Final output: [1, 2, 3, 4, 5]
Why Use Recursion?
Recursion allows us to handle deeply nested lists, no matter how many levels of nesting exist.

46.List Element Frequency: Given a nested list containing lists of integers, write a Python program to count the frequency of each element in the entire nested list.

from collections import Counter
nested_list=[[1,2,3],[7,8,8],[4,5,6]]

flat_list =[num for sublist in nested_list for num in sublist]
frequency=Counter(flat_list)
print(frequency)

47.Transpose Matrix: Write a Python program to transpose a given matrix represented as a nested list.

def transpose_matrix(matrix):
    return[list(row)for row in zip(matrix)]

matrix=[
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

transposed=transpose_matrix(matrix)

print('original matrix:')
for row in matrix:
     print(matrix)
print('\n Transposed matrix:')
for row in transposed:
        print(row)


another version

def transpose_matrix_manual(matrix):
    # Initialize the transposed matrix with empty lists for each column
    transposed = []
    for i in range(len(matrix[0])):  # Iterate over columns of the original matrix
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        transposed.append(new_row)
    return transposed

# Transposing the example matrix manually
transposed_manual = transpose_matrix_manual(matrix)

print("\nTransposed Matrix (Manual Method):")
for row in transposed_manual:
    print(row)

48.List of Lists Concatenation: Given a list of nested lists, write a Python program to concatenate all the sublists into a single flat list.

def flatten_list(nested_lists):
    # Iterates over each sublist and then each element in the sublist
    return [element for sublist in nested_lists for element in sublist]

# Example list of nested lists
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Concatenating all sublists into one flat list
flat_list = flatten_list(nested_list)

print("Concatenated flat list:", flat_list)