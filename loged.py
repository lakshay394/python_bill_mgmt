from tkinter import *
import os
from PIL import ImageTk, Image
import datetime as dt
import time
from tkinter import scrolledtext as sc_text
from tkinter import messagebox as msgbox
# =====================================================


def Exit():
    sure = msgbox.askyesno(
        "Exit", "Are you sure you want to exit?", parent=window)
    if sure == True:
        window.destroy()


date = dt.datetime.now()
time2 = time.strftime('%H:%M:%S')
time1 = ''
# fun for change value of clock


def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=f"{date:%A, %B %d, %Y}\nTime:{time2}")
    clock.after(200, tick)


def back():
    sure = msgbox.askyesno(
        "Exit", "     Are you sure\n you want to Log Out?", parent=window)
    if sure == True:
        window.withdraw()
        os.system("python main.py")
        window.destroy()


# Tk class object and properties
window = Tk()
window.title("Lakshay")
window.configure(bg='grey17')
# set width and height of screen
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.minsize(width, height)
window.wm_iconbitmap("images\\user.ico")
window.protocol("WM_DELETE_WINDOW", Exit)


# -----------------------    head lable    ---------------------- #
l1 = Label(text="Bill Management System", font=("Courier 25 bold"),
           bg="black", fg="white").pack(pady=10, fill=X)
Frame(window, width=440, bg="black", height=3).pack(fill=X)

# name,phoneno. label and entry
namevalue = StringVar()
phnovalue = StringVar()
name_label = Label(window, text="Customer-Name: ",
                   font=("Courier 20"), bg='grey17', fg="white").place(x=20, y=90)
phno_label = Label(window, text="Phone No.    : ", font=(
    "Courier 20"), bg='grey17', fg="white").place(x=20, y=150)
name_entry = Entry(window, textvariable=namevalue, font=(
    "Courier 20"), bg='grey25', borderwidth=0, fg="White").place(x=250, y=90)
phno_entry = Entry(window, textvariable=phnovalue, font=(
    "Courier 20"), bg='grey25', borderwidth=0, fg="white").place(x=250, y=150)


def name():
    t.delete("6.16", "6.70")
    t.delete("7.16", "7.70")
    global name
    global phno
    name = namevalue.get()
    phno = phnovalue.get()
    if name.isalpha() != True:
        msgbox.showinfo("Error", "please use alphabets in Customer-name")
        return None
    if phno.isdigit() != True and name.isalpha() == True:
        msgbox.showinfo("Error", "please enter numerics in Phone No.")
        return None
    else:
        if len(phno) == 10:
            t.insert(6.18, name)
            t.insert(7.18, phno)
            namevalue.set("")
            phnovalue.set("")
        else:
            msgbox.showinfo("Error", "please enter 10 digit phno.")


# name phone entr button
right_arrow = Image.open(
    "images\\right-removebg-preview.png")
right_new = right_arrow.resize((60, 50))
img_phn = ImageTk.PhotoImage(right_new)
namephnbutton = Button(window, image=img_phn, command=name, borderwidth=0, font=(
    "", 12), bg='grey17').place(x=610, y=140)

# clock
clock = Label(l1, font=("Courier 12 bold"), bg="black", fg="white")
clock.place(y=11, x=1080)

# -----------------------    back Button    ---------------------- #
photo1 = Image.open("images\left-arrow.png")
new = photo1.resize((30, 30))
img = ImageTk.PhotoImage(new)
l1 = Button(l1, image=img, command=back, borderwidth=0,
            font=("", 12), bg='black').place(x=10, y=15)


# calculate total cost
def cal_total(ev):
    totalvalue.set("")
    cost=costvalue.get()
    qty=qtyvalue.get()
    cal_total = float(cost)*float(qty)
    total_entry.insert(0, cal_total)


# -----------------------   Entry Details   ---------------------- #

left_frame = Frame(width=650, height=500, bg='grey17')

l2 = Label(left_frame, text="Enter Details", font=(
    "Courier 25 bold"), bg='grey17', fg="white").place(x=210, y=20)
Frame(left_frame, width=270, bg="black", height=2,
      background='white').place(x=210, y=60)


f1 = Frame(left_frame, bg='grey17')

item_label = Label(f1, text="Item-Name : ",
                   font=("Courier 20"), bg='grey17', fg="white")
qty_label = Label(f1, text="Quantity  : ", font=("Courier 20"),
                  bg='grey17', fg="white", anchor="w", justify="left")
cost_label = Label(f1, text="Rate      : ", font=(
    "Courier 20"), bg='grey17', fg="white", anchor="w", justify="left")
total_label = Label(f1, text="Amount    : ", font=(
    "Courier 20"), bg='grey17', fg="white")

# pack labels
item_label.grid(row=0, column=0, pady=20)
qty_label.grid(row=1, column=0, pady=20)
cost_label.grid(row=2, column=0, pady=20)
total_label.grid(row=3, column=0, pady=20)

# create tkinter variables
itemvalue = StringVar()
qtyvalue = StringVar()
costvalue = StringVar()
totalvalue = StringVar()


def show_message():
    if qtyvalue.get() == CHAR and costvalue.get == CHAR:
        msgbox.showinfo(
            'Message', 'Please enter numeric values in qty. and rate')


# create entries
item_entry = Entry(f1, textvariable=itemvalue, width=19, font=(
    "Courier 20"), borderwidth=0, bg='grey17', fg="white")
Frame(f1, width=370, bg="white").place(x=200, y=59)
qty_entry = Entry(f1, textvariable=qtyvalue, width=19, font=(
    "Courier 20"), borderwidth=0, bg='grey17', fg="white")
