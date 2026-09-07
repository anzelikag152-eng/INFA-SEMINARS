a = open('input.txt', 'r')
numbers = list(map(int, f.readline().split()))
operation = f.readline().strip()
a.close()

result = numbers[0]
for num in numbers[1:]:
    if operation == '+':
        result = result + num
    elif operation == '-':
        result = result - num
    elif operation == '*':
        result = result * num

a = open('output.txt', 'w')
a.write(str(result))
a.close()