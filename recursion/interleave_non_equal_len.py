# assume that always len(list1) == len(list2)
# a return list
# assert(interleave([1,2,3], [4,5,6]) == [1,4,2,5,3,6])
# recursion => short code, "elegant" solutions, compact
def interleave(list1, list2):
    print("list1 ", list1, " list2 ", list2)
    if len(list1) == 0 and len(list2) == 0:  # one base case
        return []
    if len(list1) == 0 and len(list2) >= 1:  #another base case
        return list2
    if len(list2) == 0 and len(list1) >= 1:  # third base case
        return list1
    
    result = [list1[0]] + [list2[0]] + interleave(list1[1:], list2[1:])
    print("returning ", result)
    return result


print(interleave([1,2,3],[4,5,6,7]))