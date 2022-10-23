from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import tkinter
import cv2
from time import strftime
import os
import csv
from tkinter import filedialog
from datetime import datetime

mydata=[]
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
    #variable
        self.var_att_id=StringVar()
        self.var_nam_id=StringVar()
        self.var_gen_id=StringVar()
        self.var_play_id=StringVar()
        self.var_time_id=StringVar()
        self.var_date_id=StringVar()
        self.var_attt_id=StringVar()
        
    
        img=Image.open(r"college_images\ft.jpg")
        img=img.resize((650,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lb2=Label(self.root,image=self.photoimg)
        f_lb2.place(x=0,y=0,width=650,height=200)
        
        img1=Image.open(r"college_images\SM.jpg")
        img1=img1.resize((750,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=650,y=0,width=600,height=200)
        
        img3=Image.open(r"college_images\LG.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_mg=Label(self.root,image=self.photoimg3)
        bg_mg.place(x=0,y=130,width=1530,height=710)
        
        #b1=Button(self.root,text="EXIT",cursor="hand2",font=("bold"),bg="cyan")
        #b1.place(x=1200,y=85,width=100,height=20)
        
        title_lbl=Label(bg_mg,text="ATTENDENCE DETAILS ",font=("times new roman",35,"bold"),bg="Blue",fg="red")
        title_lbl.place(x=0,y=0,width=1330,height=45)
        
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text= string)
            lbl.after(1000,time)
            
        lbl = Label(title_lbl,font=("time new roman",10,"bold"),background="black",foreground="red")
        lbl.place(x=0,y=0,width=90,height=50)
        time()
        
        main_frame=Frame(bg_mg,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1480,height=600)
        #Left
        
       # Left_frame=LabelFrame(main_frame,bd=2,bg="skyblue",relief=RIDGE,text="PLAYER ATTENDENCE",font=("times new roman",12,"bold"))
       # Left_frame.place(x=10,y=10,width=650,height=450)
        
      #  img_left=Image.open(r"college_images\CF.jpg")
      #  img_left=img_left.resize((650,100),Image.ANTIALIAS)
      #  self.photoimg_left=ImageTk.PhotoImage(img_left)
        
       # f_lbl=Label(Left_frame,image=self.photoimg_left)
       # f_lbl.place(x=0,y=0,width=650,height=100)
        
       # left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="Darkgreen")
       # left_inside_frame.place(x=0,y=110,width=660,height=480)
        #lable entry
        #id
     #   PLAYER_ID_LABLE=Label(left_inside_frame,text="DATE",font=("times new roman",13,"bold"))
     #   PLAYER_ID_LABLE.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
     #   PLAYER_ID_ENTRY=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_date_id,font=("times new roman",13,"bold"))
     #   PLAYER_ID_ENTRY.grid(row=0,column=3,padx=10,pady=10,sticky=W)
        #NAME
     #   PLAYER_NAME_LABLE=Label(left_inside_frame,text="PLAYER'S NAME",font=("times new roman",13,"bold"))
      #  PLAYER_NAME_LABLE.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
       # PLAYER_NAME_ENTRY=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_nam_id,font=("times new roman",13,"bold"))
       # PLAYER_NAME_ENTRY.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #GENDER
       # PLAYER_GENTER_LABLE=Label(left_inside_frame,text="GENDER",font=("times new roman",13,"bold"))
       # PLAYER_GENTER_LABLE.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        #PLAYER_GENTER_ENTRY=ttk.Entry(PER_frame,textvariable=self.var_Gender,width=18,font=("times new roman",13,"bold"))
        #PLAYER_GENTER_ENTRY.grid(row=1,column=1,padx=10,pady=5,sticky=W)
       # g_combo=ttk.Combobox(left_inside_frame,width=16,textvariable=self.var_gen_id,font=("times new roman",13,"bold"))
       # g_combo["values"]=("Male","Female","Other")
        #g_combo.current(0)
        #g_combo.grid(row=3,column=1,padx=10,pady=10,sticky=W)
        #date
       # PLAYER_DATE_LABLE=Label(left_inside_frame,text="ATTENDENCE ID",font=("times new roman",13,"bold"))
       # PLAYER_DATE_LABLE.grid(row=5,column=0,padx=10,pady=5,sticky=W)
        
     #   PLAYER_DATE_ENTRY=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_att_id,font=("times new roman",13,"bold"))
     #   PLAYER_DATE_ENTRY.grid(row=5,column=1,padx=10,pady=5,sticky=W)
        #roll
     #   PLAYER_roll_LABLE=Label(left_inside_frame,text="PLAYING ROLL",font=("times new roman",13,"bold"))
      #  PLAYER_roll_LABLE.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
       # PLAYER_roll_ENTRY=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_play_id,font=("times new roman",13,"bold"))
        #PLAYER_roll_ENTRY.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        #time
       # PLAYER_time_LABLE=Label(left_inside_frame,text="TIME",font=("times new roman",13,"bold"))
       # PLAYER_time_LABLE.grid(row=5,column=2,padx=10,pady=5,sticky=W)
        
       # PLAYER_time_ENTRY=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_time_id,font=("times new roman",13,"bold"))
       # PLAYER_time_ENTRY.grid(row=5,column=3,padx=10,pady=5,sticky=W)
        
        #status
      #  PLAYER_GENTER_LABLE=Label(left_inside_frame,text="STATUS",font=("times new roman",13,"bold"))
      #  PLAYER_GENTER_LABLE.grid(row=7,column=0,padx=10,pady=5,sticky=W)
        
        #PLAYER_GENTER_ENTRY=ttk.Entry(PER_frame,textvariable=self.var_Gender,width=18,font=("times new roman",13,"bold"))
        #PLAYER_GENTER_ENTRY.grid(row=1,column=1,padx=10,pady=5,sticky=W)
      #  g_combo=ttk.Combobox(left_inside_frame,width=16,textvariable=self.var_attt_id,font=("times new roman",13,"bold"))
      #  g_combo["values"]=("Present","Absent")
      #  g_combo.current(0)
       # g_combo.grid(row=7,column=1,padx=10,pady=10,sticky=W)
        #buttons
        
        B_frame=LabelFrame(main_frame,bd=2,bg="Darkgreen",relief=RIDGE,font=("times new roman",12,"bold"))
        B_frame.place(x=0,y=260,width=715,height=500)
        
        save_btn=Button(B_frame,text="Import csv",command=self.importcsv,width=35,height=2,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(B_frame,text="Export csv",command=self.exportcsv,width=35,height=2,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
       # Delete_btn=Button(B_frame,text="Update",width=15,height=2,font=("times new roman",13,"bold"),bg="blue",fg="white")
       # Delete_btn.grid(row=0,column=2)
        
       # Reset_btn=Button(B_frame,text="Reset",width=16,command=self.reset_data,height=2,font=("times new roman",13,"bold"),bg="blue",fg="white")
       # Reset_btn.grid(row=0,column=3)
        
        
        
        #right
      #  R_frame=LabelFrame(main_frame,bd=0,bg="white",relief=RIDGE,text="ATTENDENCE DETAILS",font=("times new roman",12,"bold"))
      #  R_frame.place(x=660,y=10,width=600,height=450)
        
        Table_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        Table_frame.place(x=5,y=5,width=1250,height=230)
        
        #scrollbar
        scroll_bar_1=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_bar_2=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.AttendenceReportTable=ttk.Treeview(Table_frame,column=("ID","NAME","ROLL_NO","STREAM","TIME","DATE","ATTENDANCE"),xscrollcommand=scroll_bar_1.set,yscrollcommand=scroll_bar_2.set)
        scroll_bar_1.pack(side=BOTTOM,fill=X)
        scroll_bar_2.pack(side=RIGHT,fill=Y)
        scroll_bar_1.config(command=self.AttendenceReportTable.xview)
        scroll_bar_2.config(command=self.AttendenceReportTable.yview)
        self.AttendenceReportTable.heading("ID",text="ATTENDANCE ID")
        self.AttendenceReportTable.heading("NAME",text="NAME")
        self.AttendenceReportTable.heading("ROLL_NO",text="ROLL_NO")
        self.AttendenceReportTable.heading("STREAM",text="STREAM")
        self.AttendenceReportTable.heading("TIME",text="TIME")
        self.AttendenceReportTable.heading("DATE",text="DATE")
        self.AttendenceReportTable.heading("ATTENDANCE",text="ATTENDANCE")
        self.AttendenceReportTable["show"]="headings"
        
        self.AttendenceReportTable.column("ID",width=100)
        self.AttendenceReportTable.column("NAME",width=200)
        self.AttendenceReportTable.column("ROLL_NO",width=100)
        self.AttendenceReportTable.column("STREAM",width=100)
        self.AttendenceReportTable.column("TIME",width=100)
        self.AttendenceReportTable.column("DATE",width=100)
        self.AttendenceReportTable.column("ATTENDANCE",width=100)
        
        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
      #  self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)
    
#fetchdata
#import
    def fetchdata(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)
    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl Files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)
#exportcsv   
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl Files","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to"+os.path.basename(fln)+"sucessfully",parent=self.root)
        except Exception as es:
             messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
   # def get_cursor(self,event=""):
   #    cursor_focus=self.AttendenceReportTable.focus()
   #    content=self.AttendenceReportTable.item(cursor_focus)
    #   data=content["values"]
       
     #  self.var_att_id.set(data[0]),
     #  self.var_nam_id.set(data[1]),
     #  self.var_gen_id.set(data[2]),
      # self.var_play_id.set(data[3]),
      # self.var_time_id.set(data[4]),
      # self.var_date_id.set(data[5]),
      # self.var_attt_id.set(data[6]),
   # def reset_data(self):
      # self.var_att_id.set(""),
      # self.var_nam_id.set(""),
      # self.var_gen_id.set("Male"),
      # self.var_play_id.set(""),
      # self.var_time_id.set(""),
      # self.var_date_id.set(""),
      # self.var_attt_id.set("Present"),
   # def update_data(self):
     # if self.var_att_id.get()=="" or self.var_nam_id.get()==""   or self.var_play_id.get()=="" or self.var_time_id.get()==""or self.var_date_id=="" :
    #    messagebox.showerror("Error","All Fields Are Require",parent=self.root)
    #  else:
    #      try:  
    #          Update=messagebox.askyesno("Update","Do you want to update this player's details ?",parent=self.root)
    #          if Update>0:
       
            
           
    
              
if __name__=="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()
