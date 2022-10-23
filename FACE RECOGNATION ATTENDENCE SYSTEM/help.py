from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class HELP:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="blue",fg="maroon")
        title_lbl.place(x=0,y=0,width=1400,height=50)
        
        img_top=Image.open(r"college_images\HLPL.jpg")
        img_top=img_top.resize((1400,605),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1400,height=605)
        
        l=Label(f_lbl,text="EMAIL ID:kundutridip260@gmail.com",font=("times new roman",15,"bold"),fg="white",bg="gray")
        l.place(x=480,y=200,)
        l=Label(f_lbl,text="EMAIL ID:gangulygourab67@gmail.com",font=("times new roman",15,"bold"),fg="white",bg="gray")
        l.place(x=480,y=235,)
        l=Label(f_lbl,text="EMAIL ID:sharmisthamondol260@gmail.com",font=("times new roman",15,"bold"),fg="white",bg="gray")
        l.place(x=480,y=270,)
        l=Label(f_lbl,text="EMAIL ID:ghoshsia45@gmail.com",font=("times new roman",15,"bold"),fg="white",bg="gray")
        l.place(x=480,y=305)
        
if __name__=="__main__":
    root=Tk()
    obj=HELP(root)
    root.mainloop()
