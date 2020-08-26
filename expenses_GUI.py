import sqlite3
import time
import tkinter as tk
from tkinter import *

#Switching to object oriented programming for the GUI frames

#Starting the data bases
curs = sqlite3.connect('userdata.db')
conn = sqlite3.connect('expenses.db')

#create a cursor for the database
cursor = conn.cursor()
udb_cursor = curs.cursor()


class Expense_App(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(Login)
    
    def switch_frame(self, frame_class):
        self.title("SKDN EXPENSE TRACKER")
        canvas = self.configure(width = 500, height= 500)
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Welcome", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)


if __name__ == "__main__":
    app = Expense_App()
    app.mainloop()
