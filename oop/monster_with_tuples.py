A = ["monsterA", 100, 25]
B = ["monsterB", 100, 20]

# now the attack
import random
hitpoints = random.randint(0, 25)
B[1] -= hitpoints
if B[1] < 0:
    print("%s is dead" % B[0])

print("health of %s = %d" %( A[0], A[1]))
print("health of %s = %d" %( B[0], B[1]))
