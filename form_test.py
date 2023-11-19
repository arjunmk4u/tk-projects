from tkinter import *
root = Tk()
# root.geometry("500x500")


# list for listbox

courseList=[
    "English",
    "R",
    "Python",
    "Statistics",
    "Software Engineering",
]

#dictionary for storing values
db={}          
#dictionary to list                     
x=list(db.values())                 

#submit function
def sub():                          
    db["RollNo"] = rollNo_in.get()
    db["Name"] = name_in.get()
    db["dep"] = dep_in.get()
    db["Course"] = course_in.get(listSel)
    rollNo_in.delete(0,END)
    name_in.delete(0,END)
    dep_in.delete(0,END)

#Show function
def show():                         
    valueYes = rollNo_in.get()
    if  valueYes:
        pass
    else:
        print(db)
        rollNo_in.insert(0,db.get("RollNo"))
        name_in.insert(0,db.get("Name"))
        dep_in.insert(0,db.get("dep"))
        output.set(','.join(map(str,db.items())))
        
    
#listbox selection event handler
def onSel(event):                   
    global listSel
    listSel = course_in.curselection()


#Text variables and entry boxes
root.grid()
title=Label(root, text="Enter your details").grid(row=0,column=0,columnspan=2)
rollNo= Label(root, text="Roll No",anchor="w",justify="left").grid(row=1,column=0,pady=3)
name= Label(root, text="Name",anchor="w",justify="left").grid(row=2,column=0,pady=3)
dep= Label(root, text="Class",anchor="w",justify="left").grid(row=3,column=0,pady=3)
course= Label(root, text="Course",anchor="w",justify="left").grid(row=4,column=0,padx=20,pady=3)
courseSel= Label(root, textvariable='listSel',anchor="w",justify="left").grid(row=4,column=1,padx=20,pady=3)


#GUI Design
rollNo_in=Entry(root,textvariable="Enter roll no")
rollNo_in.grid(row=1,column=1)
name_in=Entry(root,textvariable="Enter Name")
name_in.grid(row=2,column=1)
dep_in=Entry(root,textvariable="Enter Department")
dep_in.grid(row=3,column=1)
course_in= Listbox(root, selectmode=SINGLE)
course_in.bind("<<ListboxSelect>>", onSel)
course_in.grid(row=5,column=1,padx=20,pady=3)
#Listbox items adding
for item in courseList:
    course_in.insert(END,item)

output= StringVar()
output.set("Click show to view entered details")
out= Label(root, textvariable=output,anchor="w",justify="left").grid(row=8,column=0,pady=3)

#buttons
submit=Button(root,text="Submit",command= sub,width=22,anchor="center",justify="right").grid(row=6,column=0,columnspan=2)
showStd=Button(root,text="Show",command= show,width=22,anchor="center",justify="right").grid(row=7,column=0,columnspan=2)


root.mainloop()
