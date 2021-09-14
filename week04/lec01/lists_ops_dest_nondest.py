l = [15]
# adding

l.append(112)
l += [112]
l = l + [112]

# extending

l.extend([15, 122])
l += [15,122]
l = l + [15,112]

# sorting
sorted(l)
l.sort()

# reverse
l[::-1]
l.reverse()

# remove
l.remove(122)
# non destructive?


