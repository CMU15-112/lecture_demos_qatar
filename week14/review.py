def formatDate(s):
    l = s.split('/')
    if len(l[-1]) == 2:
        l[-1] = "20"+l[-1]
    return l[0] + '/' + l[1] + '/' + l[2]


def bestMeetingDay(dayPrefs):
    for k in dayPrefs:
        dayPrefs[k] = formatDate(dayPrefs[k])
    dc = {}
    for k in dayPrefs:
        dc[dayPrefs[k]] = dc.get(dayPrefs[k], 0) + 1
        # the above line is equivalent to the lines below
        #if dayPrefs[k] in dc:
        #    dc[dayPrefs[k]] += 1
        #else:
        #    dc[dayPrefs[k]] = 1
            
    maxc = 0
    for day in dc:
        if dc[day] > maxc:
            maxc = dc[day]
    # maxc is the max value in dc
    # get all keys with value equal to maxc
    res = set()
    for day in dc:
        if dc[day] == maxc:
            res.add(day)
    return res

   
    
    



dayPrefs = { "Omar": "4/18/2023", 
              "john": "4/19/2022", 
              "Karen": "4/19/22",
              "Huda": "4/20/22",
              "Michael": "4/20/2022"
            }

assert(bestMeetingDay(dayPrefs) == {'4/19/2022', '4/20/2022'})
print(":)")