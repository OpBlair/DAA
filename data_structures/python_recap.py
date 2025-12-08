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
