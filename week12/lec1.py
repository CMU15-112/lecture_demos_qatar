L1 = [47, 5, 6, 99, 48, 37, 20, 74, 19]

if 49 in L1: # "in" is always O(N)
    print("49 is there!")
else:
    print("49 is not there.")
    
L2 = [5, 6, 19, 20, 37, 47, 48, 74, 99]

if 49 in L2: # This is still O(N)
    print("49 is there!")
else:
    print("49 is not there.")    