'''
This version uses nested loops to count occurrences of each name.
'''
def mostCommonName_n2(names):
    if not names:
        return None
    
    maxCount = 0 # counter to keep track of the count of 
    mostCommonNames = set() # a set to track the most common names
    
  # iterate over list items
    for name in names: # n steps
        # for each list item, count how many times it appears
        count = names.count(name) # O(N)
        # if it's count is greater than maxCount
        if count > maxCount:
            maxCount = count  # update maxCount
            mostCommonNames = {name} # reset the set to the current name
        elif count == maxCount: # it has same count as the maxCount (one of the most frequent)
            mostCommonNames.add(name) # add it to the name
    
    if len(mostCommonNames) == 1: # if one element, pop it and return it
        return mostCommonNames.pop()
        
    return mostCommonNames

'''
This version sorts the list of names and then counts consecutive occurrences.
'''
def mostCommonName_nlogn(names):
    if not names:
        return None
    
    names.sort()
    maxCount = 0
    mostCommonNames = set()
    currCount = 1
    
    for i in range(1, len(names)):
        if names[i] == names[i - 1]: # if curr element equal to prev
            currCount += 1 # incremet currCOunter 
            
        else: # we hit a different name - we need to reasses previous sequence of consecutive occurances
            
            if currCount > maxCount: # if it is more than max seq seen so far
                maxCount = currCount # reset max val
                mostCommonNames = {names[i - 1]} #  create a new set with the prev element
            
            elif currCount == maxCount: # if prev seq len is equal to the current max 
                mostCommonNames.add(names[i - 1]) # add prev to the set
            
            currCount = 1 # reset the curr seq counter to 1 
    
    # We always reassessed the prevSequence when we hit a new different element
        # Check the last name
    if currCount > maxCount:
        mostCommonNames = {names[-1]}
    elif currCount == maxCount:
        mostCommonNames.add(names[-1])
    
    # pop last item if it is one element and return it
    if len(mostCommonNames) == 1:
        return mostCommonNames.pop()
    
    return mostCommonNames


'''
This version uses a dictionary to count occurrences of each name.
'''
def mostCommonName_n(names):
    if not names:
        return None
    
    # create dictionaries to track the words and their counts
    nameCount = {} 
    maxCount = 0
    mostCommonNames = set()
    
    # iterate over list items
    for name in names: # N
        # update the current name count value (get the value, return o if not there) + 1
        nameCount[name] = nameCount.get(name, 0) + 1
        # if current name count > maxCount
        if nameCount[name] > maxCount:
            # update max coutn value
            maxCount = nameCount[name]
            # create a set with that name 
            mostCommonNames = {name}
        # if it is equal..
        elif nameCount[name] == maxCount:
            # add the element to the set
            mostCommonNames.add(name)
    
    # if one element, pop it and return it
    if len(mostCommonNames) == 1:
        return mostCommonNames.pop()
    
    return mostCommonNames



def testMostCommonName(): 
    print("Testing mostCommonName_n2()...", end="") 
    assert(mostCommonName_n2(["Jane", "Aaron", "Cindy", "Aaron"]) == "Aaron") 
    assert(mostCommonName_n2(["Jane", "Aaron", "Jane", "Cindy", "Aaron"]) == {"Aaron", "Jane"}) 
    assert(mostCommonName_n2(["Cindy"]) == "Cindy") 
    assert(mostCommonName_n2(["Jane", "Aaron", "Cindy"]) == {"Aaron", "Cindy", "Jane"}) 
    assert(mostCommonName_n2([]) == None)
    print("Passed!")
    
    print(mostCommonName_nlogn(["Jane", "Aaron", "Cindy", "Aaron"]))
    
    print("Testing mostCommonName_nlogn()...", end="") 
    assert(mostCommonName_nlogn(["Jane", "Aaron", "Cindy", "Aaron"]) == "Aaron") 
    assert(mostCommonName_nlogn(["Jane", "Aaron", "Jane", "Cindy", "Aaron"]) == {"Aaron", "Jane"}) 
    assert(mostCommonName_nlogn(["Cindy"]) == "Cindy") 
    assert(mostCommonName_nlogn(["Jane", "Aaron", "Cindy"]) == {"Aaron", "Cindy", "Jane"}) 
    assert(mostCommonName_nlogn([]) == None)
    print("Passed!") 


    print("Testing mostCommonName_n()...", end="") 
    assert(mostCommonName_n(["Jane", "Aaron", "Cindy", "Aaron"]) == "Aaron") 
    assert(mostCommonName_n(["Jane", "Aaron", "Jane", "Cindy", "Aaron"]) == {"Aaron", "Jane"}) 
    assert(mostCommonName_n(["Cindy"]) == "Cindy") 
    assert(mostCommonName_n(["Jane", "Aaron", "Cindy"]) == {"Aaron", "Cindy", "Jane"}) 
    assert(mostCommonName_n([]) == None)
    print("Passed!")
    
testMostCommonName() 
