def interleave(A, B, depth = 0):
    print(" "*depth, f"hello {A} {B}")
    if len(A) == 0 and len(B) == 0:
        return []
    elif len(A) == 0:
        return B
    elif len(B) == 0:
        return A
    return [ A[0], B[0] ] + interleave(A[1:], B[1:], depth+1)

interleave([1,2,3], [4,5])
