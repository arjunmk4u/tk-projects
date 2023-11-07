from tkinter import *
root = Tk()
# root.geometry("500x500")

courseList=[
    "English",
    "R",
    "Python",
    "Statistics",
    "Software Engineering",
]
menu = StringVar()
menu.set("Select course")

sList=StringVar()
sList.set("Show students")

db={}
x=list(db.values())

def sub():
    db["RollNo"] = rollNo_in.get()
    db["Name"] = name_in.get()
    db["dep"] = dep_in.get()
    # db.update({"course":course_in.get()})
    rollNo_in.delete(0,END)
    name_in.delete(0,END)
    dep_in.delete(0,END)

def show():
    print(db)
    rollNo_in.insert(0,db.get("RollNo"))
    name_in.insert(0,db.get("Name"))
    dep_in.insert(0,db.get("dep"))


root.grid()
title=Label(root, text="Enter your details").grid(row=0,column=0,columnspan=2)
rollNo= Label(root, text="Roll No",anchor="w",justify="left").grid(row=1,column=0,pady=3)
name= Label(root, text="Name",anchor="w",justify="left").grid(row=2,column=0,pady=3)
dep= Label(root, text="Class",anchor="w",justify="left").grid(row=3,column=0,pady=3)
# course= Label(root, text="Course",anchor="w",justify="left").grid(row=4,column=0,padx=20,pady=3)


rollNo_in=Entry(root,textvariable="Enter roll no")
rollNo_in.grid(row=1,column=1)
name_in=Entry(root,textvariable="Enter Name")
name_in.grid(row=2,column=1)
dep_in=Entry(root,textvariable="Enter Department")
dep_in.grid(row=3,column=1)
# course_in= OptionMenu(root, menu, *courseList)
# course_in.grid(row=4,column=1,padx=20,pady=3)

submit=Button(root,text="Submit",command= sub,width=22,anchor="center",justify="right").grid(row=4,column=0,columnspan=2)
showStd=Button(root,text="Show",command= show,width=22,anchor="center",justify="right").grid(row=5,column=0,columnspan=2)


root.mainloop()
