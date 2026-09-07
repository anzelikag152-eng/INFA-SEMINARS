a = open('input.txt', 'r')
numbers = list(map(int, a.readline().split()))
operation = a.readline().strip()
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
