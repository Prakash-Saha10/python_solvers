87.Access Nested Dictionary: Given a nested dictionary containing student details, write a Python program to access and print specific information such as a student’s name, age, and address.

students = {
    "student1": {"name": "Alice", "age": 22, "address": "New York"},
    "student2": {"name": "Bob", "age": 24, "address": "London"},
    "student3": {"name": "Charlie", "age": 21, "address": "Sydney"}
}
student_id = input("Enter student ID (e.g., student1, student2, student3): ")

if student_id in students:
    print(f"Name: {students[student_id]['name']}")
    print(f"Age: {students[student_id]['age']}")
    print(f"Address: {students[student_id]['address']}")
else:
    print("Student ID not found.")


88.Nested Dictionary Length: Write a Python program to calculate and print the total number of key-value pairs in a nested dictionary.
def count_nested_dict_pairs(d):
    count = 0
    for key, value in d.items():
        count += 1  # Count the current key-value pair
        if isinstance(value, dict):  # If value is a dictionary, count its pairs recursively
            count += count_nested_dict_pairs(value)
    return count

nested_dict = {
    "person": {"name": "Alice", "age": 25},
    "address": {"city": "New York", "zip": "10001"},
    "contact": {"email": "alice@example.com", "phone": {"home": "1234567890", "work": "0987654321"}}
}

print(count_nested_dict_pairs(nested_dict))

89. Nested Dictionary Update: Given a nested dictionary of employee details, write a Python program to update an employee’s salary based on their employee ID

def update_salary(employee_dict, emp_id, new_salary):
    if emp_id in employee_dict:
        employee_dict[emp_id]["salary"] = new_salary
        print(f"Updated salary for Employee ID {emp_id}: {new_salary}")
    else:
        print(f"Employee ID {emp_id} not found.")
employees = {
    "E101": {"name": "Alice", "age": 30, "salary": 50000},
    "E102": {"name": "Bob", "age": 25, "salary": 45000},
    "E103": {"name": "Charlie", "age": 28, "salary": 48000}
}

update_salary(employees, "E102", 52000)
print(employees)

90. Nested Dictionary Sorting: Given a nested dictionary containing product details (product name, price, and quantity), write a Python program to sort the products based on their prices in ascending order.
def sort_products_by_price(products):
    sorted_products = dict(sorted(products.items(), key=lambda item: item[1]["price"]))
    return sorted_products
products = {
    "P101": {"name": "Laptop", "price": 800, "quantity": 5},
    "P102": {"name": "Phone", "price": 500, "quantity": 10},
    "P103": {"name": "Tablet", "price": 300, "quantity": 7}
}
sorted_products = sort_products_by_price(products)
print(sorted_products)


91.Nested Dictionary Key Search: Write a Python program that takes a key as input and searches for it in a nested dictionary. If found, print the corresponding value, otherwise, print “Key Not Found.”

Define a recursive function to search for a key in a nested dictionary
def search_key(nested_dict, target_key):
    # Iterate through the key-value pairs in the dictionary
    for key, value in nested_dict.items():
        # If the current key matches the target key, return its value
        if key == target_key:
            return value
        # If the value is another dictionary, search inside it recursively
        elif isinstance(value, dict):
            result = search_key(value, target_key)  # Recursive call
            # If the result is found in the nested dictionary, return it
            if result is not None:
                return result
    # If the key is not found in any level, return None
    return None


# Define a nested dictionary with product details
data = {
    'product1': {'name': 'Laptop', 'price': 800, 'details': {'brand': 'Dell', 'warranty': '1 year'}},
    'product2': {'name': 'Phone', 'price': 500, 'details': {'brand': 'Samsung', 'warranty': '2 years'}},
}

# Ask the user to input the key they want to search for
key_to_search = input("Enter the key to search: ")

# Call the search_key function and store the result
value = search_key(data, key_to_search)

# If a value was found, print it
if value is not None:
    print(f"Value found: {value}")
# If no value was found, inform the user
else:
    print("Key Not Found.")