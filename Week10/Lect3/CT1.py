class A(object):
    def __init__(self):
        self.b = "sparkling"
    
    def f(self):
        return self.g()

    def g(self):
        return "apple"
    
    def h(self, s):
        print(f"{self.b} {s}")
        return self.f()

    def __repr__(self):
        return f'A {self.f()}'


class B(A):
    
    def __init__(self, s):
        super().__init__()
        self.b = s
    
    def f(self):
        s=self.g()
        return f"pine{s}"
    
    def g(self):
        return super().g()

def ct3():
    b = B("still")
    print(b.h("water"))
    print(type(b) == A)
    print(isinstance(b, B))
    print(isinstance(b, A))
    return b

print(ct3())