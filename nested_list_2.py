59.Nested List Element Access: Given a nested list, write a Python program to access and print specific elements from it.


nested_number=[[1,2,3],[7,8,9],[6,5,4]]


element1=nested_number[0][1]
print('element 1:' ,element1)

element2= nested_number[1][2]
print('element2:' ,element2)

60.Nested List Flattening: Write a Python program to flatten a nested list and convert it into a single-dimensional list.

def flatten_list(nested_list):
    flat_list=[]
    for element in nested_list:
        if isinstance(element,list):
            flat_list.extend(flatten_list(element))
        else:
            flat_list.append(element)
    return flat_list

nested=[1,[2,3],[4,[5,7]]]
flattend=flatten_list(nested)

print('flattened list:',flattend)

Iteration: The function iterates over each element in the nested_list.
If the element is a list (checked using isinstance(element, list)), the function calls itself recursively to flatten that element. The resulting flattened data is then merged into flat_list using extend().
If the element is not a list, it is appended directly to flat_list.

61. Nested List Sorting: Given a nested list containing lists of integers, write a Python program to sort the sublists based on their lengths.
nested_list = [[1, 2, 3], [4], [5, 6], [7, 8, 9, 10]]
sorten=sorted(nested_list,key=len)

print('sorted by method:' ,sorten)

62.List of Tuples Conversion: Given a nested list containing tuples of (x, y) coordinates, write a Python program to convert it into a list of x-coordinates and a list of y-coordinates.
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
x_coords=[point[0] for point in coordinates]
y_coords=[point[1]for point in coordinates]
print("X-Coordinates:", x_coords)
print("Y-Coordinates:", y_coords)

63. Matrix Transpose: Write a Python program to transpose a given matrix represented as a nested list.
Original matrix (represented as a nested list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Initialize an empty result matrix with transposed dimensions.
# The new matrix will have as many rows as the original had columns and vice versa.
result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]



This wraps the inner list comprehension in another list comprehension.
The outer loop runs for as many times as there are columns in the original matrix (n times).
For each iteration of this outer loop, it creates a new inner list (with m zeros).
Thus, you end up with n lists, each of length m, forming a new nested list (or matrix) that has the dimensions of the transposed matrix.

# Iterate over each element and swap indices (i, j) -> (j, i)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        result[j][i] = matrix[i][j]

# Print the transposed matrix
for row in result:
    print(row)


64.Nested List Concatenation: Given a list of nested lists, write a Python program to concatenate all the sublists into a single flat list.
import itertools
nested_list=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list=list(itertools.chain.from_iterable(nested_list))
print("Flat list:", flat_list)

65. Count Even Numbers: Write a Python program to count the number of even numbers in a nested list.
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9, 10],
    [11, 12]
]

even_count=0

for sublist in nested_list:
    for number in sublist:
        if number %2 ==0:
            even_count+=1
print('even_count:',even_count)

66. Maximum Element in Nested List: Write a Python program to find the maximum element in a nested list of integers.
nested_list = [
    [5, 3, 9, 1],
    [2, 8, 3],
    [7, 4],
    [10, 6, 8]
]

# Flatten the nested list into a single list
flat_list = [num for sublist in nested_list for num in sublist]

Nested List Comprehension Structure: The expression inside the square brackets [ ... ] has two for clauses:
Outer loop: for sublist in nested_list This loop iterates over each element in nested_list. Here, each sublist is itself a list.
Inner loop: for num in sublist For each sublist obtained from the outer loop, this inner loop iterates over every element (num) in the current sublist.
Element Collection: The expression starts with num, which means that for every num obtained in the inner loop, it will be collected into a new list. Essentially, it gathers every element from every sublist into one flat list.

# Find the maximum element in the flat list
max_element = max(flat_list)

print("Maximum element (Method 1):", max_element)

67. Diagonal Sum of Matrix: Given a square matrix represented as a nested list, write a Python program to calculate the sum of the elements in the main diagonal.
# Define a square matrix represented as a nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Use a generator expression with the built-in sum() function.
# For a square matrix, the main diagonal elements are the ones where the row index equals the column index.
diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
#uses a generator expression that iterates over the index i from 0 to n-1 (where n is the number of rows, obtained by len(matrix)). For each i, it accesses matrix[i][i]—the element on the main diagonal—and sums them up.

print("Diagonal Sum:", diagonal_sum)

68. Nested List Element Search: Write a Python program to search for a specific element in a nested list and return its position (row and column indices).

def find_element(nested_list, target):

    for row_index, row in enumerate(nested_list):
        for col_index, element in enumerate(row):
            if element == target:
                return row_index, col_index  # Return as soon as a match is found
    return None  # Return None if the target is not found


# Example usage:
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 5
position = find_element(nested_list, target)

if position:
    print(f"Element {target} found at row {position[0]}, column {position[1]}")
else:
    print(f"Element {target} not found in the nested list.")
