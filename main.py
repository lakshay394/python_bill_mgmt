# import tkinter class
import os
from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox as msgbox
import mysql.connector



def Exit():
    sure = msgbox.askyesno("Exit","Are you sure you want to exit?", parent=window)
    if sure == True:
        window.destroy()
def click():
    db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='python_project')
    c=db.cursor()

    user=usernamevalue.get()
    passw=passwordvalue.get()

    c.execute("SELECT USERNAME,PASSWORD FROM LOGIN WHERE USERNAME=%s and PASSWORD=%s",(user,passw))
    # db.commit()
    RES=c.fetchall()
    if RES == []:
        msgbox.showinfo("ERROR!","Username and Password not matched")
    elif RES[0][0]==user and RES[0][1]==passw:
        window.withdraw()
        os.system("python loged.py")
        window.destroy()
             

# Enter Button Function
def enter(event):
    db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Lakshay@123',
    database='python_project')
    c=db.cursor()

    user=usernamevalue.get()
    passw=passwordvalue.get()

    c.execute("SELECT USERNAME,PASSWORD FROM LOGIN WHERE USERNAME=%s and PASSWORD=%s",(user,passw))
    # db.commit()
    RES=c.fetchall()
    if RES == []:
        msgbox.showinfo("ERROR!","Username and Password not matched")
    elif RES[0][0]==user and RES[0][1]==passw:
        window.withdraw()
        os.system("python loged.py")
        window.destroy()


# tkinter class object
window=Tk()
window.configure(bg="grey50")
# set width and height of screen
width= window.winfo_screenwidth() 
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.minsize(width, height) 
# change icon and title of window
window.wm_iconbitmap("images\\user.ico")
window.title("Log In Page")
window.protocol("WM_DELETE_WINDOW", Exit)

# create lable and underline
head=Label(window,text="My Shop Employee Login",font=("Agency FB",38,"bold"),bg="grey50").place(x=485,y=30)
Frame(window,width=380,bg="black",height=2).place(x=510,y=100)

# lock key image
image_frame=Frame(bg="grey50")
photo1=Image.open("images\lock.png")
new=photo1.resize((500,500))
img = ImageTk.PhotoImage(new)
image_label=Label(image_frame,image=img,bg="grey50")
image_label.pack(side=RIGHT)
image_frame.pack(side=LEFT,padx=100)


# login form frame
login_frame=Frame(width=700,height=500,bg="grey50")
# sign in label
l1=Label(login_frame,text="Sign In",font="Courier 20 bold",bg="grey50").place(x=220,y=100)

# username entry
def enter_user(e):
    if usernamevalue.get()=="username(email)":
        username.delete(0,"end")
def out_user(e):     
    if usernamevalue.get()=="":
        username.configure(show="") 
        username.insert(0, "username(email)")
usernamevalue=StringVar()
username = Entry(login_frame, width=30, borderwidth=0,textvariable=usernamevalue,font="Courier 13 ",bg="grey50")
username.insert(0, "username(email)")
username.place(x=140,y=200)
username.bind("<FocusIn>", enter_user)
username.bind("<FocusOut>", out_user)
Frame(login_frame,width=300,bg="black").place(x=140,y=225)

# password entry
def enter_pasw(e):
    if passwordvalue.get()=="password":
        password.delete(0,"end")
        password.configure(show="*") 
def out_pasw(e):     
    if passwordvalue.get()=="":
        password.configure(show="") 
        password.insert(0, "password")
passwordvalue=StringVar()
password = Entry(login_frame, width=30, borderwidth=0,textvariable=passwordvalue,font="Courier 13 ",bg="grey50")
password.insert(0, "password")
password.place(x=140,y=280)
password.bind("<FocusIn>", enter_pasw)
password.bind("<FocusOut>", out_pasw)
Frame(login_frame,width=300,bg="black").place(x=140,y=305)
# function for hide button
def hide():
    password.configure(show="*") 
    Button(login_frame,text="Show",command=show,borderwidth=0,bg="grey50",font="Courier 10").place(x=400,y=280)
# function for show button
def show():
    password.configure(show="")  
    Button(login_frame,text="Hide",command=hide,borderwidth=0,bg="grey50",font="Courier 10").place(x=400,y=280)
    
# show button for password
login_btn=Button(login_frame,text="Show",command=show,borderwidth=0,bg="grey50",font="Courier 10").place(x=400,y=280)
# pack login form
login_frame.pack(side=RIGHT,padx=20)


# login Button
photo2=Image.open("images\login.png")
new1=photo2.resize((60,60))
img1 = ImageTk.PhotoImage(new1)
image_label=Label(image_frame,image=img1,bg="grey50")
login_btn=Button(login_frame,image=img1,command=click,borderwidth=0,bg="grey50").place(x=260,y=350)
window.bind('<Return>', enter)

window.mainloop()