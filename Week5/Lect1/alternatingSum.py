#Given a list of integers, calculate the alternating sum...
#[1, 2, 3, 4] => 1 - 2 + 3 - 4 == 1 + -2 + 3 + -4


def alternatingSum(l):
    r = 0
    for i in range(len(l)):
        if i%2 == 0:
            r += l[i]
        else:
            r-=l[i]
        
    return r

def alternatingSum_v2(l):
    r = 0
    for i in range(len(l)):
        r+= l[i] * (-1)**i
        
    return r

def alternatingSum_v3(l):
    return sum(l[::2]) - sum(l[1::2])

print(alternatingSum_v2([1,2,3,4]))
print(alternatingSum_v3([1,2,3,4]))

