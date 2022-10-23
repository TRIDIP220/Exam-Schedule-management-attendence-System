from msilib.schema import ComboBox
from multiprocessing import connection
import random as rand
from sqlite3 import DatabaseError, Row
from tkinter import*
from tkinter import messagebox
from turtle import width
from webbrowser import get
from PIL import Image,ImageTk
from tkinter import ttk 
import mysql.connector
from datetime import datetime
import re
reg = re.compile(r'([0-9A-Z])+')



class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("EXAM-SCHEDULE management system")
        self.root.geometry("1295x550+230+220")


    #----------------------------------variables-------------------------------------------------
        self.var_phone=StringVar()
        self.var_Floor=StringVar()
        self.var_Room=StringVar()
        self.var_Estart=StringVar()
        self.var_Eend=StringVar()
        self.var_Bench=StringVar()
        self.var_Paid=StringVar()
        self.var_Actual=StringVar()
        self.var_Total=StringVar()

       #----------------------------------------------------Title--------------------------------- 

        title = Label(self.root , text= 'ROOM SETTING' ,font=("times new roman",18,"bold") ,bg="blue" ,fg="gold" ,relief = RIDGE)
        title.place(x=0,y=0 , width=1295 , height = 50)




      #---------------------------------------------Label Frame-------------------------------------------
        labelframeleft = LabelFrame(self.root , bd=2 ,relief= RIDGE ,text="EXAM FEES & ROOM SETTING" ,font=("times new roman",20,"bold"),padx=2 ,bg="pink")
        labelframeleft.place(x=5 , y = 50 ,width=425 ,height= 490)
       
       #---------------------------------------REGIST NO----------------------------------------
        lbl_Mobile =Label(labelframeleft ,text="Registration-no",font=("arial",10,"bold"),padx=2 ,pady=6,bg="pink") 
        lbl_Mobile.grid(row=0 , column=0 ,sticky=W)
        ent_Mobile= ttk.Entry(labelframeleft  ,textvariable=self.var_phone ,width=20 ,font=("arial",13,"bold") )
        ent_Mobile.grid(row=0 ,column= 1,sticky=W)


      #----------------Fetch data button------------------
        button_Fetch = Button(labelframeleft ,command=self.fetch_mobile ,text="Fetch" ,width=12,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,cursor="hand2")
        button_Fetch.place(x=320 , y=1)


       #---------------------------------------FLOOR NO---------------------------------------

        FLOOR =Label(labelframeleft ,text="FLOOR-NO",font=("arial",10,"bold"),padx=2 ,pady=6,bg="pink") 
        FLOOR.grid(row=1 , column=0 ,sticky=W)
        #textFLOOR= ttk.Entry(labelframeleft ,textvariable=self.var_Floor,width=29 ,font=("arial",13,"bold"))
        #textFLOOR.grid(row=1 ,column= 1)
        
        combo_FLOOR =ttk.Combobox(labelframeleft ,textvariable =self.var_Floor ,font=("arial",10,"bold"),width=24,state="readonly")
        combo_FLOOR["value"] =("1st-Floor","2nd-Floor","3rd-Floor")
        combo_FLOOR.current(0)
        combo_FLOOR.grid(row =1 , column = 1 ,padx=2)



       # --------------------------------------------ROOM NO--------------------------------------

        ROOM =Label(labelframeleft ,text="ROOM-NO",font=("arial",10,"bold"),padx=2 ,pady=6,bg="pink") 
        ROOM.grid(row=2 , column=0 ,sticky=W)
        En_ROOM =ttk.Entry(labelframeleft ,textvariable= self.var_Room ,font=("arial",10,"bold"),width=27)
        En_ROOM.grid(row =2 , column = 1)
        
        

       #------------------------------------------ Exam starting date---------------------------------------
        ExamS =Label(labelframeleft ,text="Exam starting date",font=("arial",10,"bold"),padx=2 ,pady=6,bg="pink") 
        ExamS.grid(row=4 , column=0 ,sticky=W)
        ExamS= ttk.Entry(labelframeleft ,textvariable=self.var_Estart,width=22 ,font=("arial",13,"bold"))
        ExamS.grid(row=4 ,column= 1)


       #----------------------------------------------Exam Ending date------------------------------------------
        ExamE =Label(labelframeleft ,text="Exam Ending date",font=("arial",10,"bold"),padx=2 ,pady=6,bg="pink") 
        ExamE.grid(row=5 , column=0 ,sticky=W)
        ent_ExamE= ttk.Entry(labelframeleft  ,textvariable= self.var_Eend,width=22 ,font=("arial",13,"bold"))
        ent_ExamE.grid(row=5 ,column= 1)


       #---------------------------------------BenchNO-----------------------------------------
        BENCH =Label(labelframeleft ,text="Bench-No",font=("arial",10,"bold"),padx=2 ,pady=6,bg="pink") 
        BENCH.grid(row=6 , column=0 ,sticky=W)
        #En_BENCH =ttk.Entry(labelframeleft ,textvariable=self.var_Bench ,font=("arial",13,"bold"),width=22)
        #En_BENCH.grid(row =6 , column = 1)
        con = mysql.connector.connect(host ="localhost" ,user="root" ,password="123456",database="management",)
        my_cursor = con.cursor()
        my_cursor.execute("select Bench from details")
        rows=my_cursor.fetchall()

        combo_BENCH =ttk.Combobox(labelframeleft ,textvariable =self.var_Bench ,font=("arial",10,"bold"),width=24,state="readonly")
        combo_BENCH["value"] =rows
        combo_BENCH.current(0)
        combo_BENCH.grid(row =6 , column = 1 ,padx=2)
       
  
       #---------------------------------------Paid fees---------------------------------
        paid =Label(labelframeleft ,text="Paid fees",font=("arial",10,"bold"),padx=2 ,pady=6,bg="pink") 
        paid.grid(row=7 , column=0 ,sticky=W)
        combo_paid =ttk.Entry(labelframeleft  ,textvariable= self.var_Paid,width=22 ,font=("arial",13,"bold"))
        combo_paid.grid(row =7 , column = 1)
      

       #------------------------------------------Actual fees-------------------------------------
        lbl_Actual =Label(labelframeleft ,text="Actual fees",font=("arial",10,"bold"),padx=2 ,pady=6,bg="pink") 
        lbl_Actual.grid(row=8 , column=0 ,sticky=W)
        ent_Actual= ttk.Entry(labelframeleft ,textvariable= self.var_Actual,width=22 ,font=("arial",13,"bold"))
        ent_Actual.grid(row=8 ,column= 1)


       #----------------------------------------- Remaining fees----------------------------------
        lbl_Total =Label(labelframeleft ,text="Remaining fees",font=("arial",10,"bold"),padx=2 ,pady=6 ,bg="pink") 
        lbl_Total.grid(row=9 , column=0 ,sticky=W)
        ent_Total= ttk.Entry(labelframeleft  ,textvariable=self.var_Total ,width=22 ,font=("arial",13,"bold"))
        ent_Total.grid(row=9 ,column= 1)


