### Creating a set
print("Creating A Set ============ ")
# from list
L= ['hello', 'world', 'hello', '15-112']
s1 = set(L) #silently removes duplicates
print(s1)

# from string
s= "Hello"
s2= set(s) # ignore duplicates
print(s2)

# empty set
s3 = set()
print(s3) #{} is dict
print(list())
print(type({}))


# statically allocated set
s4 = {1, 2, 3, 'A', 'D', 3}
print(s4)

### set elements are unordered
print("\nSet Properties ============ ")
L1 = [1,2,3,4]
L2= [1,3,2,4]
print(L1==L2)

s4 = set(L1)
s5 = set(L2)
print(s4==s5)

### set elements are immutable (primitive, tuples, strings)
s3 = {2,3,'A', 4.2, True, 0, False} #, [1,2]}
print(s3)
print(hash("Hello"))

### Iterarting over elements & Membership
print("\nIterating Over Elements & Membership ============ ")
for v in s3:
    print(v)
    
print(1 in s3)
print(5 not in s3)

### Adding Elements
print("\nAdding Elements ============ ")

# single element
s3.add(10)
print(s3)

# multiple elements from iterable data type (e.g. list, string, tuple, set)
s3.update([20, 30, 40])
print(s3)

### Removing elements
print("\nRemoving elements ============ ")
s3.remove(1)
print(s3)

#s3.remove('B')  #crashes

s3.discard('B')

s3.clear()
print(s3)

##### Math Set Theory Operations, e.g.
print("\nSet Theory Ops: Example Use Cases ============ ")


# Remove blacklisted IP addresses
allIPs = {'192.168.1.1', '192.168.1.2', '192.168.1.3', '10.0.0.1'}
blacklistedIPs = {'192.168.1.2', '10.0.0.1'}
allowedIPs = allIPs - blacklistedIPs
print(allowedIPs)

# Combine skills from multiple team members
aliceSkills = {'Python', 'SQL', 'Docker'}
bobSkills = {'Java', 'SQL', 'AWS'}
teamSkills = aliceSkills | bobSkills
print(teamSkills)

#Find Mutual Friends
pythonaliceFriends = {'Bob', 'Charlie', 'Diana', 'Eve'}
bobFriends = {'Alice', 'Charlie', 'Frank', 'Diana'}
print(pythonaliceFriends & bobFriends)

# Scheduling - Find bad meeting times to avoid them
aliceAvailable = {'9am', '10am', '11am', '2pm'}
bobAvailable = {'10am', '11am', '3pm', '4pm'}
badTimes = aliceAvailable ^ bobAvailable
print(badTimes)
