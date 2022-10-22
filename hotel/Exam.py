
from tkinter import*
from PIL import Image,ImageTk
from student import cust_win
from Room import Roombooking
from Details import Details
import random
import mysql.connector
import os





class hotelmanagement:
    def __init__(self ,root):
        self.root =root
        self.root.title("Exam Schedule management")
        self.root.geometry("1550x800+0+0")
 # heading image
        image1 = Image.open(r"C:\Users\Dell\OneDrive\Desktop\hotel\image\hotel.jpg")
        image1 = image1.resize((1550,140) ,Image.ANTIALIAS)
        self.photoImage1 = ImageTk.PhotoImage(image1)
        lblimage = Label(self.root , image=self.photoImage1 ,bd=4 , relief=RIDGE)
        lblimage.place(x=0 , y=0 ,width=1550 ,height=140)

#logo image
        image2 =Image.open(r"C:\Users\Dell\OneDrive\Desktop\hotel\image\Hotel-2.jpg")
        image2 = image2.resize((1550,140),Image.ANTIALIAS)
        self.photoImage2 = ImageTk.PhotoImage(image2)
        lblimage = Label(self.root , image=self.photoImage2 , bd=4 ,relief = RIDGE)
        lblimage.place(x=0 , y=0 ,width=100 ,height=140)


#----------------------------variable creation----------------------



#----------------------------------Title ----------------------------

        title = Label(self.root , text= 'EXAM  SCHEDULE  MANAGEMENT' ,font=("times new roman",30,"bold") ,bg="green" ,fg="white" ,relief = RIDGE)
        title.place(x=0 , y = 140 , width=1550 , height = 50)

 #----------------------------------------------Frame---------------------
        main_frame = Frame(self.root, bd = 4 , relief= RIDGE ,bg="Orange") 
        main_frame.place(x=0 , y= 190 ,width=1550 ,height = 620)   



       



#---------------------------------------------------menu-----------------

        menu_label = Label(main_frame ,text="MENU" ,font=("times new roman",20,"bold") ,bg="pink" ,fg="Black" ,relief = RIDGE)   
        menu_label.place(x=0 , y=0 , width= 230)
#--------------------------------------btn_frame-------------------------

        btn_frame= Frame(main_frame ,bd=4 , relief=RIDGE)
        btn_frame.place(x=0 , y=35 ,width=228 ,height = 93)

        cus_btn = Button(btn_frame ,text="Student",command=self.cust_details ,width=30 ,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,relief=RIDGE,cursor="hand2")
        cus_btn.grid(row=0 , column=0 ,pady=1)

        room_btn = Button(btn_frame ,text="Room",command=self.roombooking,width=30 ,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,relief=RIDGE,cursor="hand2")
        room_btn.grid(row=1 , column=0 ,pady=1)


        details_btn = Button(btn_frame ,text="Details",command = self.Details,width=30 ,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,relief=RIDGE,cursor="hand2")
        details_btn.grid(row=2 , column=0 ,pady=1)

        #report_btn = Button(btn_frame ,text="Report",width=30 ,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,relief=RIDGE,cursor="hand2")
        #report_btn.grid(row=3 , column=0 ,pady=1)
    
        #Logout_btn = Button(btn_frame ,text="Log-out",width=30 ,font=("times new roman",10,"bold") ,bg="green" ,fg="white" ,relief=RIDGE,cursor="hand2")
        #Logout_btn.grid(row=4 , column=0 ,pady=1)
    
    def cust_details(self):
        self.new = Toplevel(self.root)
        self.app = cust_win(self.new)


    def roombooking(self):
            self.new = Toplevel(self.root)
            self.app = Roombooking(self.new)


    def Details(self):
            self.new = Toplevel(self.root)
            self.app = Details(self.new)
        



      
if __name__ == "__main__":
    root = Tk()
    obj = hotelmanagement(root)
    root.mainloop()


    def logout():
        os.system('python firstscreen.py')
