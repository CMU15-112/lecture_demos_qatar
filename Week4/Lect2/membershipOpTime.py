### To get a sense of how fast this operation is compared to lists, look at the following code.
#- here I am creating a list of even numbers from 2 to n
#- then iterating over all numbers from 1 to n checking membership...
#- I measure the elapsed time.. so I take the time before and after doing this ...


# 0. Preliminaries
import time
n = 50000

# 1. Create a list [2,4,6,...,n] then check for membership
# among [1,2,3,...,n] in that list.

# don't count the list creation in the timing
a = list(range(2,n+1,2))

print("Using a list... ", end="")
start = time.time()
count = 0
for x in range(n+1):
    if x in a:
        count += 1
end = time.time()
elapsed1 = end - start
print(f'count={count} and time = {elapsed1:0.5f} seconds')







import time
n = 50000

# 2. Repeat, using a set
print("Using a set.... ", end="")
start = time.time()
s = set(a) # we are counting the set creation time
count = 0
for x in range(n+1):
    if x in s:
        count += 1
end = time.time()
elapsed2 = end - start
print(f'count={count} and time = {elapsed2:0.5f} seconds')


print(f'At n={n}, sets ran ~{elapsed1/elapsed2:0.1f} times faster than lists!')
print("Try a larger n to see an even greater savings!")