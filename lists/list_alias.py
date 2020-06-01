# Create a list
a = [ 2, 3, 5, 7 ]

type(a) == list
# Create an alias to the list

b = a  # No new list is created


type(b) == list


# We now have two references (aliases) to the SAME list
a[0] = 42

b[1] = 99

print(a)  #[ 42, 3, 5, 7 ]

print(b)  #[ 2, 99, 5, 7 ] WRONG
          #[ 42, 3, 5 7]


# integers (and other primitive types) don't use aliases by default
# that means, that we always copy them using assignment
x=3
y=x
# no aliasing happened here
y=1


print(x) #3
print(y) #1
