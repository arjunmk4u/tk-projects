from tkinter import *
import math
root = Tk()
# root.geometry("500x500")
root.title("Calculator")
# global a
a=[]
    
e=Entry(root,width=35, border=5,font=30)
e.grid(row=0,column=0,columnspan=4,ipady=10)


def buttonClick(number):
    e.insert(0,number)
    num=e.get()
    a.append(num)
    # print(num)
    if number==False:
        e.delete(0, END)
    return a



# def add(a):
#     result=0
#     for x in a:
#         result=result+x
#     e.insert(0,result)
#     print(result)


# def sub(a):
#     result=0
#     for x in a:
#         result=result-a
#     return result

def mul(a):
    print(math.prod(a))

# def div(a):
#     result=0
#     for x in a:
#         result=result/a
#     return result

def calculate(fun):
    match fun:
        case "*": e.delete(0,END), mul(a)
        # case "/": e.delete(0,END), lambda: div(a)
        case "=": print(a)


print(a)

button_one=Button(root,text="1",padx=30,pady=10,command= lambda: buttonClick(1)).grid(row=1,column=0)
button_two=Button(root,text="2",padx=30,pady=10,command= lambda: buttonClick(2)).grid(row=1,column=1)
button_three=Button(root,text="3",padx=30,pady=10,command= lambda: buttonClick(3)).grid(row=1,column=2)
button_four=Button(root,text="4",padx=30,pady=10,command= lambda: buttonClick(4)).grid(row=2,column=0)
button_five=Button(root,text="5",padx=30,pady=10,command= lambda: buttonClick(5)).grid(row=2,column=1)
button_six=Button(root,text="6",padx=30,pady=10,command= lambda: buttonClick(6)).grid(row=2,column=2)
button_seven=Button(root,text="7",padx=30,pady=10,command= lambda: buttonClick(7)).grid(row=3,column=0)
button_eight=Button(root,text="8",padx=30,pady=10,command= lambda: buttonClick(8)).grid(row=3,column=1)
button_nine=Button(root,text="9",padx=30,pady=10,command= lambda: buttonClick(9)).grid(row=3,column=2)
button_zero=Button(root,text="0",padx=30,pady=10,command= lambda: buttonClick(0)).grid(row=4,column=0)
button_clear=Button(root,text="C",padx=30,pady=10,command= lambda: buttonClick(False)).grid(row=4,column=1)
button_equal=Button(root,text="=",padx=30,pady=10,command= lambda: calculate("=")).grid(row=4,column=2)
button_div=Button(root,text="/",padx=30,pady=10,command= lambda: calculate("/")).grid(row=1,column=3)
button_mul=Button(root,text="*",padx=30,pady=10,command= lambda: calculate("*")).grid(row=2,column=3)
button_sub=Button(root,text="-",padx=30,pady=10,command= lambda: calculate("-")).grid(row=3,column=3)
button_add=Button(root,text="+",padx=30,pady=10,command= lambda: calculate("+")).grid(row=4,column=3)





root.mainloop()