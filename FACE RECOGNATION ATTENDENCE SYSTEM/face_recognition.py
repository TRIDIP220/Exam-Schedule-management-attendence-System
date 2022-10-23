
from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
import cv2



class Face_recognition:
    def __init__(self,root):
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
        img_side=Image.open(r"college_images\DK.jpg")
        img_side=img_side.resize((750,600),Image.ANTIALIAS)
        self.photoimg_side=ImageTk.PhotoImage(img_side)
        
        f_lbl=Label(self.root,image=self.photoimg_side)
        f_lbl.place(x=0,y=50,width=750,height=600)
        
        #bottom
        b1=Button(self.root,text="FACE DETECTOR",cursor="hand2",command=self.face_recog,font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1.place(x=950,y=500,width=250,height=40)
        
        
        #Face Recognition
    def face_recog(self):
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
              
              #my_cursor.execute("select AGE from play_ers where ID="+str(id))
             # i=my_cursor.fetchone()
              #i="+".join(i)
              
              my_cursor.execute("select NAME from play_ers where ID="+str(id))
              j=my_cursor.fetchone()
              j="+".join(j)
              
              my_cursor.execute("select GENDER from play_ers where ID="+str(id))
              l=my_cursor.fetchone()
              l="+".join(l)
              
              my_cursor.execute("select PLAYING_ROLL from play_ers where ID="+str(id))
              p=my_cursor.fetchone()
              p="+".join(p)
            
              if confidence>77:
                 # cv2.putText(img,f"AGE:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                  cv2.putText(img,f"NAME:{j}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                  cv2.putText(img,f"GENDER:{l}",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                  cv2.putText(img,f"PLAYING_ROLL:{p}",(x,y-6),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
              else:
                  cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                  cv2.putText(img,"UNKNOWN FACE",(x,y-6),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
              coord=[x,y,w,y]
              
          return coord
        def recognize(img,clf,faceCascade):
             coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
             return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(1)
        
        while True:
            ret, img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
                   
if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()