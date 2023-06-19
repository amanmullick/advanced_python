# program for hierarchical inheritance

class A():
    def d1(self):
        print("this is Class A function")

class B(A):
    def d2(self):
        print("this is Class B function")

class C(A):
    def d3(self):
        print("this is Class C function")

ob1 = B()
ob2 = C()

ob1.d1()
ob1.d2()

ob2.d1()
ob2.d3()