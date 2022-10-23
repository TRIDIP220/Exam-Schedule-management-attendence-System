from tkinter import *
import webbrowser
from PIL import Image,ImageTk
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

from requests import delete
#import subprocess
#n=1





class Face_recognition:
    def __init__(self,root):
        self.cc=StringVar()
        
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        title_lbl=Label(self.root,text="FACE   RECOGNITION  ",font=("times new roman",30,"bold"),bg="green",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        #1st Img
        img_top=Image.open(r"college_images\SA.png")
        img_top=img_top.resize((580,600),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=750,y=50,width=580,height=600)
        #2nd Img
        img_side=Image.open(r"college_images\SM.jpg")
        img_side=img_side.resize((750,600),Image.ANTIALIAS)
        self.photoimg_side=ImageTk.PhotoImage(img_side)
        
        f_lbl=Label(self.root,image=self.photoimg_side)
        f_lbl.place(x=0,y=50,width=750,height=600)
        
        #bottom
        b1=Button(self.root,text="FACE DETECTOR",cursor="hand2",command=self.face_recog,font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1.place(x=950,y=500,width=250,height=40)
        #Attendence
    def attendence(self,g,j,l,p):
      with open("Gourab.csv","r+",newline="\n") as f:
        mydatalist=f.readlines()
        nam_list=[]
        for line in mydatalist:
          entry=line.split((","))
          nam_list.append(entry[0])
        if((g not in nam_list) and(j not in nam_list) and(l not in nam_list) and(p not in nam_list)):
          now=datetime.now()
          d1=now.strftime("%d/%m/%Y")
          dtstring=now.strftime("%H:%M:%S")
          f.writelines(f"\n{g},{j},{l},{p},{dtstring},{d1},Present")
          
          
      
      
       
        #Face Recognition
    def face_recog(self):
        m=0
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
          gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
          features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
          
          
          coord=[]
          for (x,y,w,h) in features:
              cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
              id,predict=clf.predict(gray_image[y:y+h,x:x+w])
              confidence=int((100*(1-predict/300)))
              
              conn=mysql.connector.connect(host="localhost",username="root",password="GOURAB@2002",database="facerecognition")
              my_cursor=conn.cursor()
              
              
              
              my_cursor.execute("select NAME from play_ers where ID="+str(id))
              j=my_cursor.fetchone()
              j="+".join(j)
              
              my_cursor.execute("select ROLL_NO from play_ers where ID="+str(id))
              l=my_cursor.fetchone()
              l="+".join(l)
              
              my_cursor.execute("select STREAM from play_ers where ID="+str(id))
              p=my_cursor.fetchone()
              p="+".join(p)
              
              my_cursor.execute("select ID from play_ers where ID="+str(id))
              g=my_cursor.fetchone()
              g="+".join(g)
              
              if confidence>65:
                  cv2.putText(img,f"ID:{g}",(x,y-95),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                  cv2.putText(img,f"NAME:{j}",(x,y-65),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                  cv2.putText(img,f"ROLL_NO:{l}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                  cv2.putText(img,f"STREAM:{p}",(x,y-3),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                  self.attendence(g,j,l,p)
                 # i=i+1
                 # self.cc=1
                #webbrowser.open("https://docs.python.org")
                
              else:
                  cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                  cv2.putText(img,"UNKNOWN FACE",(x,y-6),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                  self.cc=0
                  
              coord=[x,y,w,y]
              
          return coord
        def recognize(img,clf,faceCascade):
             coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
             return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        
        while True: 
             ret, img=video_cap.read()
             img=recognize(img,clf,faceCascade)
             cv2.imshow("Welcome To face Recognition",img)
             #n=n+1
             if cv2.waitKey(1)==13:
               break
             #  if  self.cc==1:
                #  webbrowser.open("https://6984-110-224-18-253.in.ngrok.io")
                 # break
              # else :
                # break
            
        video_cap.release()
        cv2.destroyAllWindows()
        
        
if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()
