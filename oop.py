class Bird():
    def __init__(self,spName):
        self.name = spName
        self.eggCount = 0
    def fly(self):
        return "I can fly!"
    def countEggs(self):
        return self.eggCount
    def layEgg(self):
        self.eggCount += 1
    def __str__(self):
        if self.countEggs() == 1:
            return self.name+" has "+str(self.countEggs())+" egg"
        return self.name+" has "+str(self.countEggs())+" eggs"
    
class Penguin(Bird):
    def fly(self):
        return "No flying for me."
    def swim(self):
        return "I can swim!"

class MessengerBird(Bird):
    def __init__(self,spName, message=""):
        super().__init__(spName)
        self.message = message
    def deliverMessage(self):
        return self.message




theBird = MessengerBird("something")
print (theBird.countEggs())
print (isinstance(theBird, MessengerBird))
print (isinstance(theBird, Penguin))
print (isinstance(theBird, Bird))
print (theBird.fly())

    
        
def testBirdClasses():
    print("Testing Bird classes...", end="")
    # A basic Bird has a species name, can fly, and can lay eggs
    bird1 = Bird("Parrot")
    assert(type(bird1) == Bird)
    assert(isinstance(bird1, Bird))
    assert(bird1.fly() == "I can fly!")
    assert(bird1.countEggs() == 0)
    assert(str(bird1) == "Parrot has 0 eggs")
    bird1.layEgg()
    assert(bird1.countEggs() == 1)
    assert(str(bird1) == "Parrot has 1 egg")
    bird1.layEgg()
    assert(bird1.countEggs() == 2)
    assert(str(bird1) == "Parrot has 2 eggs")

    print ("Passed all test cases for the Bird Class")

    
    # A Penguin is a Bird that cannot fly, but can swim
    bird2 = Penguin("Emperor Penguin")
    assert(type(bird2) == Penguin)
    assert(isinstance(bird2, Penguin))
    assert(isinstance(bird2, Bird))
    assert(bird2.fly() == "No flying for me.")
    assert(bird2.swim() == "I can swim!")
    bird2.layEgg()
    assert(bird2.countEggs() == 1)
    assert(str(bird2) == "Emperor Penguin has 1 egg")


    print ("Passed all test cases for the Penguin Class")

    
    # A MessengerBird is a Bird that can optionally carry a message
    bird3 = MessengerBird("War Pigeon", message="Top-Secret Message!")
    assert(type(bird3) == MessengerBird)
    assert(isinstance(bird3, MessengerBird))



    assert(isinstance(bird3, Bird))
    assert(not isinstance(bird3, Penguin))
    assert(bird3.deliverMessage() == "Top-Secret Message!")
    assert(str(bird3) == "War Pigeon has 0 eggs")
    assert(bird3.fly() == "I can fly!")

    bird4 = MessengerBird("Homing Pigeon")
    assert(bird4.deliverMessage() == "")
    bird4.layEgg()
    assert(bird4.countEggs() == 1)
    print("Done!")


