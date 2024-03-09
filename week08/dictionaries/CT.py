def ct2(d, key): 
    while (key in d) and ((key+2) not in d): 
        d[key+2] = key+1 
        key = d[key]
    print(d)
    L = [ ] 
    for key in sorted(d.keys()): 
        L.append(10*key + d[key]) 
    return L 

print(ct2({1:5, 0:2}, 0)) 