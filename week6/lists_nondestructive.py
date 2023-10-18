lst = [ 1, 2, "a" ]
lstA = lst

lst = lst + ["b"] # creates a new list by adding the element to the end of the lst
lst = lst[:1] + ["foo"] + lst[2:] # inserts the 2nd parameter into the 1st index

lst = lst[:]  # copy first, so we don't mutate lstC
lst.remove("a") # removes the given element from the list once

lst = lst[1:] # a new list that excludes the element at the given index from the list


print("lstA: ", lstA)
print("lst:", lst)