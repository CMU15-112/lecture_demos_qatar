import random

class Monster(object):
    def __init__(self, name, hitPoints=10, attackPoints=10):
        self.name = name
        self.hp = hitPoints
        self.ap = attackPoints
        
    def attack(self, otherMonster):
        dmg = random.randint(0, self.ap)
        print(f"{self.name} is attacking {otherMonster.name} with {dmg} damage")
        otherMonster.defend(dmg)
        
    def defend(self, dmg):
        self.hp -= dmg
        
    def isDead(self):
        return self.hp <= 0
    
class Deflector(Monster):
    def __init__(self, name, hitPoints, attackPoints):
        super().__init__(name+"(Deflector)", hitPoints, attackPoints)
        self.num_attacks = 0
        
    def defend(self, dmg):
        self.num_attacks += 1
        if self.num_attacks%3 == 0:
            print(f"{self.name} deflected the attack")
        else:
            super().defend(dmg)
    
    
def MonsterBattle(monster1, monster2):
    print(f"{monster1.name} is fighting {monster2.name}")
    print("----------------------------------------------")
    
    while not monster1.isDead() and not monster2.isDead():
        print(f"{monster1.name}:{monster1.hp}\t{monster2.name}:{monster2.hp}")
        monster1.attack(monster2)
        input(">")
        
        monster1, monster2 = monster2, monster1
        
    if monster1.isDead():
        print(f"{monster1.name} is dead!")
        
    if monster2.isDead():
        print(f"{monster2.name} is dead!")
        
m1 = Monster("Bob", 20, 5)
m2 = Deflector("Fred", 30, 3)
MonsterBattle(m1, m2)