def alwaysTrue():
    return True

def alwaysFalse():
    return False

def alwaysCrash():
    x = 5 / 0
    return True
    
#print(alwaysTrue())
#print(alwaysFalse())
#print(alwaysCrash())

## This crashes
#if alwaysTrue() and alwaysCrash():
#    print("First statement is true")
#else:
#    print("First statement is false")
    
if alwaysFalse() and alwaysCrash():
    print("Second statement is true")
else:
    print("Second statement is false")
    
# Why is this useful? You can use this for error checking
a = 0
b = 7
if a != 0 and b // a == 2:
    print("The division of b by a is 2")
else:
    print("The division of b by a is not 2")