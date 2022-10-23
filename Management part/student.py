
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
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
reg = re.compile(r'([0-9A-Z])+')
class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("EXAM-SCHEDULE management system")
        self.root.geometry("1295x550+230+220")
    #----------------------------------------------------variable-------------------------------------
        self.var_ref=StringVar()
        x=rand.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_name=StringVar()
        self.var_Gender=StringVar()
        self.var_Reg=StringVar()
        self.var_email=StringVar()
        self.var_sem=StringVar()
        self.var_proof=StringVar()
        self.var_date=StringVar()
        self.var_subject=StringVar()
        

       #----------------------------------------------------Title--------------------------------- 

        title = Label(self.root , text= 'ADD STUDENT DETAILS' ,font=("times new roman",18,"bold") ,bg="blue" ,fg="gold" ,relief = RIDGE)
        title.place(x=0,y=0 , width=1295 , height = 50)
       
       #---------------------------------------------Frame-------------------------------------------
        labelframeleft = LabelFrame(self.root , bd=2 ,relief= RIDGE ,text="Student details" ,font=("times new roman",20,"bold"),padx=2 ,bg="violet")
        labelframeleft.place(x=5 , y = 50 ,width=425 ,height= 490)

       #---------------------------------------labels and entrys------------------------------------

       #---------------------------------------cus_ref----------------------------------------
        lbl_cus_ref =Label(labelframeleft ,text="Student reference",font=("arial",10,"bold"),padx=2 ,pady=6,bg="violet") 
        lbl_cus_ref.grid(row=0 , column=0 ,sticky=W)
        ent_ref= ttk.Entry(labelframeleft ,textvariable= self.var_ref ,width=22 ,font=("arial",13,"bold") ,state="readonly")
        ent_ref.grid(row=0 ,column= 1)


       #---------------------------------------cus name---------------------------------------

        cname =Label(labelframeleft ,text="Student name",font=("arial",10,"bold"),padx=2 ,pady=6,bg="violet") 
        cname.grid(row=1 , column=0 ,sticky=W)
        textcname= ttk.Entry(labelframeleft ,textvariable=self.var_name,width=29 ,font=("arial",13,"bold"))
        textcname.grid(row=1 ,column= 1)


       # --------------------------------------------Gender--------------------------------------

        Gender =Label(labelframeleft ,text="Gender",font=("arial",10,"bold"),padx=2 ,pady=6,bg="violet") 
        Gender.grid(row=2 , column=0 ,sticky=W)
        combo_gender =ttk.Combobox(labelframeleft ,textvariable= self.var_Gender, font=("arial",10,"bold"),width=27,state="readonly")
        combo_gender["value"] =("Male" ,"Female" ,"Others")
        combo_gender.current(0)
        combo_gender.grid(row =2 , column = 1)

        

       #------------------------------------------ Registration num---------------------------------------
        mobile =Label(labelframeleft ,text="Registration-no",font=("arial",10,"bold"),padx=2 ,pady=6,bg="violet") 
        mobile.grid(row=4 , column=0 ,sticky=W)
        ent_mobile= ttk.Entry(labelframeleft ,textvariable= self.var_Reg,width=22 ,font=("arial",13,"bold"))
        ent_mobile.grid(row=4 ,column= 1)


       #----------------------------------------------email-------------------------------------------
        email =Label(labelframeleft ,text="Email",font=("arial",10,"bold"),padx=2 ,pady=6,bg="violet") 
        email.grid(row=5 , column=0 ,sticky=W)
        ent_email= ttk.Entry(labelframeleft ,textvariable=  self.var_email ,width=22 ,font=("arial",13,"bold"))
        ent_email.grid(row=5 ,column= 1)


       #---------------------------------------Sem-----------------------------------------
        sem =Label(labelframeleft ,text="sem",font=("arial",10,"bold"),padx=2 ,pady=6,bg="violet") 
        sem.grid(row=6 , column=0 ,sticky=W)
        sem_nation =ttk.Combobox(labelframeleft ,textvariable=self.var_sem ,font=("arial",10,"bold"),width=27,state="readonly")
        sem_nation["value"] =("1st" ,"2nd" ,"3rd", "4th" ,"5th" ,"6th" ,"7th" ,"8th")
        sem_nation.current(0)
        sem_nation.grid(row =6 , column = 1)
       
  
       #---------------------------------------Time---------------------------------
        Time =Label(labelframeleft ,text="Time",font=("arial",10,"bold"),padx=2 ,pady=6,bg="violet") 
        Time.grid(row=7 , column=0 ,sticky=W)
        #combo_id =ttk.Entry(labelframeleft ,textvariable= self.var_proof ,font=("arial",10,"bold"),width=22)
        #combo_id.grid(row =7 , column = 1)
        sem_Time =ttk.Combobox(labelframeleft ,textvariable=self.var_proof ,font=("arial",10,"bold"),width=27,state="readonly")
        sem_Time["value"] =("10.00am - 11.30am" ,"12.00pm - 1.30pm" ,"2.00pm - 3.30pm", "4.00pm -5.30pm")
        sem_Time.current(0)
        sem_Time.grid(row =7 , column = 1)
       
      

       #------------------------------------------DATE-------------------------------------
        lbl_cus_ref =Label(labelframeleft ,text="date",font=("arial",10,"bold"),padx=2 ,pady=6,bg="violet") 
        lbl_cus_ref.grid(row=8 , column=0 ,sticky=W)
        ent_ref= ttk.Entry(labelframeleft ,textvariable= self.var_date,width=22 ,font=("arial",13,"bold"))
        ent_ref.grid(row=8 ,column= 1)


       #----------------------------------------- Subject----------------------------------
        lbl_cus_ref =Label(labelframeleft ,text="Subject",font=("arial",10,"bold"),padx=2 ,pady=6 ,bg="violet") 
        lbl_cus_ref.grid(row=9 , column=0 ,sticky=W)
        ent_ref= ttk.Entry(labelframeleft ,textvariable=self.var_subject ,width=22 ,font=("arial",13,"bold"))
        ent_ref.grid(row=9 ,column= 1)


    #------------------------------------------------button-------------------------------------
        btn_frame= Frame(labelframeleft ,bd=2 , relief=RIDGE ,bg="orange")
        btn_frame.place(x=0 , y=400 ,width=380 ,height = 30)


        button_add = Button(btn_frame ,text="Add" ,command=self.add_data ,width=12,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,cursor="hand2")
        button_add.grid(row=0 , column=0 ,pady=1)

        button_update = Button(btn_frame ,text="Update" ,command=self.update ,width=12,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,cursor="hand2")
        button_update.grid(row=0 , column=1 ,pady=1)
  

        button_Delete= Button(btn_frame ,text="Delete",command=self.mDelete,width=12,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,cursor="hand2")
        button_Delete.grid(row=0 , column=2 ,pady=1)


        button_reset = Button(btn_frame ,text="Reset",command=self.reset ,width=12,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,cursor="hand2")
        button_reset.grid(row=0 , column=3 ,pady=1)


    #--------------------------------------Table frame search---------------------------------------

        Tabframe = LabelFrame(self.root , bd=2 ,relief= RIDGE ,text="View details and search system" ,font=("times new roman",12,"bold"),padx=2 )
        Tabframe.place(x=435 , y = 50 ,width=860 ,height= 490)
        
        lblsearchby = Label(Tabframe ,text="Search by" ,font=("times new roman",12,"bold"),bg="red",fg="white")
        lblsearchby.grid(row=0 , column= 0 ,sticky=W ,padx=2)

        self.search_var=StringVar()
        combo_lblsearchby =ttk.Combobox(Tabframe ,textvariable =self.search_var ,font=("arial",10,"bold"),width=24,state="readonly")
        combo_lblsearchby["value"] =("Registration","Ref")
        combo_lblsearchby.current(0)
        combo_lblsearchby.grid(row =0 , column = 1 ,padx=2)

        self.txt_search=StringVar()
        textsearch= ttk.Entry(Tabframe ,textvariable=self.txt_search,width=24 ,font=("arial",13,"bold"))
        textsearch.grid(row=0 ,column= 2,padx=2)

        search_btn = Button(Tabframe ,text="Search",command=self.search ,width=10 ,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,relief=RIDGE,cursor="hand2")
        search_btn.grid(row=0 , column=3 ,pady=1)
        
        show_btn = Button(Tabframe ,text="Show-all",command=self.fetch_data ,width=10 ,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,relief=RIDGE,cursor="hand2")
        show_btn.grid(row=0 , column=4 ,pady=1)

        #------------------------------------table details----------------------------------------
         
        details_table = Frame(Tabframe , bd=2 , relief=RIDGE) 
        details_table.place(x=0 , y=50 ,width =860 , height=350)


        scroll_x = ttk.Scrollbar(details_table ,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table ,orient=VERTICAL)

        self.all_table=ttk.Treeview(details_table ,column =("ref","name" ,"Gender" ,"Registration-no" ,"email" ,"sem" ,"Time","date","subject"),xscrollcommand=scroll_x.set ,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM ,fill=X)
        scroll_y.pack(side=RIGHT ,fill=Y)
        scroll_x.config(command=self.all_table.xview)
        scroll_y.config(command=self.all_table.yview)

        self.all_table.heading("ref",text="Refer no")
        self.all_table.heading("name",text="Name")
        self.all_table.heading("Gender",text="Gender")
        self.all_table.heading("Registration-no",text="Registration-no")
        self.all_table.heading("email",text="Email")
        self.all_table.heading("sem",text="sem")
        self.all_table.heading("Time",text="Time")
        self.all_table.heading("date",text="Date")
        self.all_table.heading("subject",text="Subject")

        self.all_table["show"] ="headings"



        self.all_table.column("ref",width=100)
        self.all_table.column("name",width=100)
        self.all_table.column("Gender",width=100)
        self.all_table.column("Registration-no",width=100)
        self.all_table.column("email",width=100)
        self.all_table.column("sem",width=100)
        self.all_table.column("Time",width=100)
        self.all_table.column("date",width=100)
        self.all_table.column("subject",width=100)
        self.all_table.pack(fill=BOTH ,expand=1)
        self.all_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
