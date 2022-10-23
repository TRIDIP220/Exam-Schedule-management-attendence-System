from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="NavajoWhite",fg="maroon")
        title_lbl.place(x=0,y=0,width=1400,height=50)
        
        img_top=Image.open(r"college_images\bg1.jpg")
        img_top=img_top.resize((1530,625),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=625)
        
        #Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=800,y=0,width=480,height=600)
        
        img_side=Image.open(r"college_images\DEV1.jpg")
        img_side=img_side.resize((130,130),Image.ANTIALIAS)
        self.photoimg_side=ImageTk.PhotoImage(img_side)
        
        f_lbl=Label(main_frame,image=self.photoimg_side)
        f_lbl.place(x=0,y=0,width=130,height=130)
        
        #Info
        
        PLAYER_ID_LABLE=Label(main_frame,text=" NAME -TRIDIP KUNDU",font=("times new roman",13,"bold"),bg="white")
        PLAYER_ID_LABLE.place(x=200,y=5)
        
        PLAYER_ID_LABL=Label(main_frame,text=" AGE- 20",font=("times new roman",13,"bold"),bg="white")
        PLAYER_ID_LABL.place(x=200,y=40)
        
        PLAYER_ID_LAB=Label(main_frame,text=" PROFESSION-STUDENT",font=("times new roman",13,"bold"),bg="white")
        PLAYER_ID_LAB.place(x=200,y=80)
        
        
        
        img_s=Image.open(r"college_images\DEV5.jpg")
        img_s=img_s.resize((130,130),Image.ANTIALIAS)
        self.photoimg_s=ImageTk.PhotoImage(img_s)
        
        f_lbl=Label(main_frame,image=self.photoimg_s)
        f_lbl.place(x=0,y=150,width=130,height=130)
        
        
        PLAYER_ID_LA=Label(main_frame,text=" NAME -GOURAB  GANGULY",font=("times new roman",13,"bold"),bg="white")
        PLAYER_ID_LA.place(x=200,y=170)
        
        PLAYER_ID_L=Label(main_frame,text=" AGE- 20",font=("times new roman",13,"bold"),bg="white")
        PLAYER_ID_L.place(x=200,y=200)
        
        PLAYER_ID_=Label(main_frame,text=" PROFESSION-STUDENT",font=("times new roman",13,"bold"),bg="white")
        PLAYER_ID_.place(x=200,y=230)
        
        img=Image.open(r"college_images\DEV3.jpg")
        img=img.resize((130,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(main_frame,image=self.photoimg)
        f_lbl.place(x=0,y=300,width=130,height=130)
        
        
        PLAYER_ID_LA=Label(main_frame,text=" NAME -SIA GHOSH",font=("times new roman",13,"bold"),bg="white")
        PLAYER_ID_LA.place(x=200,y=320)
        
        PLAYER_ID_L=Label(main_frame,text=" AGE- 20",font=("times new roman",13,"bold"),bg="white")
        PLAYER_ID_L.place(x=200,y=350)
        
        PLAYER_ID_=Label(main_frame,text=" PROFESSION-STUDENT",font=("times new roman",13,"bold"),bg="white")
        PLAYER_ID_.place(x=200,y=379)
        
        img_=Image.open(r"college_images\DEV2.jpg")
        img_=img_.resize((130,130),Image.ANTIALIAS)
        self.photoimg_=ImageTk.PhotoImage(img_)
        
        f_lbl=Label(main_frame,image=self.photoimg_)
        f_lbl.place(x=0,y=455,width=130,height=130)
        
        
        PLAYER_I=Label(main_frame,text=" NAME -SHARMISTA MONDOL",font=("times new roman",13,"bold"),bg="white")
        PLAYER_I.place(x=200,y=455)
        
        PLAYER_=Label(main_frame,text=" AGE- 20",font=("times new roman",13,"bold"),bg="white")
        PLAYER_.place(x=200,y=485)
        
        PLAYE=Label(main_frame,text=" PROFESSION-STUDENT",font=("times new roman",13,"bold"),bg="white")
        PLAYE.place(x=200,y=515)
        
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
