class A:
    def __init__(self, msg, code):
        self.msg = msg
        self.code = code
        print("A")
    def __repr__(self):
        return f"A({self.msg})"
    def bar(self):
        return self.msg.replace('i',self.code )
    def __eq__(self, other):
        if isinstance(other, A):
            return self.msg.lower() == other.msg.lower()
        return False

class B(A):
    def __init__(self, x):
        super().__init__("q" + x, "42")
    def __repr__(self):
        return f"B({self.msg})"
    
class C:
    def __init__(self, x):
        self.x = x
    def bar(self):
        return "quiz" + self.x
    def __repr__(self):
        return f"C({self.x})"
    
a1 = A("quiz", "%")
a2 = A("QUIZ", "#")
b = B("uiz")
c = C("quiz")

print(a1 == a2)
print(a1 == b)
print(a1 == c)

print(type(a1) == type(b))
print(type(a1) == type(c))

print(isinstance(a2, type(a1)))
print(isinstance(b, type(a1)))
print(isinstance(c, type(a1)))

print(a1, a1.bar())
print(a2, a2.bar())
print(b, b.bar())
print(c, c.bar())