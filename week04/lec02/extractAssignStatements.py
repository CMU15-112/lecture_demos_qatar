"""Write the function extractAssignStatements that extracts all assignment
statements from a given text. The left-hand side of the statement must be a
variable name. For simplicity, no numbers are allowed in the variable name. The
right-hand side must be a positive integer. Between both sides, only the
character '=' or spaces can occur. Return a list of tuples, (lhs, rhs)

"""

def extractAssignStatements(text):
    """ write your code here"""




test1 = "hello,class=15112  and anotherVar=42. The end"
test2 = "  .-, anotherVar = 42."
test3="a=98,b=23232;c=543- --=-    d=-42.23"

assert(extractAssignStatements(test1) == [('class','15112'), ('anotherVar','42')])
assert(extractAssignStatements(test2) == [('anotherVar','42')])
assert(extractAssignStatements(test3) == [('a','98'), ('b', '23232'),('c','543')])
