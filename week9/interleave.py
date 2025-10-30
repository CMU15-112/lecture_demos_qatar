def interleave(list1, list2):
    if len(list1) == 0 and len(list2) == 0:
        return []
    elif len(list1) == 0:
        return list2
    elif len(list2) == 0:
        return list1
        
    return [list1[0]] + [list2[0]] + interleave(list1[1:], list2[1:])

L1=['a','b','c', 'm']
L2=['d','e','f']
print(interleave(L1, L2))