Frame(f1, width=370, bg="white").place(x=200, y=135)
cost_entry = Entry(f1, textvariable=costvalue, width=19, font=(
    "Courier 20"), borderwidth=0, bg='grey17', fg="white")
Frame(f1, width=370, bg="white").place(x=200, y=210)
total_entry = Entry(f1, textvariable=totalvalue, width=19, font=(
    "Courier 20"), borderwidth=0, bg='grey17', fg="white")
Frame(f1, width=370, bg="white").place(x=200, y=287)
# qty_entry.bind("<FocusIn>",message)
total_entry.bind("<FocusIn>", cal_total)

# pack entries
item_entry.grid(row=0, column=1, pady=20)
qty_entry.grid(row=1, column=1, pady=20)
cost_entry.grid(row=2, column=1, pady=20)
total_entry.grid(row=3, column=1, pady=20)
f1.place(x=70, y=90)
left_frame.place(y=180)


# variables for add_data function
a = 1
i1 = float(11.0)
i2 = float(11.3)
i3 = float(11.18)
i4 = float(11.29)
i5 = float(11.39)
total1 = 0
#  function for add data in textbox(invoice)


def add_data():
    global a
    global i1
    global i2
    global i3
    global i4
    global i5
    t.insert(i1, "                                                  \n")

    item = itemvalue.get()
    quantity = float(qtyvalue.get())
    price = float(costvalue.get())
    total = float(totalvalue.get())
    check1 = isinstance(quantity, (int, float))
    check2 = isinstance(price, (int, float))
    check3 = isinstance(total, (int, float))
    global total1
    total1 += float(total)
    print(total1)
    if (item != "" and check1 == True and check2 == True and total != '' and check3 == True):
        t.insert(i1, f"{a}.")
        t.insert(i2, item)
        t.insert(i3, quantity)
        t.insert(i4, price)
        t.insert(i5, f"{total}\n")
        a = a+1
        i1 = float(i1+1)
        i2 = float(i2+1)
        i3 = float(i3+1)
        i4 = float(i4+1)
        i5 = float(i5+1)

        itemvalue.set("")
        qtyvalue.set("")
        costvalue.set("")
        totalvalue.set("")
    else:
        msgbox.showerror(
            'Error', 'Please fill all fields and fill\nNUMERIC in Rate and Quantity fields.')


i = 1


def save_data():
    a = t.get(1.0, END)
    # name=t.get(6.14,6.30)
    # print(name)
    global i
    global name
    global phno

    with open(f"D:/project_files/{name} {phno}.txt", "w") as file:
        file.write(a)
        msgbox.showinfo(
            "Done", f"Data is saved in file \n D:/project_files/{name} {phno}.txt")
        i = i+1

# clear


def clear():
    t.delete(1.0, "end")
    t.insert(INSERT, "\t\t    Tax Invoice\n")
    t.insert(INSERT, "\t\tGuido V.R Pvt. Ltd.\n")
    t.insert(INSERT, "\t\t  Bhiwani-127021\n")
    t.insert(INSERT, "\t\tTel. No.-7404204923\n\n")
    t.insert(INSERT, "Customer Name : \n")
    t.insert(INSERT, "Mobile Number : \n")
    t.insert(INSERT, "--------------------------------------------------\n")
    t.insert(INSERT, "   Item           Qty.       Rate      Amount\n")
    t.insert(INSERT, "--------------------------------------------------\n")
    t.insert(11.0, "                                                  \n")
    global a
    global i1
    global i2
    global i3
    global i4
    global i5
    global total1
    total1 = 0
    a = 1
    i1 = float(11.0)
    i2 = float(11.3)
    i3 = float(11.18)
    i4 = float(11.29)
    i5 = float(11.39)

# total function


def total():
    global i1
    t.insert(i1, "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    next = float(i1+1)
    t.insert(next, f"                       Net Ammount  =  {total1}")


# text box
texr_frame = Frame(width=650, height=500, bg="lightyellow")
scr = Scrollbar(texr_frame)
scr.pack(side=RIGHT, fill=Y)
t = Text(texr_frame, height=23, width=50,
         yscrollcommand=scr.set, font=("Courier 15 bold"))
t.pack()
add_btn = Button(left_frame, text="Add", padx=15, pady=5, command=add_data, font=(
    "Courier 15 bold"), bg="skyblue").place(x=100, y=430)
total_btn = Button(left_frame, text="Total", padx=15, pady=5, command=total, font=(
    "Courier 15 bold"), bg="skyblue").place(x=214, y=430)
save_btn = Button(left_frame, text="Save", padx=15, pady=5, command=save_data, font=(
    "Courier 15 bold"), bg="skyblue").place(x=350, y=430)
clear_btn = Button(left_frame, text="clear", padx=15, pady=5, command=clear, font=(
    "Courier 15 bold"), bg="skyblue").place(x=473, y=430)


t.insert(INSERT, "\t\t    Tax Invoice\n")
t.insert(INSERT, "\t\tGuido V.R Pvt. Ltd.\n")
t.insert(INSERT, "\t\t  Bhiwani-127021\n")
t.insert(INSERT, "\t\tTel. No.-7404204923\n\n")
t.insert(INSERT, "Customer Name : \n")
t.insert(INSERT, "Mobile Number : \n")
t.insert(INSERT, "--------------------------------------------------\n")
t.insert(INSERT, "   Item           Qty.       Rate      Amount\n")
t.insert(INSERT, "--------------------------------------------------\n")

scr.config(command=t.yview)
texr_frame.place(x=705, y=130)

tick()
window.mainloop()
