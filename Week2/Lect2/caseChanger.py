def caseChanger(s):
    ret=""
    case = 0
    
    for c in s:
        
        if not c.isalpha(): # if non-alph 
            case = (case+1)%2 # switch case
            
        elif case == 0: # if case is lower
            ret+= c.lower() # add lower-case char
            
        else:# case == 1:
            ret+= c.upper()
            
    return ret

assert(caseChanger("$1-") == "")
assert(caseChanger("Hi_ThErE_mY_nAmE")=="hiTHEREmyNAME" )
print("PASSED")