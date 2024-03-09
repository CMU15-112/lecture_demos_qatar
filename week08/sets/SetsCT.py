def ct1(n): 
    s, t = set(), set() 
    while (n > 0): 
        (d, n) = (n%10, n//10) 
        if (d in t): t.remove(d) 
        elif (d in s): t.add(d) 
        s.add(d) 
    return sorted(t) 

print(ct1(13051231))













def ct2(n):
  s = set()
  for i in range(n):
      s.add(i**2 % n)
  return s

print(ct2(4))










