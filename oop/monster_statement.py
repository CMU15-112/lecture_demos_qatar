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
