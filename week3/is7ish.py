def is7ish(n):
   n =abs(n)
   sum =0
   while n!=0:
       sum += n%10
       n = n //10
   return sum%7==0

assert is7ish(0)
assert is7ish(1) == False
assert is7ish(16)
assert is7ish(19) == False
assert is7ish(9999999)
print("passed! yey!")
