import PyPDF2
from tkinter import *
import globals


def transfer_pdf(file):

    file_path = file
    pdf = PyPDF2.PdfFileReader(file_path) # Pass the file object to PdfFilReader

    globals.text.delete(0.0, END)

    for page_num in range((pdf.numPages) -1, -1, -1):

        page_obj = pdf.getPage(page_num)

        try:
            txt = page_obj.extractText()
        except:
            pass
        else:
            globals.text.insert(0.0, txt)
            globals.text.insert(0.0,"".center(100, "-"))
            globals.text.insert(0.0, 'Page {0}\n'.format(page_num + 1))
            globals.text.insert(0.0, '\n')
            
            

