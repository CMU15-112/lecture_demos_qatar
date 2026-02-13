# foo(x) is used by ct1 
def foo(x): 
    x + 1 
    return x- 1 
def ct1(x): 
    print(x + 3) 
    y=foo(x%2 + foo(12)) 
    print("y:",y) 
    
x=8 
print("study") 
print(ct1(x))