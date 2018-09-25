from tkinter import *
import sqlite3
import re
import Cal
from datetime import *

user=""

class Welcome():
    def __init__(self,master):
        self.master=master
        self.master.geometry("700x700")
        self.master.title("WELCOME")

        self.lab1=Label(self.master , text='Welcome to the home page' , font=('arial', 20)).grid(row=0,columnspan=4)
        self.but1=Button(self.master,text='Log In',fg='blue',command=self.log).grid(row=2,column=1,columnspan=1)
        self.but2 = Button(self.master, text='Register', fg='blue', command=self.register).grid(row=2, column=3)
        self.but3 = Button(self.master, text='Quit', fg='blue', command=self.quit).grid(row=2, column=5)

    def log(self):
        root2=Toplevel(self.master)
        next = Login(root2)

    def register(self):
        root3=Toplevel(self.master)
        next1 = Register(root3)

    def quit(self):
        self.master.destroy()

class Login():
    def __init__(self,master):

        self.USERNAME=StringVar()
        self.PASSWORD=StringVar()

        self.master=master
        self.master.geometry("700x700")
        self.master.title("LOGIN")

        self.label1 = Label(self.master, text="Username", font=('arial', 10)).grid(row=0, sticky="e", pady=25)
        self.entry1 = Entry(self.master, textvariable=self.USERNAME, font=10).grid(row=0, column=1)
        self.label2 = Label(self.master, text="Password", font=('arial', 10)).grid(row=1, sticky="e")
        self.entry2 = Entry(self.master, show='*', textvariable=self.PASSWORD, font=10).grid(row=1, column=1)
        self.button1 = Button(self.master, text="Login", width=15, font=('arial', 10), command=self.login).grid(pady=25, row=3, columnspan=2)
        self.button2 = Button(self.master,text='Back',width=15,font=('arial',10),command=self.finish).grid(pady=25,row=3,column=3)


    def login(self):

        conn = sqlite3.connect("Project.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM emp_details")
        rows = cur.fetchall()
        global user
        user = self.USERNAME.get()
        print(rows)
        if self.USERNAME.get() == "" or self.PASSWORD.get() == "":
            self.label3 = Label(self.master,text="Please complete the required field!", fg="red").grid(row=2, sticky='e', pady=25)
        else:
            s=self.USERNAME.get()
            print(s)
            p=self.PASSWORD.get()
            print(p)
            for row in rows:
                if row[1]==s and row[3]==p:
                    self.USERNAME.set("")
                    self.PASSWORD.set("")
                    self.label3 = Label(self.master, text="Login Succesful", fg="red").grid(row=2,sticky='e',pady=25)
                    root4 = Toplevel(self.master)
                    next2 = HomePage(root4)

            else:
                self.label3 = Label(self.master, text="Incorrect Information!Please fill again.", fg="red").grid(row=2,sticky='e',pady=25)
                self.USERNAME.set("")
                self.PASSWORD.set("")
        conn.commit()
        conn.close()

    def finish(self):
        self.master.destroy()

