def myFunctionOnLists(L):
    L.append("easy")

L=["aliasing", "is"]
print("L before calling myFunctionOnList", L)
myFunctionOnLists(L)
print("L after calling myFunctionOnList", L)