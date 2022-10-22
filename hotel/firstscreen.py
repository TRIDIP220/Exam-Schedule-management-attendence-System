import os
from tkinter import *
from tkinter import messagebox
Window=Tk()
Window.geometry("500x300")
Window.title("MAIL OTP")
Window.configure(bg="lightgreen")

def verify():
    cmd=str(a.get())
    temp='python sendmail.py'+' '+cmd
    os.system(temp)
label1=Label(Window,text="One Time Password",relief="solid",font=("arial",10,"bold"),fg='blue',bg='yellow').pack(fill=BOTH)
a=StringVar()
Re=Label(Window,text="EMAIL ID",font=("arial",10,"bold") ,bg="violet").place(x=0,y=50)
w=Entry(Window,width=30,validate="key",textvariable=a ,bg="Pink")
w.place(x=70,y=53)
log = Button(Window, text="Proceed",relief="raised", bg='yellow', font=("arial", 10, "bold"), fg='black',command=verify).place(x=0,y=120)
Window.mainloop()