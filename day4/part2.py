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

def inputReplace(input, coords):
    x = 0
    for line in input:
        y = 0
        tempList = list(line)
        for elem in tempList:
            if (x, y) in coords:
                tempList[y] = '.'
            y += 1
        input[x] = ''.join(tempList)
        x += 1
    return input
            
toReplace = []
def counter(input):
    x = 0
    result = 0
    for line in input:
        y = 0
        for elem in line:
            if elem == '@' and checkAdjacent(input, x, y) < 4:
                result += 1
                toReplace.append((x, y))
            y += 1
        x += 1
    return result

# O(n^999999)
# Takes fucking forever.
# There's a way to replace the input element without an additional fuction? There is, but:
# the replacement would have to take effect after the last iteration of counter()...
# which makes me loop through the entire input again anyways. So?
# The inputReplace() loop for every substitution drives this crazy.
for l in range(50):
    result += counter(input)
    inputReplace(input, toReplace)

print(result)