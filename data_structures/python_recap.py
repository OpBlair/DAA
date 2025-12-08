#List Comprehension
arr = [3, 1, 4, 1, 5, 9]
arr2 = [x*x for x in arr if x % 2 == 0]
print(f"Original array: {arr}")
print(f"Updated array: {arr2}")

