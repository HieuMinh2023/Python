#Binary to Decimal
#binary = input("Please enter a binary number: ")
binary = '1111'
length = (len(binary))-1
answer = 0

#using for loop
for position in range(length,-1,-1):
    #get the digit at the position 
    digit = int(binary[position])
    #add up to the final sum
    answer = digit * 2**(length-position) + answer
    

print(answer)
