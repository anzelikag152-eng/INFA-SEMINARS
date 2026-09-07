a = open('input.txt', 'r')
numbers_str = a.readline().split()
operation = a.readline().strip()
base = int(a.readline())
a.close()


numbers = []
for num_str in numbers_str:
    dec_value = 0
    for digit in num_str:
        dec_value = dec_value * base + int(digit)
    numbers.append(dec_value)

result = numbers[0]
for num in numbers[1:]:
    if operation == '+':
        result = result + num
    elif operation == '-':
        result = result - num
    elif operation == '*':
        result = result * num


if result == 0:
    result_str = '0'
else:
    negative = result < 0
    result = abs(result)
    digits = []
    while result > 0:
        digits.append(str(result % base))
        result = result // base
    digits.reverse()
    result_str = ''.join(digits)
    if negative:
        result_str = '-' + result_str


a = open('output.txt', 'w')
a.write(result_str)
a.close()
