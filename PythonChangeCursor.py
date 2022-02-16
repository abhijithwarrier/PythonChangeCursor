# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO DEMONSTRATE CHANGING THE MOUSE CURSOR TYPE WHILE HOVERING OVER THE BUTTON WIDGET IN PYTHON TKINTER
#
# In Python Tkinter, the cursor type can be changed while hovering over Button Widget by setting the cursor parameter
# of the Button Widget to one of the cursor types mentioned in the below list

# Importing necessary packages
import tkinter as tk
from tkinter import *
from tkinter import ttk

# Making the lists of mouse cursor types that are available in Python Tkinter.
cursorTypesList = [ "arrow", "circle", "clock", "cross", "dotbox", "exchange", "fleur", "heart", "man", "mouse",
                    "pirate", "plus", "shuttle", "sizing", "spider", "spraycan", "star", "target", "tcross", "trek" ]

# Defining CreateWidgets() to create necessary widgets for the GUI
def CreateWidgets():
    cursorTypeLabel = Label(root, text="CURSOR TYPES : ", bg="steelblue4")
    cursorTypeLabel.grid(row=1, column=0, padx=5, pady=5)
    root.cursorTypeCombo = ttk.Combobox(root, width=15, values=cursorTypesList)
    root.cursorTypeCombo.grid(row=1, column=2, padx=5, pady=8)
    root.cursorTypeCombo.set("SELECT CURSOR")

    messageLabel = Label(root, text="SELECT CURSOR TYPE FROM DROPDOWN\n AND CLICK ON THE BUTTON", bg="steelblue4")
    messageLabel.grid(row=2, column=0, padx=5, pady=5, columnspan=3)
    root.clickButton = Button(root, text="CHANGE CURSOR         ", width=20, command=changeCursor)
    root.clickButton.grid(row=3, column=0, columnspan=3, padx=5, pady=8)

# Defining changeCursor() function for changing the mouse cursor based on dropdown selection
def changeCursor():
    # Fetching & storing the cursor type selected in the variable
    i_CursorType = root.cursorTypeCombo.get()
    # Configuring the button to display the selected cursor
    root.clickButton.config(cursor=i_CursorType)

# Creating object of tk class
root = tk.Tk()

# Setting title, background color & size of tkinter window
# & disabling the resizing property
root.geometry("310x150")
root.resizable(False, False)
root.title("PythonChangeCursor")
root.config(bg="steelblue4")

# Creating tkinter variables
language = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
