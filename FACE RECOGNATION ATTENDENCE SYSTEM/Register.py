from sre_parse import State
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class REGISTER:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        self.var_nam=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_sequirityQ=StringVar()
        self.var_sequirityA=StringVar()
        self.var_pass=StringVar()
        self.var_conpass=StringVar()
        
        
        
        img_top=Image.open(r"college_images\hackers2.jpg")
        img_top=img_top.resize((1530,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1500,height=700)
        
        img_left=Image.open(r"college_images\password.jpg")
        img_left=img_left.resize((350,550),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=70,y=45,width=350,height=550)
        
        R_frame=Frame(self.root,bg="white")
        R_frame.place(x=420,y=45,width=600,height=550)
        
        register_lb=Label(R_frame,text="REGISTER HERE",font=("times new roman",18,"bold"),bg="White",fg="green")
        register_lb.place(x=200,y=50)
        
        PLAYER=Label(R_frame,text="Username :",font=("times new roman",15,"bold"),bg="white")
        PLAYER.place(x=30,y=100)
        
        PLAYER_E=ttk.Entry(R_frame,textvariable=self.var_nam,width=18,font=("times new roman",15,"bold"))
        PLAYER_E.place(x=155,y=100)
        
        PLAYE=Label(R_frame,text="Contact No : ",font=("times new roman",15,"bold"),bg="white")
        PLAYE.place(x=30,y=150)
        
        PLAYER_EC=ttk.Entry(R_frame,textvariable=self.var_contact,width=18,font=("times new roman",15,"bold"))
        PLAYER_EC.place(x=155,y=150)
        
        PLAYE=Label(R_frame,text="Email ID  : ",font=("times new roman",15,"bold"),bg="white")
        PLAYE.place(x=30,y=200)
        
        PLAYER_EC=ttk.Entry(R_frame,textvariable=self.var_email,width=18,font=("times new roman",15,"bold"))
        PLAYER_EC.place(x=155,y=200)
        
        PLAY=Label(R_frame,text="Select Security Question  : ",font=("times new roman",15,"bold"),bg="white")
        PLAY.place(x=30,y=250)
        
        search_combo=ttk.Combobox(R_frame,textvariable=self.var_sequirityQ,font=("times new roman",15,"bold"),state="readonly")
        search_combo["values"]=("Select Security Question","Birth Date","Your Father Name","Birth Place")
        search_combo.current(0)
        search_combo.place(x=280,y=250,width=250)
        
        PLA=Label(R_frame,text="Security Answer : ",font=("times new roman",15,"bold"),bg="white")
        PLA.place(x=30,y=300)
        
        PLAYER_ECb=ttk.Entry(R_frame,textvariable=self.var_sequirityA,width=19,font=("times new roman",15,"bold"))
        PLAYER_ECb.place(x=280,y=300)
        
        New_Password=Label(R_frame,text="Password : ",font=("times new roman",15,"bold"),bg="white")
        New_Password.place(x=30,y=350)
        
        password_Entry=ttk.Entry(R_frame,textvariable=self.var_pass,width=18,font=("times new roman",15,"bold"))
        password_Entry.place(x=205,y=350)
        
        confirm=Label(R_frame,text="Confirm Password : ",font=("times new roman",15,"bold"),bg="white")
        confirm.place(x=30,y=400)
        
        confirm_entry=ttk.Entry(R_frame,textvariable=self.var_conpass,width=18,font=("times new roman",15,"bold"))
        confirm_entry.place(x=205,y=400)
        self.var_check=IntVar()
        ck_btn=Checkbutton(R_frame,variable=self.var_check,text="I Agree the terms & conditions",font=("times new roman",13,"bold"),bg="white",offvalue=0,onvalue=1)
        ck_btn.place(x=30,y=440)
        
        #register button
        img_Right=Image.open(r"college_images\RGT.jpg")
        img_Right=img_Right.resize((100,50),Image.ANTIALIAS)
        self.photoimg_Right=ImageTk.PhotoImage(img_Right)
        b1=Button(R_frame,image=self.photoimg_Right,borderwidth=0,cursor="hand2",command=self.register,font=("times new roman",13,"bold"))
        b1.place(x=250,y=470)
        
    #Function
    def register(self):
        if self.var_nam.get()=="" or self.var_email.get()=="" or self.var_sequirityA.get()=="":
            messagebox.showerror("Error","All fields are require")
        elif self.var_pass.get()!=self.var_conpass.get():
            messagebox.showerror("Error","password & confirm Password must be same!!")
        elif  self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our terms & conditions")
        else:
            messagebox.showinfo("Success","Successfully Registered")
            conn=mysql.connector.connect(host="localhost",username="root",password="GOURAB@2002",database="facerecognition")
            my_cursor=conn.cursor()
            query=("select * from register where EMAIL=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists!!")
            else:
                my_cursor.execute("insert into register value(%s,%s,%s,%s)",(
                                                                               self.var_nam.get(),
                                                                               self.var_contact.get(),
                                                                               self.var_email.get(),
                                                                               self.var_pass.get()
                                                                                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfull")
            
            
        


        
        
        
if __name__=="__main__":
    root=Tk()
    obj=REGISTER(root)
    root.mainloop()