
import tkinter
from tkinter import*
a=Tk()
a.title("MY calculator")
a.geometry("570x600+100+200")
a.resizable(False,False)
a.configure(bg="#17161b")
equation=""
def show(value):
    global equation
    equation+=value
    top.config(text=equation)
def clear():
    global equation
    equation=""
    top.config(text=equation)
def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    top.config(text=result)

top=Label(a,width=25,height=2,text="",font=("arial",30))
top.pack()
Button(a,text="c",width=4,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=10,y=100)
Button(a,text="/",width=4,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("/")).place(x=150,y=100)
Button(a,text="%",width=4,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("%")).place(x=290,y=100)
Button(a,text="*",width=4,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("*")).place(x=430,y=100)

Button(a,text="7",width=4,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("7")).place(x=10,y=200)
Button(a,text="8",width=4,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("8")).place(x=150,y=200)
Button(a,text="9",width=4,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("9")).place(x=290,y=200)
Button(a,text="-",width=4,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("-")).place(x=430,y=200)

Button(a,text="4",width=4,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("4")).place(x=10,y=300)
Button(a,text="5",width=4,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("5")).place(x=150,y=300)
Button(a,text="6",width=4,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("6")).place(x=290,y=300)
Button(a,text="+",width=4,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("+")).place(x=430,y=300)

Button(a,text="1",width=4,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("1")).place(x=10,y=400)
Button(a,text="2",width=4,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("2")).place(x=150,y=400)
Button(a,text="3",width=4,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("3")).place(x=290,y=400)
Button(a,text="0",width=11,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("0")).place(x=30,y=500)

Button(a,text=".",width=4,height=1,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show(".")).place(x=310,y=500)
Button(a,text="=",width=4,height=3,font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda:calculate()).place(x=430,y=400)
a.mainloop()
