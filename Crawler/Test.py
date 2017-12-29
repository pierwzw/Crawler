print('A')
class MyObject(object):
    print('B')
    c=1
    MyObject.f2()
    def __init__(self, name):
        print('C')
        self.name = name
        print('D')
        self.f1()
        print(MyObject.c)

    @classmethod
    def f1(cls):
        print('F')
        cls.f2()
        c = 2

    @staticmethod
    def f2():
        print('G')
        c = 2

    def f3(self):
        c = 3

print('E')
my_object1 = MyObject('Hello')