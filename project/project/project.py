from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import os
import re
root=Tk()
root.title("LIBRARY MANAGEMENT")
root.geometry("1350x700+0+0")
img=PhotoImage(file="E:\\suraj phone\project\project\global-library-main_0_0-1.png")
img1=PhotoImage(file="E:\\suraj phone\project\project\login icon.png")
img2=PhotoImage(file="E:\\suraj phone\project\project\user icon.png")
img3=PhotoImage(file="E:\\suraj phone\project\project\passw icon.png")
#variables
uname=StringVar()
passw=StringVar()
def display():
    def donothing():
        filewin=Toplevel(win)
        button=Button(filewin, text="Do nothing button")
        button.pack()
    def member():
        root=Tk()
        root.title("permission information")
        root.geometry("500x500+0+0")
        memadd=StringVar()
        mememail=StringVar()
        memmobile=IntVar()
        memname=StringVar()
        memid=IntVar()
        la=Label(root,text="member information",width=20,font=('Calibri',20,"bold"),bg="yellow",fg="red")
        la.place(x=90,y=53)
        la1=Label(root,text='MemAdd',width=20,font=('Calibri',10,"bold"),bg="yellow",fg="red")
        la1.place(x=80,y=130)
        entry1=Entry(root,textvariable=memadd)
        entry1.place(x=240,y=130)
        la2=Label(root,text='MemEmail',width=20,font=('Calibri',10,"bold"),bg="yellow",fg="red")
        la2.place(x=80,y=180)
        entry2=Entry(root,textvariable=mememail)
        entry2.place(x=240,y=180)
        la3=Label(root,text='MemMobile',width=20,font=('Calibri',10,"bold"),bg="yellow",fg="red") 
        la3.place(x=80,y=230)
        entry3=Entry(root,textvariable=memmobile)
        entry3.place(x=240,y=230)
        la4=Label(root,text='MemName',width=20,font=('Calibri',10,"bold"),bg="yellow",fg="red")
        la4.place(x=80,y=280)
        entry4=Entry(root,textvariable=memname)
        entry4.place(x=240,y=280)
        la5=Label(root,text='MemId',width=20,font=('Calibri',10,"bold"),bg="yellow",fg="red")
        la5.place(x=80,y=330)
        entry5=Entry(root,textvariable=memid)
        entry5.place(x=240,y=330)
        button=Button(root,text='Submit',width=20,bg='brown',fg='white')
        button.place(x=300,y=380)

    def book():
        root=Tk()
        root.title("permission information")
        root.geometry("500x500+0+0")
        bookdesc=StringVar()
        booktype=StringVar()
        bookid=IntVar()
        la=Label(root,text="books information",width=20,font=('Calibri',20,"bold"),bg="yellow",fg="red")
        la.place(x=90,y=53)
        la1=Label(root,text='BookDesc',width=20,font=('Calibri',10,"bold"),bg="yellow",fg="red")
        la1.place(x=80,y=130)
        entry1=Entry(root,textvariable=bookdesc)
        entry1.place(x=240,y=130)
        la2=Label(root,text='BookType',width=20,font=('Calibri',10,"bold"),bg="yellow",fg="red")
        la2.place(x=80,y=180)
        entry2=Entry(root,textvariable=booktype)
        entry2.place(x=240,y=180)
        la3=Label(root,text='Bookid',width=20,font=('Calibri',10,"bold"),bg="yellow",fg="red")
        la3.place(x=80,y=230)
        entry3=Entry(root,textvariable=bookid)
        entry3.place(x=240,y=230)
        button=Button(root,text='Submit',width=20,bg='brown',fg='white')
        button.place(x=300,y=380)

    def student():
        root=Tk()
        root.title("user information")
        root.geometry("500x500+0+0")
        stuadd=StringVar()
        stuid=IntVar()
        stuname=StringVar()
        stumobile=IntVar()
        stuemail=StringVar()
        stupass=StringVar()
        la=Label(root,text='student information',width=20,font=('Calibri',20,"bold"),bg="yellow",fg="red")
        la.place(x=90,y=53)
        la1=Label(root,text='StuAdd',width=20,font=('Calibri',10,"bold"),bg="yellow",fg="red")
        la1.place(x=80,y=130)
        entry1=Entry(root,textvariable=stuadd)
        entry1.place(x=240,y=130)
        la2=Label(root,text='StuId',width=20,font=('Calibri',10,"bold"),bg="yellow",fg="red")
        la2.place(x=80,y=180)
        entry2=Entry(root,textvariable=stuid)
        entry2.place(x=240,y=180)
        la3=Label(root,text='stuName',width=20,font=('Calibri',10,"bold"),bg="yellow",fg="red")
        la3.place(x=80,y=230)
        entry3=Entry(root,textvariable=stuname)
        entry3.place(x=240,y=230)
        la4=Label(root,text='StuMobile',width=20,font=('Calibri',10,"bold"),bg="yellow",fg="red")
        la4.place(x=80,y=280)
        entry4=Entry(root,textvariable=stumobile)
        entry4.place(x=240,y=280)
        la5=Label(root,text='StuEmail',width=20,font=('Calibri',10,"bold"),bg="yellow",fg="red")
        la5.place(x=80,y=330)
        entry5=Entry(root,textvariable=stuemail)
        entry5.place(x=240,y=330)
        la6=Label(root,text='StuPass',width=20,font=('Calibri',10,"bold"),bg="yellow",fg="red")
        la6.place(x=80,y=330)
        entry6=Entry(root,textvariable=stupass)
        entry6.place(x=240,y=330)
        button=Button(root,text='Submit',width=20,bg='brown',fg='white')
        button.place(x=300,y=380)

       




    try:
        conn=sqlite3.connect("user.db")
        c=conn.cursor()
        date1=c.execute("SELECT user_password FROM user1 WHERE user_name='"+uname.get()+"'")
        print(data1)
        if data1:
            if data1==passw.get():
                messagebox.showinfo("successful","welcome")
            else:
                messagebox.showerror("Error","password not matched")
        else:
            messagebox.showerror("Error","user not exits")
            conn.close()
    except Error as e:
        print(e)

        
    win=Tk()
    win.title("MENU WINDOW")
    win.geometry("500x500")
    win.configure(background="light blue")
    menubar= Menu(win)
    filemenu= Menu(menubar, tearoff=0)
    filemenu.add_command(label="Book",command=book)
    filemenu.add_command(label="Member",command=member)
    filemenu.add_command(label="Student",command=student)
    menubar.add_cascade(label="New", menu=filemenu)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=win.destroy)

    searchmenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Search", menu=searchmenu)

    modifymenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Modify", menu=modifymenu)

    returnmenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Return", menu=returnmenu)

    issuemenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Issue", menu=issuemenu)

    helpmenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Help", menu=helpmenu)
    win.config(menu=menubar)


