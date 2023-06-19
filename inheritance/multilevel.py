#program for multilevel inheritance

class GrandParent():
    def d1(self):
        print("this is grandparent function")

class Parent(GrandParent):
    def d2(self):
        print("this is parent function")


class Child(Parent):
    def d3(self):
        print("this is child function")

ob = Child()
ob.d1()
ob.d2()
ob.d3()