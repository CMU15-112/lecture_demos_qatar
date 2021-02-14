# Open theFile and read in the groupings.
# Returns a list of lists.
def groupParser(theFile):
    retList = []
    with open(theFile, "r") as f:
        for line in f:
            colonSplit = line.split(":")
            commaSplit = colonSplit[1].split(",")
            
            for i in range(len(commaSplit)):
                commaSplit[i] = commaSplit[i].strip()
            
            retList.append(commaSplit)
    return retList
            
result = groupParser("groups.txt")
print(result)
print(result[1])
print(result[1][0])
print(result[1][0][2])