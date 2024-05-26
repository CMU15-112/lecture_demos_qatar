def destructiveListInList(a, b, n):    
    if n== len(a):
        a.extend(b)
        
    elif n==0:
        a[:]= b+a
        
    else:
        a[:]= a[:n]+b+a[n:]
        #a[n:n]= b
    
    #print(a)
        

a= [1,3,5]
b= [4,2]
print(a)
destructiveListInList(a,b, 1)
print(a)