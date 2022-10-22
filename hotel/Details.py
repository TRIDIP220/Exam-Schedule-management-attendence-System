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



class Details:
    def __init__(self,root):
        self.root=root
        self.root.title("EXAM-SCHEDULE management system")
        self.root.geometry("1295x550+230+220")

 #----------------------------------------------------Title--------------------------------- 

        title = Label(self.root , text= 'Details' ,font=("times new roman",18,"bold") ,bg="blue" ,fg="gold" ,relief = RIDGE)
        title.place(x=0,y=0 , width=1295 , height = 50)




      #---------------------------------------------Label Frame-------------------------------------------
        labelframeleft = LabelFrame(self.root , bd=2 ,relief= RIDGE ,text="Fill Details" ,font=("times new roman",20,"bold"),padx=2 ,bg="pink")
        labelframeleft.place(x=5 , y = 50 ,width=540 ,height= 350)

        FLOOR =Label(labelframeleft ,text="FLOOR-NO",font=("arial",10,"bold"),padx=2 ,pady=6,bg="pink") 
        FLOOR.grid(row=1 , column=0 ,sticky=W)
        self.var_floor = StringVar()
        textFLOOR= ttk.Entry(labelframeleft ,textvariable = self.var_floor,width=29 ,font=("arial",13,"bold"))
        textFLOOR.grid(row=1 ,column= 1)


        ROOM =Label(labelframeleft ,text="ROOM",font=("arial",10,"bold"),padx=2 ,pady=6,bg="pink") 
        ROOM.grid(row=2 , column=0 ,sticky=W)
        self.var_room = StringVar()
        textROOM= ttk.Entry(labelframeleft ,textvariable = self.var_room ,width=29 ,font=("arial",13,"bold"))
        textROOM.grid(row=2 ,column= 1)


        BENCH =Label(labelframeleft ,text="BENCH",font=("arial",10,"bold"),padx=2 ,pady=6,bg="pink") 
        BENCH.grid(row=3 , column=0 ,sticky=W)
        self.var_bench = StringVar()
        textBENCH= ttk.Entry(labelframeleft ,textvariable = self.var_bench,width=29 ,font=("arial",13,"bold"))
        textBENCH.grid(row=3 ,column= 1)


        #------------------------------------ADD ALL-BUTTONS---------------------------------------------------
        btn_frame= Frame(labelframeleft ,bd=2 , relief=RIDGE ,bg="orange")
        btn_frame.place(x=0 , y=200 ,width=380 ,height = 30)


        button_add = Button(btn_frame ,text="Add"  ,command=self.add_data ,width=12,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,cursor="hand2")
        button_add.grid(row=0 , column=0 ,pady=1)

        button_update = Button(btn_frame ,text="Update" ,command = self.update ,width=12,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,cursor="hand2")
        button_update.grid(row=0 , column=1 ,pady=1)
  

        button_Delete= Button(btn_frame ,text="Delete",command = self.mDelete,width=12,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,cursor="hand2")
        button_Delete.grid(row=0 , column=2 ,pady=1)


        button_reset = Button(btn_frame ,text="Reset",command = self.reset,width=12,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,cursor="hand2")
        button_reset.grid(row=0 , column=3 ,pady=1)


        #--------------------------------------Table frame search---------------------------------------

        Tabframe = LabelFrame(self.root , bd=2 ,relief= RIDGE ,text="View details and search system" ,font=("times new roman",12,"bold"),padx=2 )
        Tabframe.place(x=600 , y = 50 ,width=500 ,height= 350)
    

        scroll_x = ttk.Scrollbar(Tabframe ,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Tabframe ,orient=VERTICAL)

        self.all_table=ttk.Treeview(Tabframe ,column =("Floor" ,"Room" ,"Bench-no"),xscrollcommand=scroll_x.set ,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM ,fill=X)
        scroll_y.pack(side=RIGHT ,fill=Y)
        scroll_x.config(command=self.all_table.xview)
        scroll_y.config(command=self.all_table.yview)


        self.all_table=ttk.Treeview(Tabframe ,column =("Floor" ,"Room"  ,"Bench-no"),xscrollcommand=scroll_x.set ,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM ,fill=X)
        scroll_y.pack(side=RIGHT ,fill=Y)
        scroll_x.config(command=self.all_table.xview)
        scroll_y.config(command=self.all_table.yview)

       
        self.all_table.heading("Floor",text="Floor")
        self.all_table.heading("Room",text="Room")
        self.all_table.heading("Bench-no",text="BenchNo")
        self.all_table["show"] ="headings"



       
        self.all_table.column("Floor",width=100)
        self.all_table.column("Room",width=100)
        self.all_table.column("Bench-no",width=100)
        self.all_table.pack(fill=BOTH ,expand=1)
        self.all_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

#-----------------------------------ADD DATABASE----------------------------------------------------
    def add_data(self):
        if self.var_bench.get()=="" or self.var_floor.get()=="" or self.var_room.get()=="" :
            messagebox.showerror("Error","All the fields are required",parent=self.root)
        else:
            try:
                con = mysql.connector.connect(host="localhost",user="root",password="123456",database="management",)
                my_cursor = con.cursor()
                my_cursor.execute("""insert into  details values(%s,%s,%s)""",(
                                                                                        self.var_floor.get(),
                                                                                        self.var_room.get(),
                                                                                        self.var_bench.get(),
                                                                                        

                                                                                            ),)
                messagebox.showinfo("Success","Custor details has been registered",parent=self.root)
                con.commit()
                self.fetch_data()
                con.close()
               
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)


      #---------------FOR BINDING PURPOSE -------------------
    def get_cursor(self,event=""):
        cursor_row = self.all_table.focus()
        content = self.all_table.item(cursor_row)
        row = content["values"]
        self.var_floor.set(row[0])
        self.var_room.set(row[1])
        self.var_bench.set(row[2])
     

      #--------------------update----------------
    def update(self):
         if self.var_bench.get()=="":
                messagebox.showerror("Error","All the fields are required",parent=self.root)

         else:
            con = mysql.connector.connect(host ="localhost" ,user="root" ,password="123456",database="management",)
            my_cursor = con.cursor()
            my_cursor.execute("update details set Floor=%s,Room=%s where Bench=%s",(
            
              
                                                                                             
                                                                                             self.var_floor.get(),
                                                                                             self.var_room.get(),
                                                                                             self.var_bench.get()
                                                                                          
            
            
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
             query = "delete from details where Bench=%s"
             value =(self.var_bench.get(),)
             my_cursor.execute(query ,value)

        else:
            if not mDelete:
                return

        con.commit()
        self.fetch_data()
        con.close()

     #------------------------------Reset-------------------------
    def reset(self): 
         
        self.var_floor.set(""),
        self.var_room.set(""),
        self.var_bench.set("")



#----------------------------------------Def fetch data----------------------------------------------=
    def fetch_data(self):
        con = mysql.connector.connect(host ="localhost" ,user="root" ,password="123456",database="management",)
        my_cursor = con.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows) !=0:
            self.all_table.delete(*self.all_table.get_children())
            for i in rows:
                 self.all_table.insert("",END,values=i)
            con.commit()
        con.close()




       




if __name__ == "__main__":
    root = Tk()
    obj = Details(root)
    root.mainloop()
