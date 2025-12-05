inputRaw = open("input1.txt", encoding="utf-8")

input = []
result = 0
ranges = []
ingredients = []
fresh = []

for line in inputRaw:
    input.append(line.rstrip())

for line in input:
    if '-' in line:
        ranges.append(line)
    else:
        ingredients.append(line)

for elem in ranges:
    string = elem.split('-')
    first = int(string[0])
    last = int(string[1])

    while first <= last:
        fresh.append(str(first))
        first += 1

for elem in ingredients:
    if elem in fresh:
        result += 1

print(result)