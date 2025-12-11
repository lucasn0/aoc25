inputRaw = open("input1.txt", encoding="utf-8")

input = []
result = 0
stack = []
current_num = ""

for line in inputRaw:
    input.append(line.strip('\n'))

x = 0
for row in input:
    if len(row) > x:
        x = len(row)
y = len(input)

# una basura este dia
for col in range(x - 1, -1, -1):
    for row in range(y):
        if col < len(input[row]):
            char = input[row][col]
            if char.isdigit():
                current_num += char
            else:
                if current_num:
                    stack.append(int(current_num))
                    current_num = ""
                
                if char == '+':
                    result += sum(stack)
                    stack = []
                elif char == '*':
                    if stack:
                        prod = 1
                        for n in stack:
                            prod *= n
                        result += prod
                        stack = []
    if current_num:
        stack.append(int(current_num))
        current_num = ""

print(result)