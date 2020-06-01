a = [ 2, 3 ]
b = a  #this is an ALIAS

# This is destructive
a += [ 4 ]
print(a)
print(b)

# Here we created a new list, the previous one is still there
a = [2,3]
print(a)
print(b)


# we can have lists with mixed elements, including lists
a = [2,3, [4,5,6,7] ]

# what is the length?
print(len(a))


# note the difference between append and extend
a = [2,3]
a.append( [4,5,6,7] )
print(a)

a = [2,3]
a.extend( [4,5,6,7] )
print(a)
