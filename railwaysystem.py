import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

login = tk.Tk()
login.title("Login")
login.geometry('900x350')
connection = sqlite3.connect('login.db')
TABLE_NAME = "loginandpass"
Login_Id = "login_id"
username = "username"
password = "password"
connection = sqlite3.connect('ciis.db')
connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + Login_Id +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   username + " TEXT, " + password + " TEXT);")

connection = sqlite3.connect('ciis.db')

TABLE_NAME1 = "railway_timing_system"

appLabel = tk.Label(login, text="Railway timing System", fg="#06a099", width=35)
appLabel.config(font=("Sylfaen", 30))
appLabel.grid(row=0, columnspan=2, padx=(10, 10), pady=(30, 0))

nameLabel = tk.Label(login, text="Enter Username : ", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10, 0),
                                                pady=(30, 0))

passLabel = tk.Label(login, text="Enter Password : ", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10, 0),
                                                pady=(30, 0))

nameEntry = tk.Entry(login, width=30)
passEntry = tk.Entry(login, show="*", width=30)

nameEntry.grid(row=1, column=1, padx=(0, 10), pady=(30, 20))
passEntry.grid(row=2, column=1, padx=(0, 10), pady=(30, 20))


def insidesis():
    global nameEntry, passEntry
    loginname = nameEntry.get()
    password = passEntry.get()
    connection = sqlite3.connect('ciis.db')
    cursor = connection.execute(
        "Select * from loginandpass where username = '" + loginname + "' and  password = '" + password + "'")
    if cursor.fetchone() is not None:
        messagebox.showinfo("Login Successfull", "Login Successfull")
        login.destroy()
        ciis()

    else:
        login.destroy()
        messagebox.showinfo("Login Failed", "Username or Password is Incorrect.")


def ciis():
    root = tk.Tk()
    root.title("CIIS")
    root.geometry('1000x1000')

    appLabel = tk.Label(root, text="Railway timing System", fg="#06a099", width=35)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.grid(row=0, columnspan=2, padx=(10, 10), pady=(30, 0))

    button0 = tk.Button(root, text="Express Train", command=groundf)
    button0.grid(row=6, column=0, pady=30)

    button1 = tk.Button(root, text="Mail Train", command=firstf)
    button1.grid(row=7, column=0, pady=30)

    Button2 = tk.Button(root, text="Super Fast Train", command=secondf)
    Button2.grid(row=8, column=0, pady=30)

    Button3 = tk.Button(root, text="Local Train", command=thirdf)
    Button3.grid(row=9, column=0, pady=30)

    Button4 = tk.Button(root, text="Metro Train", command=fourthf)
    Button4.grid(row=10, column=0, pady=30)

    Button5 = tk.Button(root, text="Mono Rail", command=fifthf)
    Button5.grid(row=11, column=0, pady=30)

    root.mainloop()


def groundf():
    groundf = tk.Tk()
    groundf.title("Express Train")
    groundf.geometry('350x350')
    button01 = tk.Button(groundf, text="Rajdhani Express", command=r001)
    button01.grid(row=6, column=0, pady=30)
    groundf.mainloop()


def firstf():
    firstf = tk.Tk()
    firstf.title("Mail Train")
    firstf.geometry('350x350')
    button11 = tk.Button(firstf, text="Punjab Mail", command=r101)
    button11.grid(row=6, column=0, pady=30)
    firstf.mainloop()


def secondf():
    secondf = tk.Tk()
    secondf.title("Super Fast ")
    secondf.geometry('350x350')
    button21 = tk.Button(secondf, text="Latur Super Fast", command=r201)
    button21.grid(row=6, column=0, pady=30)
    secondf.mainloop()


def thirdf():
    thirdf = tk.Tk()
    thirdf.title("Local Train")
    thirdf.geometry('350x350')
    button31 = tk.Button(thirdf, text="Kalyan to CST", command=r301)
    button31.grid(row=6, column=0, pady=30)
    thirdf.mainloop()


def fourthf():
    fourthf = tk.Tk()
    fourthf.title("Metro Train")
    fourthf.geometry('350x350')
    button41 = tk.Button(fourthf, text="Ghatkopar to Versova", command=r401)
    button41.grid(row=6, column=0, pady=30)
    fourthf.mainloop()


def fifthf():
    fifthf = tk.Tk()
    fifthf.title("Mono Rail")
    fifthf.geometry('350x350')
    button51 = tk.Button(fifthf, text="Chembur to Jacob circle", command=r501)
    button51.grid(row=6, column=0, pady=30)
    fifthf.mainloop()


#########################################
def r001():
    r001 = tk.Tk()
    r001.title("Rajdhani Express")
    r001.geometry('350x350')
    r001l = tk.Label(r001, text="Arival : 11:45 AM").grid(row=1, column=1)
    r001.mainloop()


#############
def r101():
    r101 = tk.Tk()
    r101.title("Punjab Mail")
    r101.geometry('350x350')
    r101l = tk.Label(r101, text="Arival : 7:50 PM").grid(row=1, column=1)
    r101.mainloop()


##########
def r201():
    r201 = tk.Tk()
    r201.title("Latur Super Fast")
    r201.geometry('350x350')
    r201l = tk.Label(r201, text="Arival : 8:30 PM").grid(row=1, column=1)
    r201.mainloop()


########
def r301():
    r301 = tk.Tk()
    r301.title("Kalyan to CST")
    r301.geometry('350x350')
    r301l = tk.Label(r301, text="7:16 AM").grid(row=1, column=1)
    r301.mainloop()


##########
def r401():
    r401 = tk.Tk()
    r401.title("Ghatkopar to Versova")
    r401.geometry('350x350')
    r401l = tk.Label(r401, text="2:45 PM").grid(row=1, column=1)
    r401.mainloop()


############
def r501():
    r501 = tk.Tk()
    r501.title("Chembur to Jacob circle")
    r501.geometry('350x350')
    r501l = tk.Label(r501, text="5:30 PM").grid(row=1, column=1)
    r501.mainloop()


######################
def signup():
    signup = tk.Tk()
    signup.title("Signup")
    appLabel = tk.Label(signup, text="Railway timing System", fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))

    username = tk.Label(signup, text="Enter Username : ", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10, 0),
                                                   pady=(30, 0))

    password = tk.Label(signup, text="Enter Password : ", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10, 0),
                                                   pady=(30, 0))

    usernameEntry = tk.Entry(signup, width=30)
    passwordEntry = tk.Entry(signup, show="*", width=30)

    usernameEntry.grid(row=1, column=1, padx=(0, 10), pady=(30, 20))
    passwordEntry.grid(row=2, column=1, padx=(0, 10), pady=(30, 20))

    submitButton = tk.Button(signup, text="Submit", width=15, command=lambda: insert(usernameEntry, passwordEntry))
    submitButton.grid(row=4, column=1)

    signup.mainloop()


def insert(usernameEntry, passwordEntry):
    user = usernameEntry.get()
    passw = passwordEntry.get()
    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + username + ", " + password + " ) VALUES ( '"
                       + user + "', '" + passw + "')")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")


loginButton = tk.Button(login, text="Login", width=15, command=lambda: insidesis())
loginButton.grid(row=6, column=0, pady=25, padx=25)
signupButton = tk.Button(login, text="Signup", width=15, command=lambda: signup())
signupButton.grid(row=6, column=1, pady=25, padx=25)
login.mainloop()
