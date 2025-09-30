def destructiveRemoveNonInts(L):
    for e in L[:]:
        print(f'Checking {e} {type(e)}')
        if not isinstance(e, int):
            print(f'Removing {e}')
            L.remove(e)
        else:
            print(f"I'm not Removing {e}")
    
L = [112, '15', 4, 2, 'hey',  15.112]
assert(destructiveRemoveNonInts(L) == None)
assert(L == [112, 4, 2])
print(":-)")