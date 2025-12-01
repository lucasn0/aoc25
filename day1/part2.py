inputRaw = open("input1.txt", encoding="utf-8")

input = []
dial = 50
result = 0

for line in inputRaw:
    input.append(line.rstrip())

# NEGRADA ABOSLUTA
#for rotation in input:
#    if 'L' in rotation:
#        dial += int(rotation[1:])
#    else:
#        dial -= int(rotation[1:])
#
#    if dial == 0:
#        result += 1
#    elif dial % 100 == 0:
#        result += 1

# LAS ESTRUCTURAS DE DATOS NO EXISTEN
for rotation in input:
    if 'L' in rotation:
        for num in range(int(rotation[1:])):
            dial -= 1
            if dial % 100 == 0 or dial == 0:
                result += 1
            else: continue
    elif 'R' in rotation:
        for num in range(int(rotation[1:])):
            dial += 1
            if dial % 100 == 0 or dial == 0:
                result += 1
            else: continue

print(result)
