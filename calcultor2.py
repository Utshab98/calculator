from tkinter import *
import math
win=Tk()
win.title("Calculator")
win.geometry("325x375")
win.configure(bg="Grey")

# Input section
Ib=Entry(win,width=20,borderwidth=2,font=("Times New Roman",18),justify='right')
Ib.grid(row=0,column=0,columnspan=4)

def click(number):
    Ib.insert(END,number)

def clear():
    Ib.delete(0,END)

def add():
    global first_number
    global function
    first_number=Ib.get()
    Ib.delete(0,END)
    function="+"

def subt():
    global first_number
    global function
    first_number=Ib.get()
    Ib.delete(0,END)
    function="^"

def mul():
    global first_number
    global function
    first_number=Ib.get()
    Ib.delete(0,END)
    function="*"

def divi():
    global first_number
    global function
    first_number=Ib.get()
    Ib.delete(0,END)
    function="/"

def equals_to():
    second_number=Ib.get()
    clear()
    if function=="+":
        Ib.insert(0,float(first_number)+float(second_number))
    if function=="-":
        Ib.insert(0,float(first_number)-float(second_number))
    if function=="*":
        Ib.insert(0,float(first_number)*float(second_number))
    if function=="/":
        Ib.insert(0,float(first_number)/float(second_number))

    

# Button Section
button1= Button(win,text="1",padx=25,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda: click(1))
button2= Button(win,text="2",padx=25,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda: click(2))
button3= Button(win,text="3",padx=25,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda: click(3))
button4= Button(win,text="4",padx=25,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda: click(4))
button5= Button(win,text="5",padx=25,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda: click(5))
button6= Button(win,text="6",padx=25,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda: click(6))
button7= Button(win,text="7",padx=25,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda: click(7))
button8= Button(win,text="8",padx=25,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda: click(8))
button9= Button(win,text="9",padx=25,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda: click(9))
button0= Button(win,text="0",padx=25,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=lambda: click(0))

button_clear= Button(win,text="C",padx=25,pady=20,bg="black",fg="white",font=("Times New Roman",18),command= clear)
button_equals= Button(win,text="=",padx=25,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=equals_to)
button_add= Button(win,text="+",padx=25,pady=20,bg="black",fg="white",font=("Times New Roman",18),command= add)
button_sub= Button(win,text="-",padx=25,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=subt)
button_multiply= Button(win,text="*",padx=25,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=mul)
button_div= Button(win,text="/",padx=25,pady=20,bg="black",fg="white",font=("Times New Roman",18),command=divi)


button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button0.grid(row=4,column=1)

button_clear.grid(row=4,column=0)
button_equals.grid(row=4,column=2)

button_add.grid(row=1,column=3)
button_sub.grid(row=2,column=3)
button_multiply.grid(row=3,column=3)
button_div.grid(row=4,column=3)




win.mainloop()