def printMystery(n):
    for row in range(n):
        print(row, end=" ")
        for col in range(row):
            print("*", end=" ")
        print()

printMystery(5)
