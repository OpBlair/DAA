# 1. Initialization
my_array = [10, 20, 30, 40, 50]
print(f"Array: {my_array}")

# 2. Accessing by Index (Random Access)
# The index starts at 0
element_at_index_2 = my_array[2] 
print(f"Element at index 2: {element_at_index_2}") # Output: 30

# 3. Updating an Element
my_array[4] = 99
print(f"Array after update: {my_array}") # Output: [10, 20, 30, 40, 99]

# 4. Insertion (Dynamic Array Operation)
# This adds the element to the end of the Python list (O(1) amortized)
my_array.append(100)
print(f"Array after appending 100: {my_array}") # Output: [10, 20, 30, 40, 99, 100]

# 5. Deletion (Dynamic Array Operation)
# This removes the element at the specified index (O(n))
del my_array[0]
print(f"Array after deleting index 0: {my_array}") # Output: [20, 30, 40, 99, 100]
