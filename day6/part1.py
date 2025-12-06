inputRaw = open("input1.txt", encoding="utf-8")

input = []
result = 0
sumas = 0
mul = []


for line in inputRaw:
    input.append((' '.join(line.split())).split(' '))


for x in range(len(input[0])):
    list = []
    for y in range(len(input)):
        list.append(input[y][x])

    j = len(list)-2
    operation = list[j+1]
    m = 1

    if operation == '+':
        while j >= 0:
            sumas += int(list[j])
            j -= 1
    elif operation == '*':
        while j >= 0:
            m = m * int(list[j])
            j -= 1
        mul.append(m)

print(sumas + sum(mul))