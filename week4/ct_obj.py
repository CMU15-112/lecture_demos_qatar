class A(object):
    def __init__(self):
        self.b = "Puppy"
    def f(self):
        print("Dog")
    def g(self):
        print("Cat")
    def h(self):
        print(f"{self.b}: Pony")
        self.g()
class B(A):
    def __init__(self, s):
        self.b = s
        super().__init__()
    def g(self):
        print("Falcon")
        super().g()
    def h(self, s):
        super().h()
        print(f"{s}: Tiger")
def ct2():
    b = B("Sheep")
    b.h("Moo")
    
ct2()