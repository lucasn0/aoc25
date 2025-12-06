inputRaw = open("input1.txt", encoding="utf-8")

input = []
result = 0
ranges = []
top = 0
bottom = 0

for line in inputRaw:
    input.append(line.rstrip())

for line in input:
    if '-' in line:
        ranges.append(line)

# Tope de gama 
# Gracias ToToMa & Crack10Ki
uniqueRanges = []
ranges = [[int(x) for x in r.split('-')] for r in ranges]

while len(ranges) > 0:
    current = ranges.pop(0)
    bottom = current[0]
    top = current[1]

    expanded = True
    while expanded:
        expanded = False
        i = 0
        while i < len(ranges):
            bottom2 = ranges[i][0]
            top2 = ranges[i][1]

            if not (top < bottom2 or bottom > top2):
                bottom = min(bottom, bottom2)
                top = max(top, top2)
                ranges.pop(i)
                expanded = True
            else:
                i += 1

    uniqueRanges.append(f"{bottom}-{top}")

for ran in uniqueRanges:
    r = ran.split('-')
    result += int(r[1]) - int(r[0]) + 1

print(result)