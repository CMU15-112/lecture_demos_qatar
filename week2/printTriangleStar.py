def printTriangleStar(n):
    for row in range(n): # n times
        print(row, end='')
        for col in range(row): # row times
            print('*', end = '')
        print('')
            
        
printTriangleStar(5)