lst = [ 1, 2, "a" ]
lstA = lst  # create an alias

lst.append("b") # adds the element to the end of the list
lst.insert(1, "foo") # inserts the 2nd parameter into the 1st index
lst.remove("a") # removes the given element from the list once
lst.pop(0) # removes the element at the given index from the list

print("lstA: ", lstA)
print("lst:", lst)