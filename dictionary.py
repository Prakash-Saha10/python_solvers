79.Dictionary Manipulation: Given a dictionary with student names as keys and their corresponding scores as values, write a Python program to add a new student to the dictionary and update the score of an existing student.
new={
    'alice':76,
    'bob':90,
     'charlies':78
}

new['David']=99
new['bob']=45

print(new)

80.Dictionary Keys and Values: Write a Python program that takes a dictionary as input and prints all the keys and values in separate lines.
# Define a sample dictionary
students_scores = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

# Print all keys
print("Keys:")
for key in students_scores.keys():
    print(key)

# Print all values
print("\nValues:")
for value in students_scores.values():
    print(value)


81.Dictionary Length: Write a Python program to calculate and print the number of key-value pairs in a given dictionary.
students_scores = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 88
}

# Calculate and print the number of key-value pairs
print("Number of key-value pairs:", len(students_scores))


81.Dictionary Value Search: Given a dictionary of items and their prices, write a Python program to search for an item based on its price and print the item’s name.

items = {
    "apple": 120,
    "banana": 50,
    "mango": 150,
    "orange": 100,
    "grapes": 200
}

# Take price input from the user
search_price = int(input("Enter the price to search for: "))
    print('doesnot match')
# Flag to track if item was found
found = False

# Search for item(s) with the given price
for item, price in items.items():
    if price == search_price:
        print(f"Item found: {item}")
        found = True

if not found:
    print("No item found with that price.")

82.Dictionary Key Removal: Given a dictionary of items and their quantities, write a Python program to remove a specific item from the dictionary based on user input.

inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

item_to_remove=input('select a item to remove: ')

if item_to_remove in inventory:
    del inventory[item_to_remove]
    print('item out from inventory')
else:
    print('item does not found')

print('updated inventory,' ,inventory)

83. Dictionary Sorting: Given a dictionary with names as keys and corresponding ages as values, write a Python program to sort the dictionary based on age in ascending order.

# Sample dictionary
ages = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 22,
    "David": 28
}

# Sorting dictionary by age (ascending order)
sorted_ages = dict(sorted(ages.items(), key=lambda item: item[1]))

# Display sorted dictionary
print("Sorted dictionary:", sorted_ages)

84. Dictionary Frequency Count: Write a Python program that takes a string as input and creates a dictionary containing each character as a key and its frequency as the value.
# Get user input
text = input("Enter a string: ")

# Initialize an empty dictionary
char_count = {}

# Count character frequencies
for char in text:
    char_count[char] = char_count.get(char, 0) + 1

# Display the frequency dictionary
print("Character Frequency:", char_count)


86.Dictionary Key Check: Write a Python program that takes a key as input and checks if it exists in a given dictionary. Print “Key Found” if the key is present and “Key Not Found” otherwise.
# Define a sample dictionary
sample_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Take a key as input from the user
key_to_check = input("Enter a key to check: ")

# Check if the key exists in the dictionary
if key_to_check in sample_dict:
    print("Key Found")
else:
    print("Key Not Found")




