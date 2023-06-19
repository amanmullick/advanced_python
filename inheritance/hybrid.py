#program for hybrid inheritance

class A():
    def d1(self):
        print("this is class A function")

class B(A):
    def d2(self):
        print("this is class B function")

class C(A):
    def d3(self):
        print("this is class C function")

class D(B,C):
    def d4(self):
        print("this is class D function")

ob = D()
ob.d1()
ob.d2()
ob.d3()
ob.d4()