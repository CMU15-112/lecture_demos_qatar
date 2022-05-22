for i in range(1, 20):
    if i%2 == 0:
        continue
    if i%7 == 0:
        break
    print(i, end=" ")
    
print("bye")
