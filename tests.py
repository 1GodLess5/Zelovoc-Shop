lst = ["pepa", "banán", "banán", 4, 5, 2, 2, "pepa", 5, "pomelo", 5, 5, 6]

count = {}

for item in lst:
    count[item] = lst.count(item)

print(count)