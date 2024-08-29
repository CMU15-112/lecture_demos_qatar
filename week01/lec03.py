import math

# Floats
a = 0.1 + 0.1 + 0.1
print(a)
print(a == 0.3)

print(abs(a-0.3) < 0.00001)
print(math.isclose(a, 0.3))

# Conditionals

def f(x):
    if x > 5:
        print("Yep, that's a big number")
        print("Another line")
    else:
        print("That is a small number")
        
f(4)
f(6)
f(5)

# When x and y are both big, say so.
# When only one of them is big, say that.
# When none of them are big, say nothing.
def g(x, y):

    # x is big
    if x > 5:
        # y is big
        if y > 5:
            print("Those numbers are both big!")
        # y is small
        else:
            print("Only one number was big (1)")
    # x is small
    else:
        # y is big
        if y > 5:
            print("Only one number was big (2)")
        # y is small
  
print("---")
g(6, 7)
print("---")
g(2, 3)
print("---")
g(43, 1)
print("---")
g(2, 67)
print("---")


# When x and y are both big, say so.
# When only one of them is big, say that.
# When none of them are big, say nothing.
def gAgain(x, y):
    if x > 5 and y > 5:
        print("Those numbers are both big!")
    elif (x > 5 and y <= 5) or (x <= 5 and y > 5):
        print("Only one number was big")
        
print("---")
gAgain(6, 7)
print("---")
gAgain(2, 3)
print("---")
gAgain(43, 1)
print("---")
gAgain(2, 67)
print("---")

def scoreToLetterGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "R"
    
# Short-Circuit Analysis

def alwaysTrue():
    print("1")
    return True

def alwaysFalse():
    print("2")
    return False

print(alwaysTrue() and alwaysFalse())
print(alwaysTrue() or alwaysFalse())
print(alwaysFalse() or alwaysTrue())
