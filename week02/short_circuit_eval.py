def alwaysTrue():
    return True

def alwaysFalse():
    return False

def alwaysCrash():
    x = 5 / 0
    
print(alwaysTrue() and alwaysFalse() and alwaysCrash())

print(alwaysTrue() or alwaysCrash())