cnv=Label(root,image=img)
cnv.pack()
la=Label(root,text='LOGIN PAGE',font=('Calibri',30,"bold"),bg="yellow",fg="red")
la.place(x=0,y=0,relwidth=1)
frame=Frame(root, bg="sandybrown")
frame.place(x=400,y=150)
la1=Label(frame, image=img1,bd=0)
la1.grid(row=0,columnspan=2,pady=20)
la2=Label(frame,text="USERNAME*",image=img2,compound=LEFT,font=('Calibri',15,"bold"),bg="white")
la2.grid(row=1,column=0,padx=20,pady=10)
entry=Entry(frame,bd=5,textvariable=uname,relief=GROOVE,font=("",15))
entry.grid(row=1,column=1,padx=20)
la3=Label(frame,text="PASSWORD*",image=img3,compound=LEFT,font=('Calibri',15,"bold"),bg="white")
la3.grid(row=2,column=0,padx=20,pady=10)
entry1=Entry(frame,bd=5,textvariable=passw,show="*",relief=GROOVE,font=("",15))
entry1.grid(row=2,column=1,padx=20)
btn=Button(frame,text="login",width=15,command=display, font=('Calibri',14,"bold"),bg="yellow",fg='red')
btn.grid(row=3,column=1,pady=10)

