#tkinter module
from tkinter import *
from tkinter import messagebox as msg

root = Tk()
root.title("calculator")
root.geometry('500x500')
root.resizable(False,False)

#functions

def Add():
    if n1.get()=="" or n2.get()=="":
        msg.showinfo("Status : ","Enter any two numbers !!!")
    else:
        nn1=int(n1.get())
        nn2=int(n2.get())
        msg.showinfo("Status : ",f"Addition of {nn1} and {nn2} = {nn1+nn2}")


def Sub():
    if n1.get()=="" or n2.get()=="":
        msg.showinfo("Status : ","Enter any two numbers !!!")
    else:
        nn1=int(n1.get())
        nn2=int(n2.get())
        msg.showinfo("Status : ",f"Subtraction of {nn1} and {nn2} = {nn1-nn2}")


def Mul():
    if n1.get()=="" or n2.get()=="":
        msg.showinfo("Status : ","Enter any two numbers !!!")
    else:
        nn1=int(n1.get())
        nn2=int(n2.get())
        msg.showinfo("Status : ",f"Multiplication of {nn1} and {nn2} = {nn1*nn2}")


def Div():
    if n1.get()=="" or n2.get()=="":
        msg.showinfo("Status : ","Enter any two numbers !!!")
    else:
        nn1=int(n1.get())
        nn2=int(n2.get())
        msg.showinfo("Status : ",f"Division of {nn1} and {nn2} = {nn1/nn2}")


num1 = Label(root,text="Number 1")
num1.place(x=100,y=50)

n1=Entry(root)
n1.place(x=200,y=50)

num2 = Label(root,text="Number 2")
num2.place(x=100,y=100)

n2=Entry(root)
n2.place(x=200,y=100)




btnAdd = Button(root,text="+",command=Add)
btnAdd.place(x=150,y=200)
btnSub = Button(root,text="-",command=Sub)
btnSub.place(x=200,y=200)
btnMul = Button(root,text="*",command=Mul)
btnMul.place(x=250,y=200)
btnDiv = Button(root,text="/",command=Div)
btnDiv.place(x=300,y=200)


root.mainloop()