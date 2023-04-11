def myhash(s):
    total = 1
    for c in s:
        total += ord(c)   
    return total


print(myhash("example"))
print(myhash("15-112"))
print(myhash("Hello"))
print(myhash("World"))

print(hash("example")%10)
print(hash("15-112")%10)
print(hash("Hello")%10)
print(hash("World")%10)

# our hash is not good for anagrams
L = ['enlist','inlets','listen','silent','tinsel']
for s in L:
    print(f'{s} -> {myhash(s)}')
    
    
L = ['enlist','inlets','listen','silent','tinsel']
for s in L:
    print(f'{s} -> {hash(s)%10}')


        
    