#register window
def registeration():
    window=Tk()
    window.title("registration screen")
    window.geometry("500x500")
    
    #variables
    fname=StringVar() 
    pwd=StringVar()
    confirmpwd=StringVar()
    phoneno=StringVar()
    emailid=StringVar()
    gender=IntVar()
    country=StringVar()
    category=StringVar()


    def validateallfields():
        if fname.get()==None:
            messagebox.showinfo('Information',"Please Enter FullName To Proceed")
        elif pwd.get()== None:
            messagebox.showinfo('Information',"Please Enter Password To Proceed")
        elif confirmpwd.get()==None:
            messagebox.showinfo('Information',"Please Confirm Password To Proceed")
        elif phoneno.get()==None:
            messagebox.showinfo('Information',"Please Phone Number To Proceed")
        elif len(phoneno.get())!=10:
            messagebox.showinfo('Information',"Please Enter 10 Digit Phone Number To Proceed")
        elif emailid.get()==None:
            messagebox.showinfo('Information',"Please Enter Email Id To Proceed")
        elif gender.get()==0:
            messagebox.showinfo('Information',"Please Select Gender To Proceed")
        elif country.get()==None or country.get()== "Select Your Country":
            messagebox.showinfo('Information',"Please Enter Country  To Proceed")
        
        elif confirmpwd.get()!= pwd.get():
            messagebox.showinfo('Information',"Password Mismatch")
        else:
            messagebox.showinfo('Information','User Registration Successfully')
    
                
    window.configure(background="light blue")
    baa=Label(window,text="Registration Screen",width=20,font=("bold",20),bg="light blue")
    baa.place(x=90,y=53)
    baa1=Label(window,text="FullName",width=20,font=("bold",10),bg="light blue")
    baa1.place(x=90,y=130)
    entry1=Entry(window, textvariable=fname)
    entry1.place(x=240,y=130)
    baa2=Label(window,text="Password",width=20,font=("bold",10),bg="light blue")
    baa2.place(x=90,y=170)
    entry2=Entry(window,show="*",textvariable=pwd)
    entry2.place(x=240,y=170)
    baa3=Label(window,text="Comfirm Password",width=20,font=("bold",10),bg="light blue")
    baa3.place(x=90,y=210)
    entry3=Entry(window,show="*",textvariable=confirmpwd)
    entry3.place(x=240,y=210)
    baa4=Label(window,text="Phone No",width=20,font=("bold",10),bg="light blue")
    baa4.place(x=90,y=250)
    entry4=Entry(window,textvariable=phoneno)
    entry4.place(x=240,y=250)
    baa5=Label(window,text="Email",width=20,font=("bold",10),bg="light blue")
    baa5.place(x=90,y=290)
    entry5=Entry(window,textvariable=emailid)
    entry5.place(x=240,y=290)
    baa6=Label(window,text="Gender",width=20,font=("bold",10),bg="light blue")
    baa6.place(x=90,y=330)
    baa7=Radiobutton(window,text="Male",bg="light blue",padx=5,variable=gender,value=1)
    baa7.place(x=230,y=330)
    baa8=Radiobutton(window,text="Female",bg="light blue",padx=20,variable=gender,value=2)
    baa8.place(x=290,y=330)
    baa9=Label(window,text="Country",width=20,font=("bold",10),bg="light blue")
    baa9.place(x=90,y=370)
    list1=['India','Canada','UK','Nepal','Germany'];
    droplist=OptionMenu(window,country, *list1)
    droplist.config(width=14,bg="light blue")
    country.set("Select")
    droplist.place(x=240,y=370)
    baa10_category=Label(window,text="Category",width=20,font=("bold",10),bg="light blue")
    baa10_category.place(x=90,y=410)
    baa11=Checkbutton(window,text="Gen",bg="light blue")
    baa11.place(x=230,y=410)
    baa12=Checkbutton(window,text="SC",bg="light blue")
    baa12.place(x=290,y=410)
    baa13=Checkbutton(window,text="ST",bg="light blue")
    baa13.place(x=360,y=410)
    
    def clearallfields():
        fname.set=""
        pwd.set=""
        confirmpwd.set=""
        phoneno.set=""
        emailid.set=""    
    def callnewscreen():
        window.destroy()
        os.system('project.py')
    #buttons
    btn=Button(window,text='Register',command=validateallfields,bg='dark blue',fg='white',font=('bold',10))
    btn.place(x=150,y=450)
    btn1=Button(window,text='login page',command=callnewscreen,bg='dark blue',fg='white',font=('bold',10))
    btn1.place(x=250,y=450)
    btn2=Button(window,text='clear',command=clearallfields,bg='dark blue',fg='white',font=('bold',10))
    btn2.place(x=330,y=450)
    
btn2=Button(frame,text="sign up",width=15,command=registeration, font=('Calibri',14,"bold"),bg="yellow",fg='red')
btn2.grid(row=3,column=0,pady=10)



root.mainloop()




