from tkinter import *
window=Tk()
window.title("widget")
window.geometry("400x400")
l1=Label(text="Welcome",fg="white",bg="blue",height=1,width=300)
l2=Label(text="Welcome",fg="black",bg="light green")
e1=Entry()

def display():
    name=e1.get()
    global msg
    msg="Hello"+name+"Nice to meet you"
    tb.insert(END,msg)

tb=Text(height=3)
b=Button(text="click",command=display,height=1)

l1.pack()
l2.pack()
e1.pack()
b.pack()
tb.pack()

window.mainloop()