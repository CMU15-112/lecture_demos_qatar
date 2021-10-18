""" Assuming len(list1) == len(list2)
    Exercise:
    change the function to consider the case len(list1) != len(list2)
"""
def interleave(list1, list2):
    if len(list1) == 0:
        return []
    return [list1[0]] + [list2[0]] + interleave(list1[1:], list2[1:])
    
    
    
 

print(interleave([1,2,3],[4,5,6])) # [1,4,2,5,3,6]

"""
    interleave([1,2,3],[4,5,6]) = [1, 4 ] + interleave( [2,3], [5,6])
                                                  [2,5] + interlave([3], [6])
                                                               [3,6]  + interleave([], [])
                                                                              []
"""