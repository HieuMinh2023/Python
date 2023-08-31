n = int(input())

for row in range(1,n+1):
    for col in range(1,row+1):
        print('*', end='')

    print()

print()

#Upside down
for row in range(n, 0, -1):
    for col in range(row, 0,-1):
        print('*',end='')  
    print()

print()

for row in range(1,n+1):
    #displaying the spaces
    for col in range(n-row,0,-1):
         print(' ',end='')
    
    #displaying the stars
    for col in range(1,row+1):
        print('*', end='')

    print()

print()

#The one we're working on
for row in range(n,0,-1):
    for col in range(0,n-row,+1):
        print(' ', end='')
    for col in range(row, 0, -1):
        print('*', end='')
    
    print()

print()

for row in range(1,n+1,):
    for col in range(n-row,-1,-1):
        print(' ', end='')

    for col in range(1,row*2,1):
        print('*', end='')
    
    print()

print()

for row in range(1,n+1,):
    for col in range(n-row,0,-1):
        print('$', end='')

    for col in range(1,row*2,1):
        print('*', end='')
    
    for col in range(n-row,0,-1):
        print('$', end='')

    print()

print()       

text = ''

for row in range(1,n+1):
    for col in range(n-row,0,-1):
        print(' ', end='')   

    for col in range(row*2-1, 0 ,-1):
        if row == n:
            text = '*'
        else:
            if col == 2*row-1 or col == 1:
                text = '*'
            
            else:
                text = ' '
        
        print(text, end='')

    print()
