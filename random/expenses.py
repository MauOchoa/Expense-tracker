from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import selenium
import os

window = tk.Tk()
window.title("Expense tracker")

canvas = tk.Canvas(window, width= 400 ,height = 500)

filename = PhotoImage(file = "suitcase.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

password = 0000
text_file = open("database.txt","a")
entry = tk.Entry(window)
canvas.create_window(200, 380, window=entry)

def entrysquare():
    pass_entry = entry.get()
    if pass_entry == "0000":
        print ("login succeeded!") 

def set_password():
    open("database.txt","a")
    existing = text_file.readline().split('=')[1]
    if existing == "0000":
        pass_entry = entry.get()
        text_file.write("password= "+pass_entry)
        text_file.close()
    


login_button = tk.Button(text='Login', command=entrysquare, fg = 'black', bg= 'white')
canvas.create_window(150, 420, window=login_button)
set_pass = tk.Button(text='Set Password', command =set_password, fg= 'black', bg='white')
canvas.create_window(220,420, window=set_pass)
canvas.pack()


window.mainloop()
