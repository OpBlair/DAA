#List Comprehension
arr = [3, 1, 4, 1, 5, 9]
arr2 = [x*x for x in arr if x % 2 == 0]
print(f"Original array: {arr}")
print(f"Updated array: {arr2}")

#Dictionary counting
s = "abracadabra"
word_count = {}
for c in s:
    if c in word_count:
        word_count[c] += 1
    else:
        word_count[c] = 1
print(word_count)

#Minimum element
arr3 = [2,3,5,6,1,10]
minimum_element = arr3[0]
for x in arr3:
    if x < minimum_element:
        minimum_element = x
print(f"Minimum Element in {arr3} is {minimum_element}")

#Recursion
def recursive_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + recursive_sum(arr[1:])

arr4 = [1, 2, 3, 4, 5]
print(f"Sum of elements in {arr4} = {recursive_sum(arr4)}")

#Stable partition
arr5 = [3, -1, 4, -2, 5]
positives = [x for x in arr5 if x > 0]
negatives = [x for x in arr5 if x < 0]
partitioned = positives + negatives
print(partitioned)