#---------------------------------------------DBMS-----------------------------------------
    def add_data(self):
        if self.var_Reg.get()=="":
            messagebox.showerror("Error","All the fields are required",parent=self.root)
        elif re.fullmatch(regex, self.var_email.get()) and re.fullmatch(reg, self.var_Reg.get()):
            
            try:
                con = mysql.connector.connect(host="localhost",user="root",password="123456",database="management",)
                my_cursor = con.cursor()
                my_cursor.execute("""insert into  customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(

                                                                                            self.var_ref.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_Gender.get(),
                                                                                            self.var_Reg.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_sem.get(),
                                                                                            self.var_proof.get(),
                                                                                            self.var_date.get(),
                                                                                            self.var_subject.get(),
                                                                                            ),)
                messagebox.showinfo("Success","Student details has been registered",parent=self.root)
                con.commit()
                self.fetch_data()
                con.close()  
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)
        else:
            messagebox.showerror("Error","Email pattern (name@gmail.com) and Regitration(11-digit and Subject First capital letter",parent=self.root)

#-----------------fetching procedure------------------------------------------------------------------
    def fetch_data(self):
        con = mysql.connector.connect(host ="localhost" ,user="root" ,password="123456",database="management",)
        my_cursor = con.cursor()
        my_cursor.execute("select * from customer")
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
        self.var_ref.set(row[0])
        self.var_name.set(row[1])
        self.var_Gender.set(row[2])
        self.var_Reg.set(row[3])
        self.var_email.set(row[4])
        self.var_sem.set(row[5])
        self.var_proof.set(row[6])
        self.var_date.set(row[7])
        self.var_subject.set(row[8])

#--------------------update----------------
    def update(self):
         if self.var_mobile.get()=="":
                messagebox.showerror("Error","All the fields are required",parent=self.root)

         else:
            con = mysql.connector.connect(host ="localhost" ,user="root" ,password="123456",database="management",)
            my_cursor = con.cursor()
            my_cursor.execute("update customer set Name=%s,Gender=%s,Mobile=%s,Email=%s,Nationality=%s,idproof=%s,idnumber=%s,Address=%s where Ref=%s",(
            
              
                                                                                            self.var_name.get(),
                                                                                            self.var_Gender.get(),
                                                                                            self.var_Reg.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_sem.get(),
                                                                                            self.var_proof.get(),
                                                                                            self.var_date.get(),
                                                                                            self.var_subject.get(),
                                                                                            self.var_ref.get()
            
            
                                                                                        ) )
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Update","Student data has been updated successfully",parent=self.root)

#------------------------------Delete-------------------------
    def mDelete(self):
        mDelete = messagebox.askyesno("Exam schedule management system","Do you want to delete this student",parent=self.root)
        if mDelete>0:
             con = mysql.connector.connect(host ="localhost" ,user="root" ,password="123456",database="management",)
             my_cursor = con.cursor()
             query = "delete from customer where Ref=%s"
             value =(self.var_ref.get(),)
             my_cursor.execute(query ,value)

        else:
            if not mDelete:
                return

        con.commit()
        self.fetch_data()
        con.close()

#-------------------------------Reset------------------

    def reset(self):
        #self.var_ref.set("")
        self.var_name.set("")
        #self.var_Gender.set("")
        self.var_Reg.set("")
        self.var_email.set("")
        #self.var_sem.set("")
        #self.var_proof.set("")
        self.var_date.set("")
        self.var_subject.set("")
       
        x=rand.randint(1000, 9999)
        self.var_ref.set(str(x))


#--------------------Search----------------

    def search(self):
         con = mysql.connector.connect(host ="localhost" ,user="root" ,password="123456",database="management",)
         my_cursor = con.cursor()
         my_cursor.execute("select * from customer where "+str(self.search_var.get()) +" LIKE '%"+str(self.txt_search.get())+"%'")
         
         rows=my_cursor.fetchall()

         if len(rows)!=0:
            self.all_table.delete(*self.all_table.get_children())

            for i in rows:
                self.all_table.insert("",END,values=i)

            con.commit()
            con.close()





        




                                                                                                     
if __name__ == "__main__":
    root = Tk()
    obj = cust_win(root)
    root.mainloop()