# O(N^2)
# N=length of lst
def func6(lst):
    result = True # O( 1 )
    for i in range(len(lst)): # Runs  O(N) 
        for j in range(i+1, len(lst)): #O(N)  not constant, N-1, N-2, ..., 1,0
            if lst[i] == lst[j]: #   O(1)
                result = False # O(1)
    return result # O(1)



def func7(lst):
    result = True # O( 1 )
    for i in range(len(lst)): # Runs  O(N) 
        for j in range(len(lst)-1, len(lst)): # O(1) (constant number of passes)  
            if lst[i] == lst[j]: # 
                result = False # 
    return result #