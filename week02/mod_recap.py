# Dividend/Divisor = Quotient + Remainder/Divisor
# Dividend = Divisor*Quotient + Remainder

def checkRule(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return (dividend == divisor*quotient + remainder)

print(checkRule(4,2))
print(checkRule(4,3))
print(checkRule(3, 4))
print(checkRule(4, -2))  # largest integer that is no larger than the result



