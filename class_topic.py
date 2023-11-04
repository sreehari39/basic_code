# these is multiple inheritance: inheriting 1 or more class in  particlear class  is callled multiple inheritance
class First:
    def add(self, x, y):
        return x + y


class Second:
    def sub(self, x, y):
        return x - y


# class Third(First, Second):
class Third(Second, First):
    def mul(self, x, y):
        return x * y


obj = Third()
print(obj.sub(20, 30))
print(obj.add(20, 30))
print(obj.mul(10, 30))