class Register():
    def __init__(self,master):
        self.Username = StringVar()
        self.Password = StringVar()
        self.Name = StringVar()
        self.Designation = StringVar()
        self.Email = StringVar()
        self.Gender = StringVar()


        self.master=master
        self.master.geometry("700x700")
        self.master.title("Register")

        self.name = Label(self.master, text='Name').grid(row=0, column=0)
        self.Name1 = Entry(self.master, textvariable=self.Name).grid(row=0, column=2)

        self.label4 = Label(self.master, text="").grid(row=1, column=0)

        self.username = Label(self.master, text='Username').grid(row=2, column=0)
        self.Username1 = Entry(self.master, textvariable=self.Username).grid(row=2, column=2)

        self.label5 = Label(self.master, text="").grid(row=3, column=0)

        self.designation = Label(self.master, text='Designation').grid(row=4, column=0)
        self.Designation1 = Entry(self.master, textvariable=self.Designation).grid(row=4, column=2)

        self.label6 = Label(self.master, text="").grid(row=5, column=0)

        self.password = Label(self.master, text='Password').grid(row=6, column=0)
        self.Password1 = Entry(self.master,show='*' ,textvariable=self.Password).grid(row=6, column=2)

        self.label7 = Label(self.master, text="").grid(row=7, column=0)

        self.gender = Label(self.master, text='Gender').grid(row=8, column=0)
        self.Gender1 = Entry(self.master,textvariable=self.Gender).grid(row=8,column=2)

        self.label9 = Label(self.master, text="").grid(row=9, column=0)

        self.email = Label(self.master, text='Email').grid(row=10, column=0)
        self.Email1 = Entry(self.master, textvariable=self.Email).grid(row=10, column=2)



        self.sign = Button(self.master, text="Sign Up", width=25, font=('arial', 10), command=self.main).grid(row=12, column=1, columnspan=2)

    def main(self):
        l = ["Manager", "Executive", "Lead", "Chief"]
        lg = ['Male', 'Female']
        global user
        user = self.Username.get()
        if self.Name.get() == '' or self.Designation.get() == '' or self.Username.get() == '' or self.Password.get() == "" or self.Email.get() == "":
            self.label11 = Label(self.master, text="Fill all the columns").grid(row=11, column=0)
        else:
            if not (bool(re.match('^[a-zA-Z0-9@#$%^&*!()+_={}:"<>?;./]+$', self.Password.get())) and len(
                    self.Password.get()) >= 8):
                self.label7 = Label(self.master,
                                    text="Password must be atleast 8 characters long, Alphanumeric and contain atleast one special Character").grid(
                    row=7, column=0,columnspan=8)
            elif self.Designation.get() not in l:
                self.label6 = Label(self.master, text="Enter valid Designation").grid(row=5, column=0)
            elif self.Gender.get() not in lg:
                self.label9 = Label(self.master, text="Enter Male/Female").grid(row=9, column=0)

            else:
                try:
                    conn = sqlite3.connect("project.db")
                    cur = conn.cursor()
                    cur.execute("INSERT INTO emp_details values (?,?,?,?,?,?)", (
                    self.Name.get(), self.Username.get(), self.Designation.get(), self.Password.get(),
                    self.Gender.get(), self.Email.get()))
                    conn.commit()
                    conn.close()
                except Exception:
                    self.label11 = Label(self.master, text="Username might be taken").grid(row=11, column=0)
                else:
                    conn = sqlite3.connect("project.db")
                    cur = conn.cursor()
                    if self.Designation.get()=='Executive':
                        cur.execute("INSERT INTO emp_leaves values (?,?,?,?,?,?,?,?)", ( self.Username.get(),self.Name.get(),12,0,0,0,0,0))
                    elif self.Designation.get()=='Lead':
                        cur.execute("INSERT INTO emp_leaves values (?,?,?,?,?,?,?,?)",
                                    (self.Username.get(), self.Name.get(), 15, 0, 0, 0, 0, 0))
                    elif self.Designation.get()=='Manager':
                        cur.execute("INSERT INTO emp_leaves values (?,?,?,?,?,?,?,?)",
                                    (self.Username.get(), self.Name.get(), 18, 0, 0, 0, 0, 0))
                    else:
                        cur.execute("INSERT INTO emp_leaves values (?,?,?,?,?,?,?,?)",
                                    (self.Username.get(), self.Name.get(), 20, 0, 0, 0, 0, 0))
                    conn.commit()
                    conn.close()
                    root4 = Toplevel(self.master)
                    next2 = HomePage(root4)


class HomePage():
    def __init__(self,master):
        self.master = master
        self.master.geometry("700x700")
        self.master.title("HomePage")
        conn = sqlite3.connect("project.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM emp_details")
        rows=cur.fetchall()
        for row in rows:
            print(row)
            print(user)
            if row[1] == user:
                self.name = Label(self.master, text=row[0]).grid(row=0, column=0)
                self.username = Label(self.master, text=row[1]).grid(row=1, column=0)
                self.designation = Label(self.master, text=row[2]).grid(row=2, column=0)
                self.gender = Label(self.master, text=row[4]).grid(row=3, column=0)
                self.email = Label(self.master, text=row[5]).grid(row=4, column=0)
                self.leave = Button(self.master, text="Apply Leave", width=25, font=('arial', 10), command=self.leave).grid(row=5,column=0,columnspan=2)
            else:
                pass



    def leave(self):
        root5=Toplevel(self.master)
        next3=Leave(root5)


