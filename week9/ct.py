def ct(L):                                                     
    s = set()                                                       
    d = dict()                                                      
    for v in L:                                                     
        s.add(v)                                                    
        if (v in d):                                                
            d[v] += len(s)                                          
        else:                                                       
            d[v] = v                                                
    print("s = ",s)                                                 
    print("d = ",d)                                                 
                                                                    
ct([1,2,1,1,5,2])  