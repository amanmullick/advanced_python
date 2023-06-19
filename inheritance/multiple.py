#program for multiple inheritance

class Parent1():
    def d1(self):
        print("this is parent1 function")

class Parent2():
    def d1(self):
        print("this is parent2 function")

class Child(Parent1,Parent2):
    def d2(self):
        print("this is child function")


ob = Child()
ob.d1()