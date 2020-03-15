import random
class bankAccount():
    def __init__(self,name):
        self.Name = name
        self.accn = random.randint(100,1000000)
        self.balance = 0
    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            amount = self.balance
            self.balance = 0
            return amount
    def transfer(self,otheraccount,amount):
        money = self.withdraw(amount)
        if money == amount:
            otheraccount.deposit(money)
        else:
            self.deposit(money)
        
    def __str__(self):
        return "Name: " + self.Name + ", Acc #: "+str(self.accn) + ", $"+str(self.balance)
ba1 = bankAccount("Musab")
ba2 = bankAccount("Jumana")
ba1.deposit(500)
print (ba1)
print (ba1.withdraw(300))
print (ba1)
ba2.deposit(400)
print (ba2.withdraw(500))
print (ba2)
print (ba1,ba2)
ba1.transfer(ba2,150)
print (ba1,ba2)

ba1.transfer(ba2,100)
print (ba1,ba2)














