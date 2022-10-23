from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import random
from main import Face_Recognition_System
from Register import REGISTER


def main():
    win=Tk()
    app=LOGIN_WINDOW(win)
    win.mainloop()


class LOGIN_WINDOW():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        img_top=Image.open(r"college_images\dev.jpg")
        img_top=img_top.resize((1400,750),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1400,height=750)
        
        main_frame=Frame(f_lbl,bd=2,bg="black")
        main_frame.place(x=460,y=130,width=330,height=400) 
        
        img2=Image.open(r"college_images\PLNG.jpg")
        img2=img2.resize((75,75),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(main_frame,image=self.photoimg2)  
        f_lbl.place(x=0,y=0,width=330,height=75)
        
        Username=Label(main_frame,text="USERNAME",font=("times new roman",13,"bold"),fg="white",bg="black")
        Username.place(x=5,y=100)
        
        self.ENTRY=StringVar()
        self.pl=StringVar()
        self.PER_ECb=StringVar()
        self.PLAYER_ECb=StringVar()
        
        self.ENTRY=ttk.Entry(main_frame,width=34,font=("times new roman",13,"bold"))
        self.ENTRY.place(x=5,y=125)
        
        Password=Label(main_frame,text="PASSWORD",font=("times new roman",13,"bold"),fg="white",bg="black")
        Password.place(x=5,y=150)
        
        self.pl=ttk.Entry(main_frame,width=34,font=("times new roman",13,"bold"))
        self.pl.place(x=5,y=175)
        #login btn
        b1=Button(main_frame,text="LOGIN",cursor="hand2",command=self.login,font=("times new roman",10,"bold"),bg="red",fg="white")
        b1.place(x=105,y=220,width=105,height=40)
        #register
        b1=Button(main_frame,text="NEW USER REGISTER",cursor="hand2",command=self.register,font=("times new roman",12,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black")
        b1.place(x=0,y=280,width=200)
        #forgotpass
        b1=Button(main_frame,text="FORGET  PASSWORD",cursor="hand2",command=self.forgot,font=("times new roman",12,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black")
        b1.place(x=0,y=310,width=200)
        
    def register(self):
        self.new_window=Toplevel(self.root)
        self.app=REGISTER(self.new_window)
    
        
    def login(self):
        if self.ENTRY.get()=="" or self.pl.get()=="":
            messagebox.showerror("Error","All fields are require!!")
        else:
            
            conn=mysql.connector.connect(host="localhost",username="root",password="GOURAB@2002",database="facerecognition")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where EMAIL=%s and PASSWORD=%s",(
                                                                         self.ENTRY.get(),
                                                                         self.pl.get()
                                                                     ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Authority person")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            
    
    def resetpp(self):
        if self.ssq.get()=="":
            messagebox.showerror("Error","Please Enter correct answer!!",parent=self.root2)
        elif self.search_combo.get()=="Select Security Question ":
            messagebox.showerror("Error","Please Enter Sequirity Question!!",parent=self.root2)
            
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="GOURAB@2002",database="facerecognition")
            my_cursor=conn.cursor()
            Query=("select * from register where EMAIL=%s")
            value=(self.ENTRY.get(),)
            my_cursor.execute(Query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter Valid Username!!",parent=self.root2)
            else:
                Query=("update register set PASSWORD=%s where EMAIL=%s")
                value=(self.txt_newpp.get(),self.ENTRY.get())
                my_cursor.execute(Query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success"," Your password has been reset successfully")
                
                
                
                
            
            
        
         
    def forgot(self):
       if self.ENTRY.get()=="":
           messagebox.showerror("Error","Please enter the email address to reset password")
       else:
            conn=mysql.connector.connect(host="localhost",username="root",password="GOURAB@2002",database="facerecognition")
            my_cursor=conn.cursor()
            Query=("select * from register where EMAIL=%s")
            value=(self.ENTRY.get(),)
            my_cursor.execute(Query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Please Enter Valid Username!!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title=("Forgot Password")
                self.root2.geometry("370x450+410+160")
                PL=Label(self.root2,text="FORGOT PASSWORD ",font=("times new roman",20,"bold"),bg="blue",fg="red")
                PL.place(x=0,y=0,relwidth=1)
            #gangulygourab67@gmail.com
                PLAY=Label(self.root2,text="Select Security Question  : ",font=("times new roman",15,"bold"),bg="white")
                PLAY.place(x=50,y=80)
        
                self.search_combo=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.search_combo["values"]=("Select Security Question","Birth Date","Your Father Name","Birth Place")
                self.search_combo.current(0)
                self.search_combo.place(x=50,y=130,width=230)
        
                PLA=Label(self.root2,text="Security Answer : ",font=("times new roman",15,"bold"),bg="white")
                PLA.place(x=50,y=180)
        
                self.ssq=ttk.Entry(self.root2,width=19,font=("times new roman",15,"bold"))
                self.ssq.place(x=50,y=230)
                
                PLAl=Label(self.root2,text="New Password : ",font=("times new roman",15,"bold"),bg="white")
                PLAl.place(x=50,y=280)
        
                self.txt_newpp=ttk.Entry(self.root2,width=19,font=("times new roman",15,"bold"))
                self.txt_newpp.place(x=50,y=330)
                
                b=Button(self.root2,text="RESET PASSWORD",cursor="hand2",command=self.resetpp,font=("times new roman",10,"bold"),bg="red",fg="white")
                b.place(x=120,y=380,width=145,height=40)
        
            
        
            
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
        
        PLAYER=Label(R_frame,text="NAME  :",font=("times new roman",15,"bold"),bg="white")
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
                messagebox.showinfo("Success","Register Successfull",parent=self.root)
            
            
                    
        
        
if __name__=="__main__":
    main()
