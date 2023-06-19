#operator overloading

'''
    task : accomplish addition for two parameters
    o1(23,4)+o2(3,5)
    res = o3(26,9)

'''

class A:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b

    def __add__(self,obj):
        return self.num1+obj.num1,self.num2+obj.num2

    
a1=A(10,2)
a2=A(2,1)

print("res =",a1+a2)


