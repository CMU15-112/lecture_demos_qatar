import time
import ray

ray.init()

@ray.remote
def f(i):
    time.sleep(1)
    return i

t1= time.time()

results=[]
for i in range(4):
        results.append(f.remote(i))


print("DOING SOMETHING ELSE")
print(" curr time before par exec done: ", time.time()- t1)

ans= ray.get(results)
print("results: ", ans)
print("sequential time: ", time.time()-t1)
