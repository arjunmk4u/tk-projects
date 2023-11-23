from tkinter import *
import math
import time
root = Tk()
root.geometry("395x340")
root.title("Calculator")
root.resizable(False,False)


e=Entry(root,width = 35, border = 1,font = ("default",15),background="#565656",foreground="white")                    #textbox
e.grid(row= 0,column= 0,columnspan= 4,ipady= 20)


def buttonClick(number):                                            #onlcick event
    e.insert(END,number)


def delete():                                                       #Textfield clear function
    e.delete(0,END)


def add():                                                          #add function
    firstNumber= e.get()
    global f_num
    global fun
    fun="add"
    f_num=int(firstNumber)
    e.delete(0,END)

def sub():                                                          #subtract function
    firstNumber= e.get()
    global f_num
    global fun
    fun="sub"
    f_num=int(firstNumber)
    e.delete(0,END)

def mul():                                                          #multiplication function
    firstNumber= e.get()
    global f_num
    global fun
    fun="mul"
    f_num=int(firstNumber)
    e.delete(0,END)


def div():                                                           #division function
    firstNumber= e.get()
    global f_num
    global fun
    fun="div"
    f_num=int(firstNumber)
    e.delete(0,END)


def calculate():                                                     #function selection
    secondNumber=e.get()
    e.delete(0,END)
    try:
        if fun=="add":
            e.insert(0, f"{f_num} + {secondNumber} = {f_num + int(secondNumber)}")
        elif fun=="sub":
            e.insert(0,f"{f_num} - {secondNumber} = {f_num - int(secondNumber)}")
        elif fun == "mul":
            e.insert(0,f"{f_num} * {secondNumber} = {f_num * int(secondNumber)}")
        elif fun == "div":
            try:
                e.insert(0,f"{f_num} / {secondNumber} = {f_num / int(secondNumber)}")
            except ZeroDivisionError:
                e.insert(0,"Syntax ERROR")
    except ValueError:
        e.insert(0,"Enter numeric values")
        

#gui design
root.grid()
button_one = Button(root,text="1",font=("default",12),background="#565656",foreground="white",border=0.5,padx=40,pady=20,command= lambda: buttonClick(1)).grid(row=1,column=0)
button_two = Button(root,text="2",font=("default",12),background="#565656",foreground="white",border=0.5,padx=40,pady=20,command= lambda: buttonClick(2)).grid(row=1,column=1)
button_three = Button(root,text="3",font=("default",12),background="#565656",foreground="white",border=0.5,padx=40,pady=20,command= lambda: buttonClick(3)).grid(row=1,column=2)
button_four = Button(root,text="4",font=("default",12),background="#565656",foreground="white",border=0.5,padx=40,pady=20,command= lambda: buttonClick(4)).grid(row=2,column=0)
button_five = Button(root,text="5",font=("default",12),background="#565656",foreground="white",border=0.5,padx=40,pady=20,command= lambda: buttonClick(5)).grid(row=2,column=1)
button_six = Button(root,text="6",font=("default",12),background="#565656",foreground="white",border=0.5,padx=40,pady=20,command= lambda: buttonClick(6)).grid(row=2,column=2)
button_seven = Button(root,text="7",font=("default",12),background="#565656",foreground="white",border=0.5,padx=40,pady=20,command= lambda: buttonClick(7)).grid(row=3,column=0)
button_eight = Button(root,text="8",font=("default",12),background="#565656",foreground="white",border=0.5,padx=40,pady=20,command= lambda: buttonClick(8)).grid(row=3,column=1)
button_nine = Button(root,text="9",font=("default",12),background="#565656",foreground="white",border=0.5,padx=40,pady=20,command= lambda: buttonClick(9)).grid(row=3,column=2)
button_zero = Button(root,text="0",font=("default",12),background="#565656",foreground="white",border=0.5,padx=40,pady=20,command= lambda: buttonClick(0)).grid(row=4,column=0)
button_clear = Button(root,text="c",font=("default",12),background="#E0974C",foreground="white",border=0.5,padx=40,pady=20,command= delete).grid(row=4,column=1)
button_equal = Button(root,text="=",font=("default",12),background="#3A3A3A",foreground="white",border=0.5,padx=40,pady=20,command= calculate).grid(row=4,column=2)
button_div = Button(root,text="/",font=("default",13),background="#3A3A3A",foreground="white",border=0.5,padx=41,pady=20,command= div).grid(row=1,column=3)
button_mul = Button(root,text="*",font=("default",13),background="#3A3A3A",foreground="white",border=0.5,padx=40,pady=20,command= mul).grid(row=2,column=3)
button_sub = Button(root,text="-",font=("default",13),background="#3A3A3A",foreground="white",border=0.5,padx=40,pady=20,command= sub).grid(row=3,column=3)
button_add = Button(root,text="+",font=("default",12),background="#3A3A3A",foreground="white",border=0.5,padx=39,pady=20,command= add).grid(row=4,column=3)


root.mainloop()