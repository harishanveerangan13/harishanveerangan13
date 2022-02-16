import pymysql
import tkinter as tk
from tkinter.messagebox import showinfo

conx = pymysql.connect(
    host='localhost',
    user='root',
    password="",
    db='harish',
)
cur = conx.cursor()

WIN = tk.Tk()
WIN.geometry('500x600')
WIN.title("Registration Form")

#
# def cws(password): #parameter and function
#     symbols = set("!#$%&()*+,-./:;=?@[]^_`{|}~") #set of symbols to look for
#     if len(password) < 9:
#         return "Too small", False
#     if len(password) > 14:
#         return "Too big", False #checks whether it's just the right size
#     if not any(c in symbols for c in password): #checks if there's no any symbol from the list in the password
#         return "No symbols", False
#     if not any(c.isalpha() for c in password): #checks if the whole password has no alphabets
#         return "No letters", False
#     if not any(c.isdigit() for c in password): #checks if there's no digits
#         return "No numbers", False
#     return "Good password", True #if it goes through all of these conditions spotless, it is a good password!


def kms(PID, LNAME, FNAME, ADD, CITY, EMAIL, PASS):
    try:
        sql = ('INSERT INTO datatype (PersonID, LastName, FirstName, Address, City, Email, Pass) VALUES (%s, %s, %s, %s, %s, %s, %s)')
        val = (PID, LNAME, FNAME, ADD, CITY, EMAIL, PASS)
        cur.execute(sql, val)
        conx.commit()
    except Exception as e:
        showinfo(title= "Error", message= e)



PID = tk.StringVar()
LNAME =  tk.StringVar()
FNAME =  tk.StringVar()
ADD =  tk.StringVar()
CITY = tk.StringVar()
EMAIL = tk.StringVar()
PASS = tk.StringVar()

PIDEntry = tk.Entry(WIN, textvariable= PID)
LPID = tk.Label(WIN, text= "Person ID", font=("Verdana", 12))

LNAMEEntry = tk.Entry(WIN, textvariable= LNAME)
LLNAME = tk.Label(WIN, text= "Last Name", font=("Verdana", 12))

FNAMEEntry = tk.Entry(WIN, textvariable= FNAME)
LFNAME = tk.Label(WIN, text= "First Name", font =("Verdana", 12))

ADDEntry = tk.Entry(WIN, textvariable= ADD)
LADD = tk.Label(WIN, text= "Address", font=("Verdana", 12))

CITYEntry = tk.Entry(WIN, textvariable= CITY)
LCITY = tk.Label(WIN, text="City", font=("Verdana", 12))

EMAILEntry = tk.Entry(WIN, textvariable= EMAIL)
LEMAIL = tk.Label(WIN, text=  "Email", font=("Verdana", 12))

PASSEntry = tk.Entry(WIN, show="*", textvariable= PASS)
LPASS = tk.Label(WIN, text= "Password", font=("Verdana", 12))

SIGNUP = tk.Button(WIN, text= "R e g i s t e r", bg= 'black', fg= 'white', width=20, command=lambda:kms(PID.get(), LNAME.get(), FNAME.get(), ADD.get(), CITY.get(), EMAIL.get(), PASS.get()))

tit = tk.Label(WIN, text="Registration Form", font=("Verdana", 24))


tit.place(x=75, y=0)

LPID.place(x=50, y=75)
PIDEntry.place(x=200, y=75, width=200)

LLNAME.place(x=50, y=135)
LNAMEEntry.place(x=200, y=135, width=200)

LFNAME.place(x=50, y=180)
FNAMEEntry.place(x=200, y=180, width=200)

LADD.place(x=50, y=240)
ADDEntry.place(x=200, y=240, width=200)

LCITY.place(x=50, y=300)
CITYEntry.place(x=200, y=300, width=200)

LEMAIL.place(x=50, y=360)
EMAILEntry.place(x=200, y=360, width=200)

LPASS.place(x=50, y=420)
PASSEntry.place(x=200, y=420, width=200)

SIGNUP.place(x=175, y=500)

WIN.mainloop()