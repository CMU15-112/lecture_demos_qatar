# Very simple, far-from-fully implemented Fraction class
# to demonstrate the OOP ideas from above.
# Note that Python actually has a full Fraction class that
# you would use instead (from fractions import Fraction),
# so this is purely for demonstrational purposes.



class Fraction(object):
    
    def __init__(self, num, den):
        # Partial implementation -- does not deal with 0 or negatives, etc
        g = Fraction.gcd(num, den)
        self.num = num // g
        self.den = den // g
    
    def __repr__(self):
        return '%d/%d' % (self.num, self.den)

    def __eq__(self, other):
        return (isinstance(other, Fraction) and
                ((self.num == other.num) and (self.den == other.den)))

    def times(self, other):
        if (isinstance(other, int)):
            return Fraction(self.num * other, self.den)
        else:
            return Fraction(self.num * other.num, self.den * other.den)

    def __hash__(self):
        return hash((self.num, self.den))
    
    @staticmethod
    def gcd(x, y):
        if (y == 0): return x
        else: return Fraction.gcd(y, x%y)
    

def testFractionClass():
    print('Testing Fraction class...', end='')
    assert(str(Fraction(2, 3)) == '2/3')
    assert(str([Fraction(2, 3)]) == '[2/3]')
    assert(Fraction(2,3) == Fraction(2,3))
    assert(Fraction(2,3) != Fraction(2,5))
    assert(Fraction(2,3) != "Don't crash here!")
    assert(Fraction(2,3).times(Fraction(3,4)) == Fraction(1,2))
    assert(Fraction(2,3).times(5) == Fraction(10,3))
    s = set()
    assert(Fraction(1, 2) not in s)
    s.add(Fraction(1, 2))
    assert(Fraction(1, 2) in s)
    s.remove(Fraction(1, 2))
    assert(Fraction(1, 2) not in s)
    print('Passed.')

if (__name__ == '__main__'):
    testFractionClass()