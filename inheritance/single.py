#program for single level inheritance

class Parent:       #create the Parent class
    def d1(self):
        print("this is parent class function")

class Child(Parent):    #inheriting class Parent in Child class
    def d2(self):
        print("this is child class function")

ob = Child()
ob.d1()
ob.d2()