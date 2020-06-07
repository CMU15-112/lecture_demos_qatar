class Test:
    pass
class Newtest(object):
    def __init__(self, x):
        self.x = x
    def increaseX(step):
        x += step

test = Test()
newtest = Newtest(8)
print(newtest.x)

print(type(test))
print(type(newtest))

newtest.increaseX(1)  # we are trying to call increaseX(newtest, 1)
