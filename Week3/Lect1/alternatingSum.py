#Given a list of integers, calculate the alternating sum...
#[1, 2, 3, 4] => 1 - 2 + 3 - 4 == 1 + -2 + 3 + -4


def alternatingSum(l):
    
    res= 0
    for i in range(len(l)):
        if i%2==0:
            res+=l[i]
        else:
            res-=l[i]
    return res


def alternatingSumV2(l):
    
    evenSum= sum(l[::2]) 
    oddSum= sum(l[1::2])
     
    return evenSum-oddSum


def altenratingSumV3(l):
    s= 1
    res=0
    for e in l:
        res+= (s*e)
        s*=(-1)
        
    return res



print(alternatingSum([1,2,3,4]))
print(alternatingSumV2([1,2,3,4]))
print(altenratingSumV3([1,2,3,4]))