#------------------------------------MONEY RECEIPT----------------------------------------
        button_Money = Button(labelframeleft ,text="Money receipt",command=self.total ,width=12,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,cursor="hand2")
        button_Money.grid(row=10 , column=0 ,pady=1 ,sticky=W)


#------------------------------------ADD ALL-BUTTONS---------------------------------------------------
        btn_frame= Frame(labelframeleft ,bd=2 , relief=RIDGE ,bg="orange")
        btn_frame.place(x=0 , y=400 ,width=380 ,height = 30)


        button_add = Button(btn_frame ,text="Add" ,command=self.add_data ,width=12,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,cursor="hand2")
        button_add.grid(row=0 , column=0 ,pady=1)

        button_update = Button(btn_frame ,text="Update",command=self.update ,width=12,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,cursor="hand2")
        button_update.grid(row=0 , column=1 ,pady=1)
  

        button_Delete= Button(btn_frame ,text="Delete",command=self.mDelete,width=12,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,cursor="hand2")
        button_Delete.grid(row=0 , column=2 ,pady=1)


        button_reset = Button(btn_frame ,text="Reset",command=self.reset,width=12,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,cursor="hand2")
        button_reset.grid(row=0 , column=3 ,pady=1)
 #--------------------------------------Table frame search---------------------------------------

        Tabframe = LabelFrame(self.root , bd=2 ,relief= RIDGE ,text="View details and search system" ,font=("times new roman",12,"bold"),padx=2 )
        Tabframe.place(x=435 , y = 280 ,width=860 ,height= 260)
        
        lblsearchby = Label(Tabframe ,text="Search by" ,font=("times new roman",12,"bold"),bg="red",fg="white")
        lblsearchby.grid(row=0 , column= 0 ,sticky=W ,padx=2)

        self.search_var=StringVar()
        combo_lblsearchby =ttk.Combobox(Tabframe ,textvariable =self.search_var ,font=("arial",10,"bold"),width=24,state="readonly")
        combo_lblsearchby["value"] =("Registration")
        combo_lblsearchby.current(0)
        combo_lblsearchby.grid(row =0 , column = 1 ,padx=2)

        self.txt_search=StringVar()
        textsearch= ttk.Entry(Tabframe ,textvariable=self.txt_search,width=24 ,font=("arial",13,"bold"))
        textsearch.grid(row=0 ,column= 2,padx=2)

        search_btn = Button(Tabframe ,text="Search",command=self.search ,width=10 ,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,relief=RIDGE,cursor="hand2")
        search_btn.grid(row=0 , column=3 ,pady=1)
        
        show_btn = Button(Tabframe ,text="Show-all" ,command = self.fetch_data,width=10 ,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,relief=RIDGE,cursor="hand2")
        show_btn.grid(row=0 , column=4 ,pady=1)


         #------------------------------------table details----------------------------------------
         
        details_table = Frame(Tabframe , bd=2 , relief=RIDGE) 
        details_table.place(x=0 , y=50 ,width =860 , height=180)


        scroll_x = ttk.Scrollbar(details_table ,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table ,orient=VERTICAL)

        self.all_table=ttk.Treeview(details_table ,column =("Mobile","Floor" ,"Room" ,"Starting date" ,"Ending date" ,"Bench-no"),xscrollcommand=scroll_x.set ,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM ,fill=X)
        scroll_y.pack(side=RIGHT ,fill=Y)
        scroll_x.config(command=self.all_table.xview)
        scroll_y.config(command=self.all_table.yview)

        self.all_table.heading("Mobile",text="Mobile")
        self.all_table.heading("Floor",text="Floor")
        self.all_table.heading("Room",text="Room")
        self.all_table.heading("Starting date",text="Starting date")
        self.all_table.heading("Ending date",text="Ending date")
        self.all_table.heading("Bench-no",text="BenchNo")
        self.all_table["show"] ="headings"



        self.all_table.column("Mobile",width=100)
        self.all_table.column("Floor",width=100)
        self.all_table.column("Room",width=100)
        self.all_table.column("Starting date",width=100)
        self.all_table.column("Ending date",width=100)
        self.all_table.column("Bench-no",width=100)
        self.all_table.pack(fill=BOTH ,expand=1)
        self.all_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



        
    #---------------------------------------------DBMS-----------------------------------------
    #---------------------------------------ADD data-----------------------------------------
    def add_data(self):
        if self.var_phone.get()=="" or self.var_Floor.get()=="" or self.var_Bench.get()=="" or self.var_Room.get()=="" or self.var_Paid=="":
            messagebox.showerror("Error","All the fields are required",parent=self.root)
        else:
            try:
                con = mysql.connector.connect(host="localhost",user="root",password="123456",database="management",)
                my_cursor = con.cursor()
                my_cursor.execute("""insert into  room values(%s,%s,%s,%s,%s,%s)""",(
                                                                                        self.var_phone.get(),
                                                                                        self.var_Floor.get(),
                                                                                        self.var_Room.get(),
                                                                                        self.var_Estart.get(),
                                                                                        self.var_Eend.get(),
                                                                                        self.var_Bench.get(),
                                                                                        

                                                                                            ),)
                messagebox.showinfo("Success","Custor details has been registered",parent=self.root)
                con.commit()
                self.fetch_data()
                con.close()
               
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)

    #-----------------fetching procedure------------------------------------------------------------------
    def fetch_data(self):
        con = mysql.connector.connect(host ="localhost" ,user="root" ,password="123456",database="management",)
        my_cursor = con.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows) !=0:
            self.all_table.delete(*self.all_table.get_children())
            for i in rows:
                 self.all_table.insert("",END,values=i)
            con.commit()
        con.close()

    #---------------FOR BINDING PURPOSE -------------------
    def get_cursor(self,event=""):
        cursor_row = self.all_table.focus()
        content = self.all_table.item(cursor_row)
        row = content["values"]
        self.var_phone.set(row[0])
        self.var_Floor.set(row[1])
        self.var_Room.set(row[2])
        self.var_Estart.set(row[3])
        self.var_Eend.set(row[4])
        self.var_Bench.set(row[5])



    #--------------------update----------------
    def update(self):
         if self.var_phone.get()=="":
                messagebox.showerror("Error","All the fields are required",parent=self.root)

         else:
            con = mysql.connector.connect(host ="localhost" ,user="root" ,password="123456",database="management",)
            my_cursor = con.cursor()
            my_cursor.execute("update room set Floor=%s,Room=%s,ExamStart=%s,ExamEnd=%s,Bench=%s where Mobile=%s",(
            
              
                                                                                             
                                                                                             self.var_Floor.get(),
                                                                                             self.var_Room.get(),
                                                                                             self.var_Estart.get(),
                                                                                             self.var_Eend.get(),
                                                                                             self.var_Bench.get(),
                                                                                             self.var_phone.get()
            
            
                                                                                        ) )
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Update","Customer data has been updated successfully",parent=self.root)


