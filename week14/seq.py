import time

def f(i):
    time.sleep(1)
    return i

t1= time.time()

results=[]
for i in range(4):
        results.append(f(i))

print("results: ", results)
print("sequential time: ", time.time()-t1)






