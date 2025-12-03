inputRaw = open("input1.txt", encoding="utf-8")

input = []
result = 0

for line in inputRaw:
    input.append(line.rstrip())

# JOHN CARMACK HIMSELF WROTE THIS:
def biggest(string):
    battery = string
    batteryList = list(battery)
    bigF = 0
    bigS = 0

    for bat in battery:
        if int(bat) > bigF and int(battery.find(bat))+1 != len(battery):
            bigF = int(bat)
    for j in range(batteryList.index(str(bigF))+1):
        batteryList.pop(0)
    battery = ''.join(batteryList)

    for bat in battery:
        if int(bat) > bigS:
            bigS = int(bat)
    return (str(bigF) + str(bigS))

for line in input:
    result += int(biggest(line))

print(result)