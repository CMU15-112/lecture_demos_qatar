def longestMatchingSchedule(rosters):
    # extract the schedules
    studentToCourses = {}
    for program in rosters:
        pdict = rosters[program]
        for course in pdict:
            cdict = pdict[course]
            for s in cdict:
                if s not in studentToCourses:
                    studentToCourses[s] = [course]
                else:
                    studentToCourses[s].append(course)
    # now we find the longest match
    coursesToStudents = {}
    cMax = 0
    for s in studentToCourses:
        cTuple = tuple(sorted(studentToCourses[s]))
        if cTuple not in coursesToStudents:
            coursesToStudents[cTuple] = {s}
        else:
            coursesToStudents[cTuple].add(s)
            if len(cTuple) > cMax:
                cMax = len(cTuple)
    return cMax
    

rosters1 = {
 'CS': 
     {'15-213': {'ahmed'}, 
      '15-150': {'ahmed'}
     }, 
 'IS': 
     {'67-262': {'betty', 'ahmed'}
     }, 
 'HCI': 
     {'05-318': {'fred'}}, 
 'BS': 
     {'70-340': {'omar', 'huda'}, 
      '70-257': {'ahmed', 'betty'}
     }
}

assert longestMatchingSchedule(rosters1) == 1