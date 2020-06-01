l=[2,3,5,4,2,4,5,2]

def destructiveRemove2s(l):
    #n=l.count(2)
    for i in range( len(l) ):
        print("i=",i)
        print("l=",l)
        if 2 not in l:
            break
        l.remove(2)
        print("l after ", l)


# one quick way to make a non-destructive version from the destructive version
def nondestructiveRemove2s(l):
    newlist=list(l)
    destructiveRemove2s(newlist)
    return newlist

# better
def nondestructiveRemove2sv2(l):
    newlist=[]
    for item in l:
        if item != 2:
            newlist += [item]
    return newlist


newl = nondestructiveRemove2sv2(l)
print("l: ", l)
print("newl (no 2s): ",newl)
