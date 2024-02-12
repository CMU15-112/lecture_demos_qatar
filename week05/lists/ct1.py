def ct1():
    alist = [4, 2, 8, 6, 5]
    blist = alist
    blist[3] = 999
    print(blist)
    print(alist)    
    
print(ct1())