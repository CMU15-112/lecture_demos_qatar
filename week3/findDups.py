def findDuplicates(L):
    Lnodups = []
    for e in L:
        if L.count(e) > 1 and e not in Lnodups:
            Lnodups.append(e)
    return Lnodups