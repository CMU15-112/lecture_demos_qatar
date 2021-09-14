a = [9, 14, 2021]

b = [9, 14, 2021]


print(a==b)
print(a is b)  # they are not the same list

b = a  # now they refer to the same list  # what happened to the previous a?
print(a==b)
print(a is b)  # 

a[1] = 15
print(a)
print(b)