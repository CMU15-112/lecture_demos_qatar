# O( NlogN )
# 
def func5(lst):  
    n = len(lst)  # O(1) because len(L) is O(1)
    result = None # O(1) 
    for i in range(len(lst)): # Runs O(N) times
        num = n #  O(1)
        while num > 0: # Runs O(logN) times
            if lst[i] == num:   # O(1)
                result = lst[i] # O(1)
            num = num // 2 #  O(1)
    return result # O(1)


num=n
num=n/2
num=(n/2)/2 = n/4
num=(n/4)/2 = n/8
num=(n/8)/2 = n/16
--->  num=0 when  log(n) passes, times


