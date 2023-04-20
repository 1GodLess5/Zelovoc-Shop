lst = [1, 2, 3, 4, 5, 2, 2, 1, 5, 5, 5, 5, 6]

count = {}

for item in lst:
    count[item] = lst.count(item)

print(count)