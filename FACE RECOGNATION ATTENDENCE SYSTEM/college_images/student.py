from cProfile import label
from tkinter import *
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
class PLAYERS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        img=Image.open(r"G:\FACE RECOGNATION ATTENDENCE SYSTEM\college_images\JK.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lb2=Label(self.root,image=self.photoimg)
        f_lb2.place(x=0,y=0,width=500,height=130)
        
        img1=Image.open(r"G:\FACE RECOGNATION ATTENDENCE SYSTEM\college_images\DF.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=500,height=130)
        
        img2=Image.open(r"G:\FACE RECOGNATION ATTENDENCE SYSTEM\college_images\SD.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=800,y=0,width=500,height=130)
        
        img3=Image.open(r"G:\FACE RECOGNATION ATTENDENCE SYSTEM\college_images\CK.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_mg=Label(self.root,image=self.photoimg3)
        bg_mg.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_mg,text="PLAYER BASIC DETAILS ",font=("times new roman",35,"bold"),bg="darkgrey",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_mg,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)
        #Left
       
       
        Left_frame=LabelFrame(main_frame,bd=2,bg="yellow",relief=RIDGE,text="PLAYERS DETAILS",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=650,height=450)
        
        img_left=Image.open(r"G:\FACE RECOGNATION ATTENDENCE SYSTEM\college_images\AS.jpg")
        img_left=img_left.resize((650,100),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=10,y=10,width=650,height=100)
        
        
        
        PER_frame=LabelFrame(Left_frame,bd=2,bg="yellow",relief=RIDGE,text="BASIC DETAILS",font=("times new roman",12,"bold"))
        PER_frame.place(x=5,y=130,width=700,height=300)
        #Id
        
        PLAYER_ID_LABLE=Label(PER_frame,text="PLAYER'S ID",font=("times new roman",13,"bold"))
        PLAYER_ID_LABLE.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        PLAYER_ID_ENTRY=ttk.Entry(PER_frame,width=12,font=("times new roman",13,"bold"))
        PLAYER_ID_ENTRY.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        #name
        PLAYER_NAME_LABLE=Label(PER_frame,text="PLAYER'S NAME",font=("times new roman",13,"bold"))
        PLAYER_NAME_LABLE.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        PLAYER_NAME_ENTRY=ttk.Entry(PER_frame,width=18,font=("times new roman",13,"bold"))
        PLAYER_NAME_ENTRY.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #Age
        PLAYER_AGE_LABLE=Label(PER_frame,text="AGE",font=("times new roman",13,"bold"))
        PLAYER_AGE_LABLE.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        PLAYER_AGE_ENTRY=ttk.Entry(PER_frame,width=12,font=("times new roman",13,"bold"))
        PLAYER_AGE_ENTRY.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        
        #Gender
        PLAYER_GENTER_LABLE=Label(PER_frame,text="PLAYER'S GENDER",font=("times new roman",13,"bold"))
        PLAYER_GENTER_LABLE.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        PLAYER_GENTER_ENTRY=ttk.Entry(PER_frame,width=18,font=("times new roman",13,"bold"))
        PLAYER_GENTER_ENTRY.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #Passion
        PLAYER_PLAYING_ROLE_LABLE=Label(PER_frame,text="PLAYING_ROLE",font=("times new roman",13,"bold"))
        PLAYER_PLAYING_ROLE_LABLE.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        PLAYER_PLAYING_ROLE_ENTRY=ttk.Entry(PER_frame,width=18,font=("times new roman",13,"bold"))
        PLAYER_PLAYING_ROLE_ENTRY.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #Email
        PLAYER_EMAIL_ID_LABLE=Label(PER_frame,text="EMAIL_ID",font=("times new roman",13,"bold"))
        PLAYER_EMAIL_ID_LABLE.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        PLAYER_EMAIL_ID_ENTRY=ttk.Entry(PER_frame,width=12,font=("times new roman",13,"bold"))
        PLAYER_EMAIL_ID_ENTRY.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #Button frame
        B_frame=LabelFrame(PER_frame,bd=2,bg="yellow",relief=RIDGE,font=("times new roman",12,"bold"))
        B_frame.place(x=0,y=150,width=715,height=200)
        
        save_btn=Button(B_frame,text="Save",width=15,height=2,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(B_frame,text="Update",width=15,height=2,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        Delete_btn=Button(B_frame,text="Delete",width=15,height=2,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=2)
        
        Reset_btn=Button(B_frame,text="Reset",width=15,height=2,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=3)
        
        T_frame=LabelFrame(PER_frame,bd=2,bg="yellow",relief=RIDGE,font=("times new roman",12,"bold"))
        T_frame.place(x=0,y=195,width=715,height=100)
        
        Take_Photo_btn=Button(T_frame,text="Take Photo",width=33,height=3,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Take_Photo_btn.grid(row=1,column=0)
        Update_Photo_btn=Button(T_frame,text="Update Photo",width=33,height=3,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Update_Photo_btn.grid(row=1,column=1)
        
        
        
        
        
        
        
        #Right
        R_frame=LabelFrame(main_frame,bd=2,bg="lightpink",relief=RIDGE,text="PLAYERS DETAILS",font=("times new roman",12,"bold"))
        R_frame.place(x=660,y=10,width=600,height=450)
        
        img_Right=Image.open(r"G:\FACE RECOGNATION ATTENDENCE SYSTEM\college_images\CG.jpg")
        img_Right=img_Right.resize((650,100),Image.ANTIALIAS)
        self.photoimg_Right=ImageTk.PhotoImage(img_Right)
        
        f_lbl=Label(R_frame,image=self.photoimg_Right)
        f_lbl.place(x=10,y=10,width=600,height=100)
        
        SR_frame=LabelFrame(R_frame,bd=2,bg="white",relief=RIDGE,text="Searching System",font=("times new roman",12,"bold"))
        SR_frame.place(x=5,y=120,width=600,height=70)
        
        PLAYER_NAME_LABLE=Label(SR_frame,text="Search By:",font=("times new roman",13,"bold"),bg="green")
        PLAYER_NAME_LABLE.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(SR_frame,font=("times new roman",10,"bold"),state="readonly",width="15")
        search_combo["values"]=("Select","Id_No","Age","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        SEARCH_ENTRY=ttk.Entry(SR_frame,width=18,font=("times new roman",10,"bold"))
        SEARCH_ENTRY.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(SR_frame,text="Search",width=11,height=1,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)
        
        ShowAll_btn=Button(SR_frame,text="ShowAll",width=11,height=1,font=("times new roman",10,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4,padx=4)
        
        Table_frame=Frame(R_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=5,y=210,width=580,height=210)
        
        scroll_bar_1=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_bar_2=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.player=ttk.Treeview(Table_frame,column=("Name","Age","Id No","Email Id","Gender","Playing Role","Photo"),xscrollcommand=scroll_bar_1.set,yscrollcommand=scroll_bar_2.set)
        scroll_bar_1.pack(side=BOTTOM,fill=X)
        scroll_bar_2.pack(side=RIGHT,fill=Y)
        scroll_bar_1.config(command=self.player.xview)
        scroll_bar_2.config(command=self.player.yview)
        
        self.player.heading("Name",text="Name")
        self.player.heading("Age",text="Age")
        self.player.heading("Id No",text="Id No")
        self.player.heading("Email Id",text="Email Id")
        self.player.heading("Gender",text="Gender")
        self.player.heading("Playing Role",text="Playing Role")
        self.player.heading("Photo",text="Photo")
        self.player["show"]="headings"
        
        self.player.column("Name",width=100)
        self.player.column("Age",width=100)
        self.player.column("Id No",width=100)
        self.player.column("Email Id",width=100)
        self.player.column("Gender",width=100)
        self.player.column("Playing Role",width=100)
        self.player.column("Photo",width=100)
        self.player.pack(fill=BOTH,expand=1)
        
        
if __name__=="__main__":
    root=Tk()
    obj=PLAYERS(root)
    root.mainloop()