#------------------------------Delete-------------------------
    def mDelete(self):
        mDelete = messagebox.askyesno("Exam schedule management system","Do you want to delete this student",parent=self.root)
        if mDelete>0:
             con = mysql.connector.connect(host ="localhost" ,user="root" ,password="123456",database="management",)
             my_cursor = con.cursor()
             query = "delete from room where Mobile=%s"
             value =(self.var_phone.get(),)
             my_cursor.execute(query ,value)

        else:
            if not mDelete:
                return

        con.commit()
        self.fetch_data()
        con.close()


    #-------------------------------Reset------------------

    def reset(self): 
        self.var_Floor.set("")
        self.var_Room.set("")
        self.var_Estart.set("")
        self.var_Eend.set("")
        self.var_Bench.set("")
        self.var_phone.set("")
        self.var_Actual.set("")
        self.var_Total.set("")
        self.var_Paid.set("")



    #-----------------Searchinfg details-------------------------------------
    def search(self):
        con = mysql.connector.connect(host ="localhost" ,user="root" ,password="123456",database="management",)
        my_cursor = con.cursor()
        my_cursor.execute("select * from room where "+str(self.search_var.get()) +" LIKE '%"+str(self.txt_search.get())+"%'")
         
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.all_table.delete(*self.all_table.get_children())

            for i in rows:
                self.all_table.insert("",END,values=i)

            con.commit()
            con.close()

       
