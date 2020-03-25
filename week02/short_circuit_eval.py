def alwaysTrue():
    return True

def alwaysFalse():
    return False

def alwaysCrash():
    5 / 0
    return True

print(alwaysTrue() and alwaysFalse() and alwaysTrue() and alwaysCrash())
print(alwaysTrue() or alwaysCrash())