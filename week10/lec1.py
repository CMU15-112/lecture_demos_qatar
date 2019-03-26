# Should be O(N)
def merge(lst1, lst2):
    retList = []
    i = 0
    j = 0
    while i < len(lst1) or j < len(lst2):
        if i == len(lst1):
            retList.append(lst2[j])
            j += 1
        elif j == len(lst2):
            retList.append(lst1[i])
            i += 1           
        elif lst1[i] < lst2[j]:
            retList.append(lst1[i])
            i += 1
        else:
            retList.append(lst2[j])
            j += 1

    return retList

def merge(lst1, lst2):
    retList = []
    while len(lst1) > 0 or len(lst2) > 0:
        if len(lst1) == 0:
            retList.append(lst2[-1])
            lst2.pop()
        elif len(lst2) == 0:
            retList.append(lst1[-1])
            lst1.pop()           
        elif lst1[-1] > lst2[-1]:
            retList.append(lst1[-1])
            lst1.pop()
        else:
            retList.append(lst2[-1])
            lst2.pop()
    retList.reverse()
    return retList

def mergeSort(lst):
    if len(lst) == 1:
        return lst
    else:
        leftHalf = mergeSort(lst[:len(lst)//2])
        rightHalf = mergeSort(lst[len(lst)//2:])
        return merge(leftHalf, rightHalf)
        
print(mergeSort([3,1,9,2,7,8,4,10]))