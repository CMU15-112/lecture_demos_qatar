def ct2(n):
    def f(n):
        r,m = 0,n
        while m>0:
            r,m = r+m,m-1
        return 2*r-n
    def g(n):
        return (f(n+1) - f(n-1))
    
    #n = n*2
    #return n
    
    return f(g(n))

print(ct2(3)) 