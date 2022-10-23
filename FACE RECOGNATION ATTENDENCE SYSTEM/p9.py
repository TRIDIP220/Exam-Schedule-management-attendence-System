from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class TRAIN:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        
        title_lbl=Label(self.root,text="TRAIN  DATA  SET ",font=("times new roman",35,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1400,height=45)
        
        img_top=Image.open(r"college_images\DK.jpg")
        img_top=img_top.resize((1530,225),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=225)
        
        #botton
        
        b1=Button(self.root,text="TRAIN DATA",command=self.traun_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="green",fg="white")
        b1.place(x=0,y=250,width=1300,height=60)
        
        img_buttom=Image.open(r"college_images\imgref3_orig.jpg")
        img_buttom=img_buttom.resize((1530,680),Image.ANTIALIAS)
        self.photoimg_buttom=ImageTk.PhotoImage(img_buttom)
        
        f_lbl=Label(self.root,image=self.photoimg_buttom)
        f_lbl.place(x=0,y=300,width=1400,height=680)
        
    def traun_classifier(self):
        data_dr=("data")
        path=[os.path.join(data_dr,file) for file in os.listdir(data_dr)]
        
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')#gray scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #train classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=TRAIN(root)
    root.mainloop()
