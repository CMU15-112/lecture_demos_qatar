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
    
class Berserker(Monster):
    
    def __init__(self, name, hitPoints, attackPoints, frequency):
        super().__init__("Berserker " + name, hitPoints, attackPoints)
        self.frequency = frequency
        self.attacks = 0
        
    def attack(self, otherMonster):
        dmg = random.randint(0, self.ap)
        
        if self.attacks % self.frequency == (self.frequency-1):
            print(f"{self.name} is going berserk!")
            dmg = 2 * dmg
            
        print(f"{self.name} is attacking {otherMonster.name} with {dmg} damage")
        
        otherMonster.defend(dmg)
        
        self.attacks += 1
        
class Deflector(Monster):
    
    def __init__(self, name, hitPoints, attackPoints):
        super().__init__("Deflector "+name, hitPoints, attackPoints)
        self.defenses = 0
        
    def defend(self, dmg):
        if self.defenses < 3:
            print(f"{self.name} deflected the attack!")
            self.defenses += 1
        else:
            super().defend(dmg)

class Knight(Monster):
    def __init__(self, name, hitPoints, attackPoints):
        super().__init__("Knight "+ name, hitPoints, attackPoints)
        
    def defend(self, attackPoints):
        num = random.randint(1,100)
        if num <= 25:
            print(f"{self.name} defends against the attack!")
        else:
            super().defend(attackPoints)

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
    

m1 = Deflector("Bob", 20, 5)
m2 = Berserker("Fred", 30, 3, 4)
MonsterBattle(m1, m2)