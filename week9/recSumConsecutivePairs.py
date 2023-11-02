def recSumConsecutivePairs(L):
    if len(L) < 2:   return [] else [L[0]+L[1]] + recSumConsecutivePairs(L[1:])
