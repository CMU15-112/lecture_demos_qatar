import random
class Monster():
    def __init__(self,name,h,a):
        self.name = name
        self.health = h
        self.attackS = a
    def isDead(self):
        return self.health <= 0
    def defend(self,attack):
        self.health -= attack
    def attack(self,othermonster):
        power = random.randint(0,self.attackS)
        print (self.name," attacked ",othermonster.name, "with ",power)
        othermonster.defend(power)
        
    def __str__(self):
        result = "name: "+self.name
        result += " health: "+str(self.health)
        return result
class uberMonster(Monster):
    def __init__(self,name,hl, a,insurance):
        super().__init__(name,hl,a)
        self.insurance = insurance
    def defend(self,attack):
        df = random.randint(1,100)
        if df <= 25:
            print (self.name," defended itself")
        else:
            super().defend(attack)
    


        
m1 = uberMonster("CMU",100,5,"HMC")
m2 = Monster("COVID-19",110,4)
while ((not m1.isDead()) and (not m2.isDead())):
    m1.attack(m2)
    temp = m1
    m1 = m2
    m2 = temp
print(m1)
print(m2)


#m1.attack(m2)

#print(m1)
#print(m2)







        
