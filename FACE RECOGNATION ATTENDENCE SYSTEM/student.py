
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import tkinter
from matplotlib.pyplot import get
import mysql.connector
import cv2
from time import strftime


class PLAYERS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
    #variable
        self.var_nam=StringVar()
        self.var_Id=StringVar()
        self.var_Age=StringVar()
        self.var_Gender=StringVar()
        self.var_Email=StringVar()
        self.var_Playing_roll=StringVar()
        self.var_sem=StringVar()
        self.var_stream=StringVar()
    #self.var_photo=StringVar()
    
    
        
        img=Image.open(r"G:\FACE RECOGNATION ATTENDENCE SYSTEM\college_images\facial-recognition_0.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lb2=Label(self.root,image=self.photoimg)
        f_lb2.place(x=0,y=0,width=500,height=130)
        
        img1=Image.open(r"G:\FACE RECOGNATION ATTENDENCE SYSTEM\college_images\kp.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=500,height=130)
        
        img2=Image.open(r"G:\FACE RECOGNATION ATTENDENCE SYSTEM\college_images\gettyimages-1022573162.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
            
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=800,y=0,width=500,height=130)
            
        img3=Image.open(r"G:\FACE RECOGNATION ATTENDENCE SYSTEM\college_images\CK.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_mg=Label(self.root,image=self.photoimg3)
        bg_mg.place(x=0,y=130,width=1530,height=710)
        
        #b1=Button(self.root,text="EXIT",cursor="hand2",font=("bold"),bg="cyan")
        #b1.place(x=1200,y=85,width=100,height=20)
        
        title_lbl=Label(bg_mg,text="STUDENT BASIC DETAILS ",font=("times new roman",35,"bold"),bg="darkgrey",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        b1=Button(self.root,text="EXIT",cursor="hand2",command=self.exit,font=("bold"),bg="red")
        b1.place(x=1200,y=95,width=55,height=20)
        
        main_frame=Frame(bg_mg,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text= string)
            lbl.after(1000,time)
            
        lbl = Label(title_lbl,font=("time new roman",10,"bold"),background="darkgray",foreground="blue")
        lbl.place(x=0,y=0,width=90,height=50)
        time()
        #Left
       
       
        Left_frame=LabelFrame(main_frame,bd=2,bg="yellow",relief=RIDGE,text="STUDENTS DETAILS",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=650,height=450)
        
        img_left=Image.open(r"G:\FACE RECOGNATION ATTENDENCE SYSTEM\college_images\ft.jpg")
        img_left=img_left.resize((650,100),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=10,y=10,width=650,height=100)
        
        
        
        PER_frame=LabelFrame(Left_frame,bd=0,bg="yellow",relief=RIDGE,text="BASIC DETAILS",font=("times new roman",12,"bold"))
        PER_frame.place(x=5,y=115,width=700,height=400)
        #Id
        
        PLAYER_ID_LABLE=Label(PER_frame,text="STUDENT'S ID",font=("times new roman",10,"bold"))
        PLAYER_ID_LABLE.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        PLAYER_ID_ENTRY=ttk.Entry(PER_frame,textvariable=self.var_Id,width=18,font=("times new roman",13,"bold"))
        PLAYER_ID_ENTRY.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        #name
        PLAYER_NAME_LABLE=Label(PER_frame,text="STUDENT'S NAME",font=("times new roman",10,"bold"))
        PLAYER_NAME_LABLE.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        PLAYER_NAME_ENTRY=ttk.Entry(PER_frame,textvariable=self.var_nam,width=18,font=("times new roman",13,"bold"))
        PLAYER_NAME_ENTRY.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #Age
        PLAYER_AGE_LABLE=Label(PER_frame,text="AGE",font=("times new roman",10,"bold"))
        PLAYER_AGE_LABLE.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        PLAYER_AGE_ENTRY=ttk.Entry(PER_frame,textvariable=self.var_Age,width=18,font=("times new roman",13,"bold"))
        PLAYER_AGE_ENTRY.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        
        #Gender
        PLAYER_GENTER_LABLE=Label(PER_frame,text="STUDENT'S GENDER",font=("times new roman",10,"bold"))
        PLAYER_GENTER_LABLE.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        #PLAYER_GENTER_ENTRY=ttk.Entry(PER_frame,textvariable=self.var_Gender,width=18,font=("times new roman",13,"bold"))
        #PLAYER_GENTER_ENTRY.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        g_combo=ttk.Combobox(PER_frame,textvariable=self.var_Gender,width=16,font=("times new roman",13,"bold"))
        g_combo["values"]=("Male","Female","Other")
        g_combo.current(0)
        g_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        #Passion
        PLAYER_PLAYING_ROLE_LABLE=Label(PER_frame,text="ROLL NO",font=("times new roman",10,"bold"))
        PLAYER_PLAYING_ROLE_LABLE.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        PLAYER_PLAYING_ROLE_ENTRY=ttk.Entry(PER_frame,textvariable=self.var_Playing_roll,width=18,font=("times new roman",13,"bold"))
        PLAYER_PLAYING_ROLE_ENTRY.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #Email
        PLAYER_EMAIL_ID_LABLE=Label(PER_frame,text="EMAIL_ID",font=("times new roman",10,"bold"))
        PLAYER_EMAIL_ID_LABLE.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        PLAYER_EMAIL_ID_ENTRY=ttk.Entry(PER_frame,textvariable=self.var_Email,width=18,font=("times new roman",13,"bold"))
        PLAYER_EMAIL_ID_ENTRY.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        #sem
        PLAYER_SEMESTER_LABLE=Label(PER_frame,text="SEMESTER",font=("times new roman",10,"bold"))
        PLAYER_SEMESTER_LABLE.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        PLAYER_SEMESTER_ENTRY=ttk.Entry(PER_frame,textvariable=self.var_sem,width=18,font=("times new roman",13,"bold"))
        PLAYER_SEMESTER_ENTRY.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        #stream
        PLAYER_STREAM_LABLE=Label(PER_frame,text="STREAM",font=("times new roman",10,"bold"))
        PLAYER_STREAM_LABLE.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        PLAYER_STREAM_ENTRY=ttk.Entry(PER_frame,textvariable=self.var_stream,width=18,font=("times new roman",13,"bold"))
        PLAYER_STREAM_ENTRY.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #Button frame
        B_frame=LabelFrame(PER_frame,bd=2,bg="yellow",relief=RIDGE,font=("times new roman",12,"bold"))
        B_frame.place(x=0,y=180,width=715,height=200)
        
        save_btn=Button(B_frame,text="Save",command=self.dd_data,width=15,height=2,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(B_frame,text="Update",command=self.update_data,width=15,height=2,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        Delete_btn=Button(B_frame,text="Delete",command=self.del_data,width=15,height=2,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=2)
        
        Reset_btn=Button(B_frame,text="Reset",command=self.reset_data,width=15,height=2,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=3)
        
        T_frame=LabelFrame(PER_frame,bd=2,bg="yellow",relief=RIDGE,font=("times new roman",12,"bold"))
        T_frame.place(x=0,y=225,width=715,height=100)
        
        Take_Photo_btn=Button(T_frame,command=self.generate_dataset,text="Take Photo",width=65,height=3,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Take_Photo_btn.grid(row=1,column=0)
        #Update_Photo_btn=Button(T_frame,text="Update Photo",width=33,height=3,font=("times new roman",13,"bold"),bg="blue",fg="white")
        #Update_Photo_btn.grid(row=1,column=1)
        
        
        
        
        
        
        
        #Right
        R_frame=LabelFrame(main_frame,bd=0,bg="lightpink",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        R_frame.place(x=660,y=10,width=600,height=450)
        
        img_Right=Image.open(r"G:\FACE RECOGNATION ATTENDENCE SYSTEM\college_images\th.jpg")
        img_Right=img_Right.resize((650,100),Image.ANTIALIAS)
        self.photoimg_Right=ImageTk.PhotoImage(img_Right)
        
        f_lbl=Label(R_frame,image=self.photoimg_Right)
        f_lbl.place(x=10,y=10,width=600,height=100)
        
        SR_frame=LabelFrame(R_frame,bd=2,bg="white",relief=RIDGE,text="Searching System",font=("times new roman",12,"bold"))
        SR_frame.place(x=5,y=120,width=600,height=70)
        
        PLAYER_NAME_LABLE=Label(SR_frame,text="Search By:",font=("times new roman",13,"bold"),bg="green")
        PLAYER_NAME_LABLE.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        self.var_combo=StringVar()
        search_combo=ttk.Combobox(SR_frame,textvariable=self.var_combo,font=("times new roman",10,"bold"),state="readonly",width="15")
        search_combo["values"]=("Select","Age","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        self.var_search=StringVar()
        SEARCH_ENTRY=ttk.Entry(SR_frame,textvariable=self.var_search,width=18,font=("times new roman",10,"bold"))
        SEARCH_ENTRY.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(SR_frame,command=self.search,text="Search",width=11,height=1,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)
        
        ShowAll_btn=Button(SR_frame,command=self.fetch_data,text="ShowAll",width=11,height=1,font=("times new roman",10,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4,padx=4)
        
        Table_frame=Frame(R_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=5,y=210,width=580,height=210)
        
        scroll_bar_1=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_bar_2=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.player=ttk.Treeview(Table_frame,column=("ID","NAME","AGE","GENDER","EMAIL ID","ROLL_NO","SEMESTER","STREAM"),xscrollcommand=scroll_bar_1.set,yscrollcommand=scroll_bar_2.set)
        scroll_bar_1.pack(side=BOTTOM,fill=X)
        scroll_bar_2.pack(side=RIGHT,fill=Y)
        scroll_bar_1.config(command=self.player.xview)
        scroll_bar_2.config(command=self.player.yview)
        
        self.player.heading("ID",text="ID")
        self.player.heading("NAME",text="NAME")
        self.player.heading("AGE",text="AGE")
        self.player.heading("GENDER",text="GENDER")
        self.player.heading("EMAIL ID",text="EMAIL ID")
        self.player.heading("ROLL_NO",text="ROLL_NO")
        self.player.heading("SEMESTER",text="SEMESTER")
        self.player.heading("STREAM",text="STREAM")
        self.player["show"]="headings"
        
        self.player.column("ID",width=200)
        self.player.column("NAME",width=200)
        self.player.column("AGE",width=200)
        self.player.column("GENDER",width=200)
        self.player.column("EMAIL ID",width=200)
        self.player.column("ROLL_NO",width=200)
        self.player.column("SEMESTER",width=200)
        self.player.column("STREAM",width=200)
        
        self.player.pack(fill=BOTH,expand=1)
        self.player.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
#function
    def dd_data(self):
       if self.var_nam.get()=="" or self.var_Id.get()=="" or self.var_Gender.get()==""  or self.var_Age.get()=="" or self.var_Email.get()=="" or self.var_Playing_roll.get()=="" or self.var_sem.get()==""  or self.var_stream.get()=="" :
        messagebox.showerror("Error","All Fields Are Require",parent=self.root)
       else:
            try:
               messagebox.showinfo("success","Sucessfully Completed ",parent=self.root)
               conn=mysql.connector.connect(host="localhost",username="root",password="GOURAB@2002",database="facerecognition")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into play_ers values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                   self.var_Id.get(),
                                   self.var_nam.get(),
                                   self.var_Age.get(),
                                   self.var_Gender.get(),
                                   self.var_Email.get(),
                                   self.var_Playing_roll.get(),
                                   self.var_sem.get(),
                                   self.var_stream.get()))
    
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("Success","Player details has been added Sucessfully",parent=self.root)
            except Exception as es:
             messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
        
    #Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="GOURAB@2002",database="facerecognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from play_ers")
        data=my_cursor.fetchall()
               
        if len(data)!=0:
            self.player.delete(*self.player.get_children())
            for i in data:
                self.player.insert("",END,values=i)
            conn.commit()
        conn.close()
        
#getcursor
    def get_cursor(self,event=""):
       cursor_focus=self.player.focus()
       content=self.player.item(cursor_focus)
       data=content["values"]
       
       self.var_Id.set(data[0]),
       self.var_nam.set(data[1]),
       self.var_Age.set(data[2]),
       self.var_Gender.set(data[3]),
       self.var_Email.set(data[4]),
       self.var_Playing_roll.set(data[5]),
       self.var_sem.set(data[6]),
       self.var_stream.set(data[7])
       
#update
    def update_data(self):
      if self.var_nam.get()=="" or self.var_Id.get()=="" or self.var_Gender.get()==""  or self.var_Age.get()=="" or self.var_Email.get()=="" or self.var_Playing_roll.get()=="" or self.var_sem.get()==""  or self.var_stream.get()==""   :
        messagebox.showerror("Error","All Fields Are Require",parent=self.root)
      else:
          try:  
              Update=messagebox.askyesno("Update","Do you want to update this player's details ?",parent=self.root)
              if Update>0:
                  conn=mysql.connector.connect(host="localhost",username="root",password="GOURAB@2002",database="facerecognition")
                  my_cursor=conn.cursor()
                  my_cursor.execute("Update play_ers set ID=%s, NAME=%s,GENDER=%s,EMAIL=%s,ROLL_NO=%s,SEMESTER=%s,STREAM=%s where AGE=%s",(
                                                                                                          self.var_Id.get(),
                                                                                                          self.var_nam.get(),
                                                                                                          self.var_Gender.get(),
                                                                                                          self.var_Email.get(),
                                                                                                          self.var_Playing_roll.get(),
                                                                                                          self.var_sem.get(),
                                                                                                          self.var_stream.get(),
                                                                                                          self.var_Age.get()
                                     
                                                                                                          
                                                                                                          ))
                                  
                                    
                  
       
       
              else :
                  if not Update:
                      return
              messagebox.showinfo("Sucess","Student details sucessfully updated",parent=self.root)   
              conn.commit()
              self.fetch_data()
              conn.close()
          except EXCEPTION as es:
              messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
#delete
    def del_data(self):
       if self.var_Age.get()=="":
           messagebox.showerror("Error","Age mustbe Require",parent=self.root)
           
       else:
          try:
              delete=messagebox.askyesno("Player Delete Page","Do you want to delete this player?",parent=self.root)
              if delete>0:
                  conn=mysql.connector.connect(host="localhost",username="root",password="GOURAB@2002",database="facerecognition")
              
                  my_cursor=conn.cursor()
                  sql="Delete from play_ers where AGE=%s"
                  val=(self.var_Age.get(),)
                  my_cursor.execute(sql,val)
              else:
                  if not delete:
                      return
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("Delete","Sucessfully Deleted",parent=self.root)
          except EXCEPTION as es:
              messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
#Reset
    def reset_data(self):
       self.var_Id.set("")
       self.var_nam.set(""),
       self.var_Age.set("")
       self.var_Gender.set("Male"),
       self.var_Email.set(""),
       self.var_Playing_roll.set(""),
       self.var_sem.set(""),
       self.var_stream.set(""),
       
       
#Take Photo Sample
    def generate_dataset(self):
        if self.var_nam.get()=="" or self.var_Id.get()=="" or self.var_Gender.get()==""  or self.var_Age.get()=="" or self.var_Email.get()=="" or self.var_Playing_roll.get()=="" or self.var_sem.get()==""  or self.var_stream.get()=="" :
          messagebox.showerror("Error","All Fields Are Require",parent=self.root)
        else:
           try:  
              conn=mysql.connector.connect(host="localhost",username="root",password="GOURAB@2002",database="facerecognition")
              my_cursor=conn.cursor()
              my_cursor.execute("select * from play_ers")
              myresult=my_cursor.fetchall()
              id=0
              for x in myresult:
                  id=id+1
                                  
                  
              my_cursor.execute("update play_ers set  NAME=%s,AGE=%s,GENDER=%s,EMAIL=%s,ROLL_NO=%s,SEMESTER=%s,STREAM=%s  where ID=%s",(
                                                                                                          self.var_Age.get(),
                                                                                                          self.var_nam.get(),
                                                                                                          self.var_Gender.get(),
                                                                                                          self.var_Email.get(),
                                                                                                          self.var_Playing_roll.get(),
                                                                                                          self.var_sem.get(),
                                                                                                          self.var_stream.get(),
                                                                                                          self.var_Id.get()==id+1
                                                                                                          
                                                                                                           ))
              conn.commit()
              self.fetch_data()
              self.reset_data()
              conn.close()
#loadpredefind data on face from opencv
              face_class=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
              
              def face_cropped(img):
                  gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                  faces=face_class.detectMultiScale(gray,1.3,5)
                  
                  for (x,y,w,h) in faces:
                      face_cropped=img[y:y+h,x:x+w]
                      return face_cropped
                  
              cap=cv2.VideoCapture(0)
              imd_id=0
              while True:
                  ret,my_frame=cap.read()
                  if face_cropped(my_frame) is not None:
                      imd_id+=1
                      face=cv2.resize(face_cropped(my_frame),(450,450))
                      face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                      file_name_path="data/user."+str(id)+"."+str(imd_id)+".jpg"
                      cv2.imwrite(file_name_path,face)
                      cv2.putText(face,str(imd_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                      cv2.imshow("Crooped Face",face)
                  
                  if cv2.waitKey(1)==13 or int(imd_id)==50:
                      break
           
              cap.release()
              cv2.destroyAllWindows
              messagebox.showinfo("Result","Generating data sets completed",parent=self.root)
           except EXCEPTION as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)        
            
    def search(self):
        if self.var_search.get()  ==""or self.var_combo.get() =="" :
            messagebox.showerror("Error","Please select option",parent=self.root) 
        else:
            try:    
                conn=mysql.connector.connect(host="localhost",username="root",password="GOURAB@2002",database="facerecognition")
                my_cursor=conn.cursor()  
                my_cursor.execute("select * from play_ers where "+str(self.var_combo.get())+" LIKE '%"+str(self.var_search.get())+"%'") 
                data=my_cursor.fetchall() 
                if len(data)!=0:
                    self.player.delete(*self.player.get_children())
                    for i in data:
                        self.player.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except EXCEPTION as es:
             messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("PLAYERS","Are you sure to exit this page?",parent=self.root)
        if  self.exit >0:
            self.root.destroy()
        else:
            return                        
                                    
        
           
    
              
if __name__=="__main__":
    root=Tk()
    obj=PLAYERS(root)
    root.mainloop()
