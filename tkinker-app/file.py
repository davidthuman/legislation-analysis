from tkinter import *
from tkinter import filedialog
import globals
import pdfReader


def new_file():
    globals.text.delete(0.0, END)  # Deletes all the contents of the text editor.


def open_file():
    file1 = filedialog.askopenfile(mode='r')  # To open open_file filedialog.
    print(file1.name)
    if file1.name[-3:] == "pdf":
        name = file1.name
        file = name[name.rfind("/") + 1:]
        pdfReader.transfer_pdf(file)
    else:
        data = file1.read()
        globals.text.delete(0.0, END)
        globals.text.insert(0.0, data)  # Inserts data variable in text editor.


def save_file():
    filename = "Untitled.txt"
    data = globals.text.get(0.0, END)
    file1 = open(filename, "w")
    file1.write(data)


def save_as():
    file1 = filedialog.asksaveasfile(mode='w')  # To open save_as filedialog.
    data = globals.text.get(0.0, END)
    file1.write(data)

def file_menu():
    mymenu = Menu()
    list1 = Menu()
    list1.add_command(label='New file', command=new_file)  # To create menus.
    list1.add_command(label='Open file', command=open_file)
    list1.add_command(label='Save', command=save_file)
    list1.add_command(label='Save as', command=save_as)
    list1.add_command(label='Exit', command=globals.gui.quit)
    mymenu.add_cascade(label='File', menu=list1)  # To create a file option.
    globals.gui.config(menu=mymenu)
    globals.text.pack()  # To display the text in the centre.


