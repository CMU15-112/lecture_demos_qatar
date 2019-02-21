import copy
a = [5,10,15,20,25,30,35,40,45]

# Must iterate through copy of list because I want to modify the list inside
# the loop.
for i in copy.copy(a):
    if i%5 == 0:
        a.remove(i)
        
print(a)