#--------------------------------------Fetch all data through phone number---------------------------------
    def fetch_mobile(self):
        if self.var_phone.get() =="" or not re.fullmatch(reg, self.var_phone.get()):
            messagebox.showerror("ERROR","Please enter the Registration number",parent=self.root)

        else:
            #-----------------------------------------------FETCH NAME-----------------------------------
             con = mysql.connector.connect(host ="localhost" ,user="root" ,password="123456",database="management",)
             my_cursor = con.cursor()
             query =("select Name from customer where Registration=%s")
             value = (self.var_phone.get(),)
             my_cursor.execute(query ,value)
             row = my_cursor.fetchone()

             if row == None:
                    messagebox.showerror("Error","This Registration not found",parent=self.root)
             else:
                    con.commit()
                    con.close()

                    showDataframe =Frame(self.root,bd=4,relief=RIDGE,padx=2)
                    showDataframe.place(x=450 , y=55,width = 300 ,height = 180)

                    lblname = Label(showDataframe ,text="Name:",font=("arial",12,"bold"))
                    lblname.place(x=0 , y=0)

                    lbl = Label(showDataframe ,text =row[0] ,font=("arial",12,"bold"))
                    lbl.place(x=80 , y=2)

#------------------------------------------------FETCH GENDER---------------------------------------
                    con = mysql.connector.connect(host ="localhost" ,user="root" ,password="123456",database="management",)
                    my_cursor = con.cursor()
                    query =("select Gender from customer where Registration=%s")
                    value = (self.var_phone.get(),)
                    my_cursor.execute(query ,value)
                    row = my_cursor.fetchone()



                    lblGender = Label(showDataframe ,text="Gender:",font=("arial",12,"bold"))
                    lblGender.place(x=0 , y=30)

                    lbl2 = Label(showDataframe ,text =row ,font=("arial",12,"bold"))
                    lbl2.place(x=80 , y=30)



