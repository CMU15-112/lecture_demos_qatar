def swap(X, i, j):
    temp = X[i]
    X[i] = X[j]
    X[j] = temp

    
def reverse(L):
    for i in range(0,len(L)//2):
        swap(L,i,len(L) - 1 - i)

def reverseB(Y):
    R = []
    for i in range(len(Y) - 1,-1 , -1):
        R.append(Y[i])
    return R
    
A = [1,3,4,8,2,5]
#reverse(A)


B = reverseB(A)
print (A)
