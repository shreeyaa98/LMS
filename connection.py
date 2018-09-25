from tkinter import *
import sqlite3

def main():
    root=Tk()
    root.title("Registration")

Username = StringVar()
Password = StringVar()
Name = StringVar()
Designation = StringVar()
Email = StringVar()
PASSWORD = StringVar()

conn=sqlite3.connect('project.db')
cursor=conn.cursor()

frame1 = Frame(root)
frame2 = Frame(root)

def showframe(frame):
    frame.raise()

labell = Label(frame2,text="congrats")
labell.pack(padx='50',pady='50')

name=Label(frame1,text='Name')
name.grid(row=0,column=0)
Name=Entry(frame1,textvariable='Name')
Name.grid(row=0,column=2)

label1=Label(frame1,text="")
label1.grid(row=1,column=0)

username=Label(frame1,text='Username')
username.grid(row=2,column=0)
Username=Entry(frame1,textvariable='Username')
Username.grid(row=2,column=2)

label3=Label(frame1,text="")
label3.grid(row=3,column=0)

designation=Label(frame1,text='Designation')
designation.grid(row=4,column=0)
Designation=Entry(frame1,textvariable='Designation')
Designation.grid(row=4,column=2)

label5=Label(frame1,text="")
label5.grid(row=5,column=0)

password=Label(frame1,text='Password')
password.grid(row=6,column=0)
Password=Entry(frame1,textvariable='Password')
Password.grid(row=6,column=2)

label7=Label(frame1,text="")
label7.grid(row=7,column=0)

gender=Label(frame1,text='Gender')
gender.grid(row=8,column=0)
var1 = IntVar()
Checkbutton(frame1, text="male", variable=var1).grid(row=8,column=2)
var2 = IntVar()
Checkbutton(frame1, text="female", variable=var2).grid(row=8,column=3)

label9=Label(frame1,text="")
label9.grid(row=9,column=0)

email=Label(frame1,text='Email')
email.grid(row=10,column=0)
Email=Entry(frame1,textvariable='Email')
Email.grid(row=10,column=2)

label11=Label(frame1,text="")
label11.grid(row=11,column=0)

sign = Button(frame1, text="Sign Up", width=25, font=('arial', 10),command=show_frame(frame2))
sign.grid(row=12,column=1, columnspan=2)

frame1.grid(padx='100',pady="100")
root.geometry("700x700")
root.mainloop()

