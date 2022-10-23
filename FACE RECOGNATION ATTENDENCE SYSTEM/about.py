from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class ABOUT:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        img_top=Image.open(r"college_images\DD.jpeg")
        img_top=img_top.resize((1400,350),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1400,height=350)
        
        main_frame=Frame(self.root,bd=0,bg="green")
        main_frame.place(x=0,y=300,width=1400,height=600)
        
        PLAYER_ID_LABLE=Label(main_frame,text="THIS PORTAL IS MADE FOR CRICKETS PLAYERS.BY THIS PORTAL THEY CAN STORE THERE .",font=("times new roman",18,"bold"),bg="green")
        PLAYER_ID_LABLE.place(x=20,y=20)
        
        PLAYER_ID_LABL=Label(main_frame,text="PERSONAL AS WELL AS PROFESSIONAL DETAILS BY CREATING AN ACCOUNT.AT FIRST ",font=("times new roman",18,"bold"),bg="green")
        PLAYER_ID_LABL.place(x=20,y=65)
        
        PLAYER_ID_LAB=Label(main_frame,text="THEY HAVE TO REGISTER THERESELFS  AND LOGIN TO THIS PORTAL. AFTER THAT THEY",font=("times new roman",18,"bold"),bg="green")
        PLAYER_ID_LAB.place(x=20,y=105)
       
        PLAYER_ID_LA=Label(main_frame,text=" CAN STORE THERE DETAILS IN PLAYER'S DETAILS ALSO THEY HAVE TO GIVE THEIR PHOTO ",font=("times new roman",18,"bold"),bg="green")
        PLAYER_ID_LA.place(x=20,y=145)
        
        PLAYER_ID_L=Label(main_frame,text="SAMPLE,AFTER SUCESSFULLY STORED DETAILS TRAIN DATA PART TRAIN THEIR DATA",font=("times new roman",18,"bold"),bg="green")
        PLAYER_ID_L.place(x=20,y=185)
        
        PLAYER_ID_=Label(main_frame,text="TRAIN THEIR DATA THEN FACE RECOGNITION PART RECOGNISED THEIR FACE AND OPEN ",font=("times new roman",18,"bold"),bg="green")
        PLAYER_ID_.place(x=20,y=225)
        
        PLAYER_ID_=Label(main_frame,text="ANOTHER PAGE.WHERE THEY CAN STORE THERE PROFESSIONAL DETAILS",font=("times new roman",18,"bold"),bg="green")
        PLAYER_ID_.place(x=20,y=265)
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=ABOUT(root)
    root.mainloop()