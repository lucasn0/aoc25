inputRaw = open("input1.txt", encoding="utf-8")

input = []
result = 0

for line in inputRaw:
    input.append(line.rstrip())

# JOHN CARMACK HIMSELF WROTE THIS:

def biggestTwelveDigits(string):
    battery = list(string)
    result = []
    currentInd = 0

    for x in range(12):
        current = int(battery[0])
        currentInd = 0
        lenBat = 0

        # CODE SNIPPET FROM NASA SPACE SHUTTLE COMPUTER:
        for num in battery:
            if int(num) > current and lenBat < len(battery) - (11 - x):
                current = int(num)
                currentInd = battery.index(str(current))
            print(currentInd)
            lenBat += 1
        result.append(str(current))
        print(result)
        for j in range(currentInd+1):

            battery.pop(0)
            print(result)


        print(battery)
    
    return ''.join(result)

for line in input:
    result += int(biggestTwelveDigits(line))

print(result)