#-------------------------------------------------------FETCH SEM---------------------------------------
                    con = mysql.connector.connect(host ="localhost" ,user="root" ,password="123456",database="management",)
                    my_cursor = con.cursor()
                    query =("select Nationality from customer where Registration=%s")
                    value = (self.var_phone.get(),)
                    my_cursor.execute(query ,value)
                    row = my_cursor.fetchone()




                    lblGender = Label(showDataframe ,text="Sem:",font=("arial",12,"bold"))
                    lblGender.place(x=0 , y=60)

                    lbl2 = Label(showDataframe ,text =row ,font=("arial",12,"bold"))
                    lbl2.place(x=80 , y=60)


#-------------------------------------------------------FETCH SUBJECT---------------------------------------
                    con = mysql.connector.connect(host ="localhost" ,user="root" ,password="123456",database="management",)
                    my_cursor = con.cursor()
                    query =("select Address from customer where Registration=%s")
                    value = (self.var_phone.get(),)
                    my_cursor.execute(query ,value)
                    row = my_cursor.fetchone()




                    lblGender = Label(showDataframe ,text="Subject:",font=("arial",12,"bold"))
                    lblGender.place(x=0 , y=90)

                    lbl2 = Label(showDataframe ,text =row ,font=("arial",12,"bold"))
                    lbl2.place(x=80 , y=90)

#-------------------------------------------------------FETCH Date---------------------------------------
                    con = mysql.connector.connect(host ="localhost" ,user="root" ,password="123456",database="management",)
                    my_cursor = con.cursor()
                    query =("select idnumber from customer where Registration=%s")
                    value = (self.var_phone.get(),)
                    my_cursor.execute(query ,value)
                    row = my_cursor.fetchone()




                    lblGender = Label(showDataframe ,text="Date:",font=("arial",12,"bold"))
                    lblGender.place(x=0 , y=120)

                    lbl2 = Label(showDataframe ,text =row ,font=("arial",12,"bold"))
                    lbl2.place(x=80 , y=120)


#-------------------------------------------------------FETCH Time---------------------------------------
                    con = mysql.connector.connect(host ="localhost" ,user="root" ,password="123456",database="management",)
                    my_cursor = con.cursor()
                    query =("select idproof from customer where Registration=%s")
                    value = (self.var_phone.get(),)
                    my_cursor.execute(query ,value)
                    row = my_cursor.fetchone()




                    lblGender = Label(showDataframe ,text="Time:",font=("arial",12,"bold"))
                    lblGender.place(x=0 , y=150)

                    lbl2 = Label(showDataframe ,text =row[0] ,font=("arial",12,"bold"))
                    lbl2.place(x=80 , y=150)


    def total(self):
        Start = self.var_Estart.get()
        End = self.var_Eend.get()
        Start = datetime.strptime(Start,"%d/%m/%y")
        End = datetime.strptime(End,"%d/%m/%y")
        q1= 200
        p = self.var_Paid.get()
        if int(p) > (abs(End-Start).days * q1):
            messagebox.showerror("ERROR" ,"Paid is greater than Actual")
        else:
            self.var_Actual.set(abs(End-Start).days * q1)
            self.var_Total.set((abs(End-Start).days * q1)- int(p))
    


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()

