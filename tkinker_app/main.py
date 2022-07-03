from tkinter import *
from tkinter import filedialog
import file
import globals

globals.initalize()
file.file_menu()





globals.gui.title("Bill Editing and Voting")
globals.gui.geometry("1000x1000")  # 600 is length and 500 is breadth of the text editor.
globals.gui.mainloop()  # To display the window in the screen. This line is compulsory.