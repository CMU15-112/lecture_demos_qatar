#### s.issubset(t)
#test whether every element in s is in t	
print({1,2} <= {1},     {1,2}.issubset({1}))
print({1,2} <= {1,2},   {1,2}.issubset({1,2}))
print({1,2} <= {1,2,3}, {1,2}.issubset({1,2,3}))

#### s.issuperset(t)
#test whether every element in t is in s	
print({1,2} >= {1},     {1,2}.issuperset({1}))
print({1,2} >= {1,2},   {1,2}.issuperset({1,2}))
print({1,2} >= {1,2,3}, {1,2}.issuperset({1,2,3}))

#### s.union(t)
#new set with elements from both s and t	
print({1,2} | {1},     {1,2}.union({1}))
print({1,2} | {1,3},   {1,2}.union({1,3}))
s = {1,2}
t = s | {1,3}
print(s, t)

#### s.intersection(t)
#new set with elements common to s and t	
print({1,2} & {1},     {1,2}.intersection({1}))
print({1,2} & {1,3},   {1,2}.intersection({1,3}))
s = {1,2}
t = s & {1,3}
print(s, t)


#### s.difference(t)
#new set with elements in s but not in t	
print({1,2} - {1},     {1,2}.difference({1}))
print({1,2} - {1,3},   {1,2}.difference({1,3}))
s = {1,2}
t = s - {1,3}
print(s, t)


#### s.update(t)
#modify s adding all elements found in t	
s = {1,2}
t = {1,3}
u = {2,3}
s.update(u)
t |= u
print(s, t, u)

