%finding the count of the element that meets that meets a given criteria (is multiple of 4)


def meetsCriteria(element):
    if(element %4 ==0): ## is multiple of 4
        return True
    return False

def findCount(element):
    count= 0
    toExamine =0
    
    while(toExamine <= element):
        toExamine+=1
        
        if(meetsCriteria(toExamine)):
            print("Hit: ", toExamine)
            count+=1
    
    return count
    

findCount(28)