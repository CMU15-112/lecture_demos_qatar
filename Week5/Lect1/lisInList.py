'''
Write the function destructiveListInList(a, b, n) which destructively modifies a
(without modifying b) by adding all the values of b between elements
a[n-1] and a[n] and returns the usual value returned by destructive functions.

When n == 0, it adds all values of b onto the front of a.
You may assume 0 <= n <= len(a).
When n == len(a), it adds all values of b at the back of a
(the function behaves like a.extend(b)).
'''
def destructiveListInList(a, b, n):
    
    # case 1-  n = 0:
    if n == 0:
        a[:] = b + a
    
   pass
        

a= [1,3,5]
b= [4,2]
print(a)
destructiveListInList(a,b, 1)
print(a)