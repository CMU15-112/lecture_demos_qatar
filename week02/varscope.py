secret = 42

def secretNumber():
    secret = 15112
    return secret

def secretFunction(x):
    doubleSecret = secretNumber() * 2
    print("doubleSecret inside secretFunction", doubleSecret)
    x += doubleSecret
    return x


newnumber = secretFunction(1)
# doubleSecret is gone

print("newNumber = ", newnumber) # 85
print("secret = ",secret) #42
#print("doubleSecret = ", doubleSecret)  # It is local! no longer available when secretFunction returns
