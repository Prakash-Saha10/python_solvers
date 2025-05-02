69.Duplicate Removal: Write a Python program that takes a list of elements as input and creates a new set containing only the unique elements from the list.

def duplicate_remove(lst):
    unique=[]
    seen=set()
    for item in lst:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    return unique

input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
result=duplicate_remove(input_list)
print('unique elements',result)


Input from user
input_list = input("Enter elements separated by spaces: ").split()

# Convert input to appropriate data type if needed (e.g., int)
input_list = [int(i) for i in input_list]

# Convert list to set to remove duplicates
unique_set = set(input_list)

# Print the result
print("Unique elements:", unique_set)

70.Set Intersection: Given two sets A and B, write a Python program to find their intersection and print the common elements.
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

intersection = A & B

print("Common elements in A and B:", intersection)

71.Set Union: Given two sets A and B, write a Python program to find their union and print all the distinct elements from both sets.

set1=set(map(int,input('input numbers1:').split()))
set2=set(map(int,input('input numbers2:').split()))

union_set=set1.union(set2)

print('union set:',union_set)

72.Set Difference: Given two sets A and B, write a Python program to find the difference between set A and set B (i.e., elements present in A but not in B) and print the result.

A = set(map(int(input("Enter elements of set A separated by spaces: ").split())))
B = set(map(int(input("Enter elements of set B separated by spaces: ").split())))

# Find difference A - B
difference = A.difference(B)

# Print result
print("Elements in A but not in B:", difference)


73. Set Symmetric Difference: Given two sets A and B, write a Python program to find the symmetric difference between the two sets (i.e., elements that are present in either set A or set B, but not in both) and print the result.
A = set(map(int, input("Enter elements of set A separated by spaces: ").split()))
B = set(map(int, input("Enter elements of set B separated by spaces: ").split()))

# Calculate the symmetric difference
symmetric_diff = A.symmetric_difference(B)

# Print the result
print("Symmetric Difference (A Δ B):", symmetric_diff)


74. Set Operations: Given three sets A, B, and C, write a Python program to find and print the intersection of A and B, the union of B and C, and the difference between C and A.
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
C = {5, 6, 7, 8, 9}

# Intersection of A and B
intersection_AB = A & B
print("Intersection of A and B:", intersection_AB)

# Union of B and C
union_BC = B | C
print("Union of B and C:", union_BC)

# Difference between C and A (elements in C but not in A)
difference_CA = C - A
print("Difference between C and A:", difference_CA)

75. Set Subset Check: Given two sets A and B, write a Python program to check if set A is a subset of set B and print the result.

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

# Check if A is a subset of B
if A.issubset(B):
    print("Set A is a subset of Set B")
else:
    print("Set A is NOT a subset of Set B")

77.Set Length Check: Write a Python program that takes a set as input and prints the number of elements in the set.
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
# Check if A is a superset of B
if A.issuperset(B):
    print("Set A is a superset of Set B")
else:
    print("Set A is NOT a superset of Set B")

77.Set Length Check: Write a Python program that takes a set as input and prints the number of elements in the set.
user_set = set(map(int,input("Enter elements of set separated by spaces: ").split()))
print("Number of elements in the set:", len(user_set))

78.Set Membership Test: Write a Python program that takes an element as input and checks if it exists in a given set. Print “Found” if the element is present and “Not Found” otherwise.
# Define a sample set
sample_set = {1, 3, 5, 7, 9}

# Take input from the user
element = int(input("Enter an element: "))

# Check for membership in the set
if element in sample_set:
    print("Found")
else:
    print("Not Found")

