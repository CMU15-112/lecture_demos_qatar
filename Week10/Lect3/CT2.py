class A(object):
    def __init__(self):
        self.b = "Panda"

    def f(self):
        return self.g()

    def g(self):
        return "KungFu"

class B(A):
    def __init__(self, s):
        super().__init__()
        self.b = s

    def f(self, s):
        self.d = " Master"
        return self.h(s) + self.d

    def h(self, s):
        print(f"{s} Soup")
        return super().g()

def ct4():
    a = A()
    b = B("Po")
    print(isinstance(b, A))
    print(b.b)
    return b.f("Noodles")

print(ct4())