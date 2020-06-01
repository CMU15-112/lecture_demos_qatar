def replaceLastWith15112(l):
    # l is an ALIAS of the list that is passed to the function
    # l
    l[-1] = 15112
    # so this changes will be made to the list that is passed to the function

def NDreplaceLastWith15112(l):
    # l is an ALIAS
    # l
    newlist = list(l)  #but newlist is NOT the same l
    # we copied it
    newlist[-1] = 15112
    # and this changes do not affect l
    return newlist


a==[42,99,5,7]

theresult=NDreplaceLastWith15112(a)
print(theresult)  # [42,99,5,15112]
print(a==[42,99,5,7])

replaceLastWith15112(a)
print(a==[42,99,5,7])
