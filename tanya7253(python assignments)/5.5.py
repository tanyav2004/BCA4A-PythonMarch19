# Creating a list
my_list = [1, 2, 3, 4, 5]

# Append function
my_list.append(6)
print("After append:", my_list)

# Extend function
my_list.extend([7, 8, 9])
print("After extend:", my_list)

# Insert function
my_list.insert(2, 10)
print("After insert:", my_list)

# Remove function
my_list.remove(3)
print("After remove:", my_list)

# Pop function
popped_element = my_list.pop()
print("Popped element:", popped_element)
print("After pop:", my_list)

# Index function
index_of_4 = my_list.index(4)
print("Index of 4:", index_of_4)

# Count function
count_of_2 = my_list.count(2)
print("Count of 2:", count_of_2)

# Sort function
my_list.sort()
print("After sort:", my_list)

# Reverse function
my_list.reverse()
print("After reverse:", my_list)

# Copy function
copied_list = my_list.copy()
print("Copied list:", copied_list)

# Clear function
my_list.clear()
print("After clear:", my_list)
