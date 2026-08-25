def alwaysTrue():
    return True

def alwaysFalse():
    return False

def alwaysCrashes():
    x = 5 / 0

print(alwaysTrue() or alwaysCrashes())

print(alwaysFalse() and alwaysCrashes())

#print(alwaysCrashes() or alwaysTrue())

