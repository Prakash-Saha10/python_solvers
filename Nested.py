30.Multiplication Table: Write a Python program using nested loops to print the multiplication table from 1 to 10.

for i in range(1,11):
    for j in range(1,11):
        print(f'{i} x {j} = {i*j}', end='\t')
    print()

31.Print Patterns: Write a Python program using nested loops to print the following pattern:
*
**
***
****
*****

rows=6
for i in range(1,rows+1):
    for j in range(i):
        print('*',end='')
    print()

{The outer loop controls how many lines you want (from 1 to 5).
The inner loop prints * as many times as the current row number (i).
end="" is used to keep printing on the same line.
After printing the stars in one row, print() moves to the next line}.

32. Matrix Multiplication: Write a Python program using nested loops to multiply two matrices.

# Define the matrices
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]
# Get the dimensions of the matrices
rows_A, cols_A = len(A), len(A[0])
rows_B, cols_B = len(B), len(B[0])
# Ensure matrix multiplication is possible
if cols_A != rows_B:
    print("Matrix multiplication is not possible.")
else:
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication using nested loops
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or rows_B, since cols_A == rows_B
                result[i][j] += A[i][k] * B[k][j]

    # Print the resulting matrix
    for row in result:
        print(row)

33. Chessboard Pattern: Write a Python program using nested loops to print a chessboard pattern (alternating “X” and “O” characters) of size 8×8.

size=int(input('chessboard size: '))
for row in range(size):
    for col in range(size):
        if (row+col)%2==0:
            print('x' ,end=" ")
        else:
            print('o' ,end=" ")
    print()


34.Number Pyramid: Write a Python program using nested loops to print a number pyramid like the following: 1 22 333 4444 55555

rows=int(input('print a number: '))
for i in range(1, rows+1):
    for j in range(i):
        print(i, end='')
    print('')

