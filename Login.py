from tkinter import *
import sqlite3

root = Tk()
root.title("LMS")
USERNAME = StringVar()
PASSWORD = StringVar()


def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Python: Simple Login Application")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))



def login():
    conn = sqlite3.connect("Project.db")
    cur = conn.cursor()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        label3.config(text="Please complete the required field!", fg="red")
    else:
        cur.execute("SELECT * FROM emp_login")
        rows=cur.fetchall()
        print(rows)
        s=int(USERNAME.get())
        p=PASSWORD.get()
        for row in rows:
            if row[0]==s and row[1]==p:
                HomeWindow()
                USERNAME.set("")
                PASSWORD.set("")
                label3.config(text="SUCCESFUL")
                break
        else:
            label3.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    conn.commit()
    conn.close()



frame = Frame(root)

label1 = Label(frame, text="Username", font=('arial', 10))
label1.grid(row=0, sticky="e", pady=25)
entry1 = Entry(frame, textvariable=USERNAME, font=10)
entry1.grid(row=0, column=1)
label2 = Label(frame, text="Password", font=('arial', 10))
label2.grid(row=1, sticky="e")
entry2 = Entry(frame, show='*',textvariable=PASSWORD, font=10)
entry2.grid(row=1, column=1)
button1 = Button(frame, text="Login", width=25, font=('arial', 10), command=login)
button1.grid(pady=25, row=3, columnspan=2)
label3 = Label(frame)
label3.grid(row=2, sticky='e', pady=25)
frame.pack(padx=150, pady=150)
root.geometry("700x700")
root.mainloop()







