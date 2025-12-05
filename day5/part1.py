inputRaw = open("input1.txt", encoding="utf-8")

input = []
result = 0
ranges = []
ingredients = []

for line in inputRaw:
    input.append(line.rstrip())

for line in input:
    if '-' in line:
        ranges.append(line)
    else:
        ingredients.append(line)
ingredients.pop(0)

# Tope de gama
for elem in ingredients:
    for ran in ranges:
        string = ran.split('-')
        first = int(string[0])
        last = int(string[1])
        if int(elem) >= first and int(elem) <= last:
            result += 1
            break

print(result)