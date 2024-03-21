
def gcd(x, y): #recursion
    if(y==0): return x
    else: return gcd(y, x%y)


'''
Write the class Fraction so that the test code runs as specified.
Do not hardcode against the values used in the testcases, though you can assume that the testcases cover the needed functionality.
You must use proper OOP design

NOTE: You don’t need to deal with 0 or negatives for now
'''
class Fraction(object):
    
    def __init__(self, num, den):
        g= gcd(num, den)
        self.num= num//g
        self.den= den//g
        
    def __repr__(self):
        return f"{self.num}/{self.den}"
    
    def __eq__(self, other):
        return (type(other)==type(self)) and (self.num==other.num) and (self.den== other.den)

    def times(self, n):
        
        if type(n)==int:
            return Fraction(n*self.num, self.den)
        else:
            return Fraction(self.num*n.num, self.den*n.den)

    def __hash__(self):
        return hash((self.num, self.den))
        

def testFractionClass():
    
    print('Testing Fraction class...', end='')
    # __init__ and __repr__
    assert(str(Fraction(2, 3)) == '2/3')
    assert(str([Fraction(2, 3)]) == '[2/3]')
    
    #__eq__
    assert(Fraction(2,3) == Fraction(4,6))
    assert(Fraction(2,3) != Fraction(2,5))
    assert(Fraction(2,3) != "Don't crash here!")
    
    #times
    assert(Fraction(2,3).times(Fraction(3,4)) == Fraction(1,2))
    assert(Fraction(2,3).times(5) == Fraction(10,3))
    
    #hash
    s = set()
    assert(Fraction(1, 2) not in s)
    s.add(Fraction(1, 2))
    assert(Fraction(1, 2) in s)
    s.remove(Fraction(1, 2))
    assert(Fraction(1, 2) not in s)
    print('Passed.')

if (__name__ == '__main__'):
    testFractionClass()