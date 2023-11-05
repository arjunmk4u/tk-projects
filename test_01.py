from tkinter import *
root = Tk()



a=0
def onClick():
    global a
    a=a+1
    myLabelTwo.config(text=a)

    
myLabelOne=Label(root, text="Hello Wolrd!")
myLabelOne.pack()
myLabelTwo=Label(root, text=a)
myLabelTwo.pack()
myButtonOne=Button(root,text="Click ME",command=onClick)
myButtonOne.pack()
root.mainloop()