#Binary to Decimal
binary = int(input(''))
print('Your binary input is: ',binary)
#binary = 1010011
value = 0
quotient = binary
answer = 0

while quotient != 0:
    remainder = quotient % 10
    
    answer = remainder * (2**value) + answer
    
    quotient = quotient // 10

    value = value + 1


print('The associated decimal number is: ',answer)
