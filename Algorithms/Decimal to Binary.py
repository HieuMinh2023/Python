number = int(input("Please enter a decimal number: "))
print(number)
quotient = number
value = 10
remaider = 0
answer = ''

while quotient != 0:
    remaider = str(quotient%2)
    quotient = quotient // 2
    answer = remaider + answer

print(answer)
