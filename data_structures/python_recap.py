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
for i in range(1, len(arr3)-1):
    if minimum_element <= arr3[i+1]:
        minimum_element = arr3[i]
print(f"Minimum Element in {arr3} is {minimum_element}")

#Recursion
arr4 = [1, 2, 3, 4, 5]
sum = 0
for a in range(len(arr4)-1):
	sum += arr4[a]
print(f"Sum of elements in {arr4} = {sum}")