class Leave():
    def __init__(self,master):
        self.master = master
        self.master.geometry("700x700")
        self.master.title("Leave")

        self.from_date=StringVar()
        self.to_date=StringVar()

        self.t=('Casual','Earned','Duty','Maternal','Paternal','Unpaid')
        self.leave_option = Spinbox(self.master, values=self.t)
        self.leave_option.grid(row=0, column=1)
        #self.from_date = Button(self.master, text="FROM", width=25, font=('arial', 10), command=self.disp_cal1).grid(row=1, column=1)
        self.lab = Label(self.master, text="Enter the date in the format 'dd.mm.yyyy").grid(row=1,column=0)
        self.from1 = Label(self.master, text="FROM").grid(row=2,column=1)
        self.ent1 = Entry(self.master, width=20, bd=3,textvariable=self.from_date).grid(row=3,column=1)
        self.lab = Label(self.master, text="TO").grid(row=2,column=3)
        self.ent1 = Entry(self.master, width=20, bd=3,textvariable=self.to_date).grid(row=3, column=3)
        self.Enter=Button(self.master,text="Enter",width=25,command=self.get_dates).grid(row=4,column=0)
        self.lab2 = Label(self.master, text=" ").grid(row=5, column=1)
        self.lab3 = Label(self.master, text=" ").grid(row=6,column=1)
        #self.to_date = Button(self.master, text="TO", width=25, font=('arial', 10), command=self.disp_cal2).grid(row=1,column=2)

    def get_dates(self):
        from1=self.from_date.get()
        to=self.to_date.get()
        list1=re.findall(r'\d\d\.\d\d\.\d\d\d\d',from1)
        list2=re.findall(r'\d\d\.\d\d\.\d\d\d\d',to)
        if list1==[] or list2==[]:
            print('invalid date')
            self.lab2 = Label(self.master, text="Enter the date in the correct format").grid(row=5,column=1)


        #if not (bool(re.match('^[a-zA-Z0-9@#$%^&*!()+_={}:"<>?;./]+$', self.from_date.get())):
        l1=[int(i) for i in from1.split('.')]
        l2=[int(i) for i in to.split('.')]
        if l1[0]>1 and l1[0]<31 and l1[1]>1 and l1[1]<12:
            pass
        else:
            print('invalid date')
            self.lab2 = Label(self.master, text="Enter date in correct format").grid(row=5,column=1)

        from_date=date(l1[2],l1[1],l1[0])
        to_date=date(l2[2],l2[1],l2[0])
        leave_days=to_date-from_date
        c=leave_days.days
        print(c)
        leave_type=self.leave_option.get()
        conn = sqlite3.connect("Project.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM emp_leaves")
        rows = cur.fetchall()
        print(user)
        for row in rows:
            if row[0]==user:
                t=row
        print(t)
        print(rows)
        if leave_type=='Casual':
            if t[2]<c:
                self.lab2 = Label(self.master, text="Leaves Remaining are less than applied for").grid(row=5,column=1)
                s="Remaining Leaves:",t[2]
                self.lab3 = Label(self.master,text=s).grid(row=6,column=1)
            else:
                val=t[2]-c
                print(val)
                cur.execute("UPDATE emp_leaves SET Casual=? WHERE username=? ",(val,user))
                conn.commit()
                conn.close()
                print("updated")
                self.lab2 = Label(self.master, text="Leave approved").grid(row=5,column=1)
                s="Remaining Leaves:",val
                self.lab3 = Label(self.master, text=s).grid(row=6,column=1)
        if leave_type=='Earned':
            if t[3]<c:
                self.lab2 = Label(self.master, text="Leaves Remaining are less than applied for").grid(row=5,column=1)
                s="Remaining Leaves:",t[3]
                self.lab3 = Label(self.master, text=s).grid(row=6,column=1)
            else:
                val=t[3]-c
                print(val)
                cur.execute("UPDATE emp_leaves SET Earned=? WHERE username=? ",(val,user))
                conn.commit()
                conn.close()
                print("updated")
                self.lab2 = Label(self.master, text="Leave approved").grid(row=5,column=1)
                s="Remaining Leaves:",val
                self.lab3 = Label(self.master, text=s).grid(row=6,column=1)
        if leave_type=='Unpaid':
                cur.execute("UPDATE emp_leaves SET Unpaid=? WHERE username=? ",(c,user))
                conn.commit()
                conn.close()
                print("updated")
                self.lab2 = Label(self.master, text="Leave approved").grid(row=5,column=1)
                s="No. of Unpaid Leaves taken:",c
                self.lab3 = Label(self.master, text=s).grid(row=6,column=1)

    

def main():
    root=Tk()
    new=Welcome(root)
    root.mainloop()


if __name__ == '__main__':
    main()