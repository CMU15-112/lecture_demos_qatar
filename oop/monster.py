"""Game: "Monster battle"

- A monster is a character of the game that can attack other monsters.

- A monster has a name, health, and strength

- The health of a monster is defined by a number of points

- When a monster attacks another monster, it hits it with a number of points
  randomly chosen between 0 and its strength

- When a monster defends itself from another monster, it receives a "damage"
  equal to the number of points that the attacker uses for the attack. The
  health is decreased by the number of points of the damage.

- An example

   - Monsters A, B, all healthy (health=100)
   - A has strength 25, and B has strength 20
   - A decides to attack B, so the hit points chosen randomly are 10 points
   - B defends, and receives a damage of 10 points, so its health now becomes 90

Special characters:

   A Berserker is a monster that, with certain frequency, it enter in a
   trance-like state of blind rage that makes his attack twice as powerful.

   A deflector is a monster that fully negates the first 3 attackes that it
   receives

"""

""" How to represent a monster?  -> name, health, strength
    Let's use a tuple (name, h, s)
    A = ("monsterA", 100, 25)
    B = ("monsterB", 100, 20)

    # now the attack
    import random
    hitpoints = random.randint(0, 25)
    B[1] -= hitpoints
    if B[1] < 0:
       print("%s is dead" % B[0])

    print("health of %s = %d", A[0], A[1])
    print("health of %s = %d", B[0], B[1])

    Let's use a function
    def attack(x, y):
        hitpoints = random.randint(0, x[2])
        y[1] -= hitpoints
        if y[1] < 0:
           print("%s is dead" % y[0])

     attack(A, B)
"""
