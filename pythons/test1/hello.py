class oma():
    name = ""
    toinen = "xx"
    def __init__(self, name_in):
        self.name = name_in
    def method1(self):
        print(self.name)
class toka(oma):
    def method2(self):
        print("tokasta " + self.name)
your_name = input('what is your name? ')
print("hello " + your_name)
obj1 = toka(your_name)
obj1.method1()
obj1.method2()
print(obj1.toinen)