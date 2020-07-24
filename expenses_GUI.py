import sqlite3
import time
try:
    import Tkinter as tk
except:
    import tkinter as tk
from tkinter import *

#Switching to object oriented programming for the GUI frames

class Expense_App(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.__frame = None
        self.switch_frame(Login)
    
    def switch_frame(self, frame_class):
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
