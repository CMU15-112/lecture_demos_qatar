def permutations(L):
    if len(L) == 0:
        return [[]]
    else:
        ret = [ ]
        for i in range(len(L)):
            item = L[i]
            others = L[:i]+L[i+1:]
            
            # Get the permutations of the others
            perms = permutations(others)
            for subPerm in perms:
                # For each subpermutation, put item
                # in the front of it and add it to our answer
                onePerm = [item]+subPerm
                ret.append(onePerm)
        return ret
            
print(permutations([1,2,3]))