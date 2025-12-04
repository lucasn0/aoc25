inputRaw = open("input1.txt", encoding="utf-8")

input = []
result = 0

for line in inputRaw:
    input.append(line.rstrip())

# TERRY DAVIS ONCE SAID:
def checkAdjacent(input, x, y):
    # top, topR, right, bottomR, bottom, bottomL, left, topL
    coords = [(x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1)]
    paper = 0
    xLen = len(input[0])
    yLen = len(input)

    for coord in coords:
        if coord[0] < xLen and coord[1] < yLen and coord[0] != -1 and coord[1] != -1 and input[coord[0]][coord[1]] == '@':
            paper += 1
        else: continue

    return paper

x = 0
for line in input:
    y = 0
    for elem in line:
        if elem == '@' and checkAdjacent(input, x, y) < 4:
            result += 1
        y += 1
    x += 1

print(result)