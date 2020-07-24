import sqlite3
import time
import tkinter as tk
from tkinter import *

print("WELCOME TO SKDN EXPENSER TRACKER!")
time.sleep(2)
curs = sqlite3.connect('userdata.db')
conn = sqlite3.connect('expenses.db')
#registro = input("""Select 1 or 2 according to the case
#1.- Set Up Account
#2.- Log in
#""")

#create a cursor for the database
cursor = conn.cursor()
udb_cursor = curs.cursor()

def Add_exp(type):
    amount = float(input("Enter the amount:"))
    if type == "Expense":
        amount = (amount * -1)
    subtype = input("category? e.g. food, uber, salary ")
    print("")
    exp = [(type, amount, subtype)]
    cursor.executemany("INSERT INTO expenses VALUES(?,?,?)", exp)
    #commiting the database
    conn.commit()
    curs.commit()
    Main()

def Delete():
    cursor.execute("SELECT rowid, * FROM expenses")
    record = cursor.fetchall()
    print("Select the ID of the record to delete:")
    print("")
    print("ID       TYPE             AMOUNT          CATEGORY")
    print("--------------------------------------------------")
    for items in record:
        print(str(items[0]) + "\t" + items[1] + "\t\t" + " $" + str(items[2]) + "\t" + items[3])
    id_record = input("ID: ")
    if id_record == "cancelar":
        Main()
    else:
        cursor.execute("DELETE from expenses WHERE rowid =" + str(id_record))
        conn.commit()
        print("Record Deleted successfuly!")
        print("")
        time.sleep(1)
        Main()
        

def Generate():
    #query for the database
    try:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        total = []
        print("TYPE             AMOUNT          CATEGORY")
        print("-----------------------------------------")
        for items in expenses:
            print(items[0] + "\t\t" + " $"+ str(items[1]) + "\t"+ " " + items[2])
            total.append(items[1])
        savings = sum(total)
        print("-----------------------------------------")
        print("Account Total     $" + str(savings))
        print("")
        confirmation = input ("Is this correct?(y/n): ")
        confirmation.lower()
        if confirmation == "y":
            Main()
        elif confirmation == "n":
            Delete()
        else:
            print("Insert y / n")
    except:
        print("Error Occured")
def Close():
    print("Closing App...")
    #commiting the database
    conn.commit()
    curs.commit()
    #close the connection
    conn.close()
    curs.close()
    print("goodbye!")

def Main():
    main_action = input("""Select the number of the option accordingly
    1.- Add income
    2.- Add expense
    3.- Generate Summary
    4.- Erase record
    5.- Close App
    """)
    if main_action == "1":
        Add_exp("Income")
    elif main_action == "2":
        Add_exp("Expense")
    elif main_action == "3":
        Generate()
    elif main_action == "4":
        Delete()
    elif main_action == "5":
        Close()
    else:
        print("coming soon...")
    time.sleep(2)


def Set_up ():
    try:
        name = input("Enter your name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email: ")
        account = input("Enter your account name:")
        password = input("Insert password:")
        user_data = [
            (name, last_name, email, account, password)
        ]
        #creating the cursor for the user database
        udb_cursor.execute("""CREATE TABLE user_data_table (
                name TEXT,
                last_name TEXT,
                email TEXT,
                account TEXT,
                password TEXT
        )""")
        udb_cursor.executemany("INSERT INTO user_data_table VALUES(?,?,?,?,?)", user_data)
        cursor.execute("""CREATE TABLE expenses (
                type TEXT,
                amount INTEGER,
                subtype TEXT
        )""")
        #commiting the database
        conn.commit()
        curs.commit()
        Main()
    except:
        print("You are registered already!")

def Login():
    try:
        username = input("Insert email: ")
        password = input("Insert Password: ")
        udb_cursor.execute("SELECT * FROM user_data_table")
        pass_item = udb_cursor.fetchall()
        #print(pass_item)
        for passw in pass_item:
            if username == passw[2] and password == passw[4]:
                print("Log in Succesfull!")
                time.sleep(2)
                Main()
            else:
                print("username or password incorrect")
                print(passw[3])
                Login()
    except:
        print("you have not registered yet!")
        register = input("do you want to register? (y/n)")
        register.lower()
        if register == "y":
            Set_up()  
            

#if registro == "1":
#    Set_up()
#elif registro =="2":
#    Login()
#else:
#    Close()
############################################################GUI####################################
#creating a window
window = tk.Tk()
window.title("SKDN EXPENSE TRACKER")

canvas = tk.Canvas(window, width= 500 ,height = 500)

filename = PhotoImage(file = "suitcase.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

set_up_button = tk.Button(text='Login', command=Set_up, fg = 'black', bg= 'white')
canvas.create_window(200, 420, window=set_up_button)
login_button = tk.Button(text='Set up', command =Login, fg= 'black', bg='white')
canvas.create_window(300,420, window=login_button )
canvas.pack()



window.mainloop()
#adiing more elements tom my database
#gastos = [("expense",'2000'),("income",'13000'),("expense",'220')]
#cursor.executemany("INSERT INTO expensest VALUES (?,?)", gastos)





#Query the database
#cursor.execute("SELECT rowid, * FROM expensest")
#cursor.fetchone()
#cursor.fetchmany(1)
#items = cursor.fetchall()
#expenses = []
#for item in items:
#    if item[0]=="expense":
#        expenses.append(item[1])
#    else:
#        pass
#print (expenses)


#DATA BASE DATATYPE
#NULL 
#INTEGER
#REAL
#TEXT
#BLOB


#commiting the database
#conn.commit()
#curs.commit()
#close the connection
#conn.close()
#curs.close()
# Commands for SQLITE
#CREATE TABLE name_of_table (column DATATYPE,)
#INSERT INTO name_of_table VALUES (column,column,...n )
# "to isnsert a lot of data at once"
# cursor.executemany("INSERT INTO name_of_table VALUES(?,?, ..n)", name_of_list)
