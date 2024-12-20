from tkinter import*
from math import *
root=Tk()
root.title("Calculator")
root.geometry("210x200")
e=Entry(root,bd=8,width=30)
e.grid(row=0,column=1,columnspan=5)
def setText(txt):
    l=len(e.get())
    e.insert(l,txt)
def clear1():
    txt=e.get()
    e.delete(0,END)
    e.insert(0,txt[:-1])
def clear():
    e.delete(0,END)
def sqroot():
    txt=sqrt(float(e.get()))
    e.delete(0,END)
    e.insert(0,txt)
def negation():
    txt=e.get()
    if txt[0]=="-":
        e.delete(0,END)
        e.insert(0,txt[1:])
    elif txt[0]=="+":
        e.delete(0,END)
        e.insert(0,"-"+txt[1:])
    else:
        e.insert(0,"-")

def equals():
    try:
        s=e.get()
        for i in range(0,len(s)):
            if s[i]=="+" or s[i]=="-" or s[i]=="*"or s[i]=="/" or s[i]=="%" :
                expr=str(float(s[:i]))+s[i:]
                break
            else :
                expr=s
            e.delete(0,END)
            e.insert(0,eval(expr))
    except Exception:
        e.delete(0,END)
        e.insert(0,"INVALID  EXPRESSION")

back1=Button(root,text="<--",command=lambda:clear1(),width=10)
back1.grid(row=1,column=1,columnspan=2)
sqr=Button(root,text=u'\u221A',command=lambda:sqroot(),width=4)
sqr.grid(row=1,column=2)
can=Button(root,text="c",command=lambda:clear(),width=4)
can.grid(row=1,column=3)
neg=Button(root,text="+/-",command=lambda:negation(),width=4)
neg.grid(row=1,column=5)
nine=Button(root,text="9",command=lambda:setText("9"),width=4)
nine.grid(row=2,column=1)
eight=Button(root,text="8",command=lambda:setText("8"),width=4)
eight.grid(row=2,column=2)
seven=Button(root,text="7",command=lambda:setText("7"),width=4)
seven.grid(row=2,column=3)
six=Button(root,text="6",command=lambda:setText("6"),width=4)
six.grid(row=3,column=1)
five=Button(root,text="5",command=lambda:setText("5"),width=4)
five.grid(row=3,column=2)
four=Button(root,text="4",command=lambda:setText("4"),width=4)
four.grid(row=3,column=3)
three=Button(root,text="3",command=lambda:setText("3"),width=4)
three.grid(row=4,column=1)
two=Button(root,text="2",command=lambda:setText("2"),width=4)
two.grid(row=4,column=2)
one=Button(root,text="1",command=lambda:setText("1"),width=4)
one.grid(row=4,column=3)
zero=Button(root,text="0",command=lambda:setText("0"),width=4)
zero.grid(row=5,column=3) #,columnspan=2)
dot=Button(root,text=".",command=lambda:setText("."),width=4)
dot.grid(row=3,column=4)
div=Button(root,text="/",command=lambda:setText("/"),width=4)
div.grid(row=2,column=4)
mul=Button(root,text="*",command=lambda:setText("*"),width=4)
mul.grid(row=4,column=4)
minus=Button(root,text="-",command=lambda:setText("-"),width=4)
minus.grid(row=1,column=4)
plus=Button(root,text="+",command=lambda:setText("+"),width=4)
plus.grid(row=5,column=4)
mod=Button(root,text="%",command=lambda:setText("%"),width=4)
mod.grid(row=5,column=2)
byx=Button(root,text="1/x",command=lambda:setText("%"),width=4)
byx.grid(row=5,column=1)
equal=Button(root,text="=",command=lambda:equals(),width=4,height=3)
equal.grid(row=2,column=5,rowspan=6)
root.mainloop()


        


                    
        