inputRaw = open("input1.txt", encoding="utf-8")
input = inputRaw.read()

input = input.split(',')
final = 0

# TOPISIMO DE GAMA
# O(n^99999)
def splice(string):
    start = 10
    
    while start >= 1:
        print(start)
        result = str(string)
        nums = []
        
        if start > len(result) // 2 or len(result) % start != 0:
            start -= 1
            continue

        for k in range(len(result) // start):
            nums.append(result[:start])
            result = result[start:]
            
        print(nums)

        if len(nums) > 0 and nums.count(nums[0]) == len(nums):
            return string
        
        start -= 1
    return 0

for ranges in input:
    print(ranges)
    fromNum = int(ranges.rsplit('-')[0])
    toNum = int(ranges.rsplit('-')[1])
    
    while fromNum <= toNum:
        final += splice(fromNum)
        fromNum += 1

print(final)
