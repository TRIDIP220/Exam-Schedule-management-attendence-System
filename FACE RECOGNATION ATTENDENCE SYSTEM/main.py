

from cProfile import label
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from student import PLAYERS
from train import TRAIN
from pop import Face_recognition
from developer import Developer
from help import HELP
from time import strftime
from datetime import datetime
from Attendence import Attendence


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        img=Image.open(r"college_images\gh.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lb2=Label(self.root,image=self.photoimg)
        f_lb2.place(x=0,y=0,width=500,height=130)
        
        img1=Image.open(r"college_images\pp.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=500,height=130)
        
        img2=Image.open(r"college_images\kp.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=800,y=0,width=500,height=130)

        img3=Image.open(r"college_images\SM.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_mg=Label(self.root,image=self.photoimg3)
        bg_mg.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_mg,text="FACE  RECOGNITION ATTENDANCE SYSTEM ",font=("times new roman",30,"bold"),bg="darkgrey",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text= string)
            lbl.after(1000,time)
            
        lbl = Label(title_lbl,font=("time new roman",10,"bold"),background="darkgray",foreground="blue")
        lbl.place(x=0,y=0,width=90,height=50)
        time()
            
        #player details
        img4=Image.open(r"college_images\ft.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_mg,image=self.photoimg4,command=self.player_details,cursor="hand2")
        b1.place(x=200,y=100,width=150,height=150)
        
        b1=Button(bg_mg,text="STUDENT DETAILS",command=self.player_details,cursor="hand2",font=("bold"),bg="cyan")
        b1.place(x=200,y=220,width=150,height=30)
        #face detect
        img5=Image.open(r"college_images\hj.jpg")

        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_mg,image=self.photoimg5,cursor="hand2",command=self.Face_data)
        b1.place(x=400,y=100,width=150,height=150)
        
        b1=Button(bg_mg,text="FACE DETECTOR",cursor="hand2",command=self.Face_data,font=("bold"),bg="cyan")
        b1.place(x=400,y=220,width=150,height=30)
        #Player Attendence
        img6=Image.open(r"college_images\att.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_mg,image=self.photoimg6,cursor="hand2",command=self.AB)
        b1.place(x=600,y=100,width=150,height=150)
        
        b1=Button(bg_mg,text="ATTENDENCE",cursor="hand2",command=self.AB,font=("bold"),bg="cyan")
        b1.place(x=600,y=220,width=150,height=30)
        #Help Desk
        img7=Image.open(r"college_images\HL.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_mg,image=self.photoimg7,cursor="hand2",command=self.Hel)
        b1.place(x=800,y=100,width=150,height=150)
        
        b1=Button(bg_mg,text="HELP DESK",cursor="hand2",command=self.Hel,font=("bold"),bg="cyan")
        b1.place(x=800,y=220,width=150,height=30)
        #photos
        img8=Image.open(r"college_images\PP.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_mg,image=self.photoimg8,cursor="hand2",command=self.open_img)
        b1.place(x=200,y=300,width=150,height=150)
        
        b1=Button(bg_mg,text="PHOTO",cursor="hand2",command=self.open_img,font=("bold"),bg="cyan")
        b1.place(x=200,y=420,width=150,height=30)
        #train data
        img9=Image.open(r"college_images\di.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_mg,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=400,y=300,width=150,height=150)
        
        b1=Button(bg_mg,text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("bold"),bg="cyan")
        b1.place(x=400,y=420,width=150,height=30)
        #Develope
        img10=Image.open(r"college_images\DD.jpeg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_mg,image=self.photoimg10,cursor="hand2",command=self.DEV)
        b1.place(x=600,y=300,width=150,height=150)
        
        b1=Button(bg_mg,text="DEVELOPER",cursor="hand2",command=self.DEV,font=("bold"),bg="cyan")
        b1.place(x=600,y=420,width=150,height=30)
        #exit
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_mg,image=self.photoimg11,cursor="hand2",command=self.exit)
        b1.place(x=800,y=300,width=150,height=150)
        
        b1=Button(bg_mg,text="EXIT",cursor="hand2",command=self.exit,font=("bold"),bg="cyan")
        b1.place(x=800,y=420,width=150,height=30)
        
    def open_img(self):
        os.startfile("data")
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face_Recognition_System","Are you sure to exit this page?",parent=self.root)
        if  self.exit >0:
            self.root.destroy()
        else:
            return
        
    def player_details(self):
        self.new_window=Toplevel(self.root)
        self.app=PLAYERS(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=TRAIN(self.new_window)
    def Face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
    def DEV(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    def Hel(self):
        self.new_window=Toplevel(self.root)
        self.app=HELP(self.new_window)
    def AB(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)
        
    
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()


