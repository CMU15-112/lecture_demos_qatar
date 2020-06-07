import random
A = ["monsterA", 100, 25]
B = ["monsterB", 100, 20]

#Let's use a function
def attack(x, y):
    hitpoints = random.randint(0, x[2])
    y[1] -= hitpoints
    if y[1] < 0:
        print("%s is dead" % y[0])

attack(A, B)


print("health of %s = %d" %( A[0], A[1]))
print("health of %s = %d" %( B[0], B[1]))
