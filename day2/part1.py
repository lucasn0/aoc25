inputRaw = open("input1.txt", encoding="utf-8")
input = inputRaw.read()

input = input.split(',')
result = 0

# TOPE DE GAMA
def splice(string):
    result = str(string)
    
    if len(result) > 1 and len(result) % 2 == 0:
        if result.count(result[int(len(result)/2):]) >= 2:
            return int(string)
        else: return 0
    else: return 0

for range in input:
    fromNum = int(range.rsplit('-')[0])
    toNum = int(range.rsplit('-')[1])
    
    while fromNum <= toNum:
        result += splice(fromNum)
        fromNum += 1
    




print(input[0].rsplit('-'))

print(splice('99'))

print(result)
