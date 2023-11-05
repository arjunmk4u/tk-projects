#increment decrement in tkinter
from tkinter import *
root = Tk()
root.geometry("500x500")
a=0
label= StringVar()
label.set(f'I am at position {a}')
if a<0:
        label.set("Sorry no negatives")
def increment():
    global a
    a=a+1
    label.set(f'I am at position {a}')

def decrement():
    global a
    a=a-1
    label.set(f'I am at position {a}')


labelOne=Label(root , textvariable=label).grid(row=1,column=0)
inc=Button(root,text=f'Increment', command=increment,padx=20).grid(row=0,column=1)
dec=Button(root,text=f'Decrement',command=decrement,padx=20).grid(row=0,column=0)
qt=Button(root,text="QUIT",command=quit,padx=20).grid(row=2,column=0)
root.mainloop()