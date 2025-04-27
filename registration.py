from tkinter import *
from tkinter import messagebox
screen=Tk()
screen.title("My Registration form")
screen.geometry("500x500")
screen.resizable(False,False)
def register():
    name=name_info.get()
    study=studied_info.get()
    age=age_info.get()
    phone=phone_info.get()
    email=email_info.get()
    address=address_info.get()

    if name=="":
        messagebox.showerror("Error","Please enter your Name")
    elif study=="":
        messagebox.showerror("Error","Please enter your Standard")
    elif age=="":
        messagebox.showerror("Error","Please enter your Age")
    elif phone=="":
        messagebox.showerror("Error","Please enter your Phone Number")
    elif email=="":
        messagebox.showerror("Error","Please enter your Email Id")
    elif address=="":
        messagebox.showerror("Error","Please enter your Address")
    else:
        Label(screen,text="Registration Successful",font="25",fg="Green").place(x=160,y=420)

    with open(name+".txt","w")as f:
        f.write("Name:"+name+"\n")
        f.write("Standard:"+study+"\n")
        f.write("Age:"+age+"\n")
        f.write("Phone Number:"+phone+"\n")
        f.write("Email ID:"+email+"\n")
        f.write("Address:"+address+"\n")

def clear():
    name_entry.delete(0,END)
    studied_entry.delete(0,END)
    age_entry.delete(0,END)
    phone_entry.delete(0,END)
    email_entry.delete(0,END)
    address_entry.delete(0,END)
Label(screen,text="Registration Form",font="ariel 20 bold",bg="yellow",fg="black").pack(fill="both")
Label(screen,text="Name",font="20").place(x=30,y=70)
Label(screen,text="Studied",font="20").place(x=30,y=120)
Label(screen,text="Age",font="20").place(x=30,y=170)
Label(screen,text="Phone Number",font="20").place(x=30,y=220)
Label(screen,text="Email Id",font="20").place(x=30,y=270)
Label(screen,text="Address",font="20").place(x=30,y=320)

name_info=StringVar()
studied_info=StringVar()
age_info=StringVar()
phone_info=StringVar()
email_info=StringVar()
address_info=StringVar()
name_entry=Entry(screen,font="10",bd=4,textvariable=name_info)
name_entry.place(x=150,y=75)
studied_entry=Entry(screen,font="10",bd=4,textvariable=studied_info)
studied_entry.place(x=150,y=120)
age_entry=Entry(screen,font="10",bd=4,textvariable=age_info)
age_entry.place(x=150,y=170)
phone_entry=Entry(screen,font="10",bd=4,textvariable=phone_info)
phone_entry.place(x=150,y=220)
email_entry=Entry(screen,font="10",bd=4,textvariable=email_info)
email_entry.place(x=150,y=270)
address_entry=Entry(screen,font="10",bd=4,textvariable=address_info)
address_entry.place(x=150,y=320)
Button(screen,text="Register",font="20",command=register).place(x=200,y=370)
Button(screen,text="Clear",font="20",command=clear).place(x=420,y=450)
mainloop()
