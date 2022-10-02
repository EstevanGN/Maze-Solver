import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import csv

root = tk.Tk()

# Window general configuration
root.title('Maze Solver')

# Size of canvas
canvas = tk.Canvas(root, width=1280, height=720)
canvas.grid(columnspan=1280, rowspan=720)
canvas.configure(bg='#171d2d')

# Logo
logo = Image.open('logo.png')
logo = logo.resize((100, 100))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=0, row=0)

# Project
title = tk.Label(root, text="Maze Solver", 
                 font="Raleway 32 bold", bg="#171d2d",
                 fg="white", justify=tk.LEFT)
title.grid(column=1, row=0, padx=150)
# Names
creators = tk.Label(root, 
                    text="Daniel Estevan Garcia Niño\nJaime Andres Macias Sanchez\nSantiago Tovar Mosquera", 
                 font="Raleway 16 bold", bg="#171d2d",
                 fg="white", justify=tk.LEFT)
creators.grid( column=2, row=0)
# University
university = Image.open('logo-unal.png')
basewidth = 250
wpercent = (basewidth/float(university.size[0]))
hsize = int((float(university.size[1])*float(wpercent)))
university = university.resize((basewidth,hsize), Image.ANTIALIAS)
university = ImageTk.PhotoImage(university)
university_label = tk.Label(image=university)
university_label.image = university
university_label.grid(column=3, row=0)

# To search files
#def open_file():
#    browse_text.set("Loading...")
#    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
#    if file:
#        read_pdf = PyPDF2.PdfFileReader(file)
#        page = read_pdf.getPage(0)
#        page_content = page.extractText()
#
#        #text box
#        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
#        text_box.insert(1.0, page_content)
#        text_box.tag_configure("center", justify="center")
#        text_box.tag_add("center", 1.0, "end")
#        text_box.grid(column=1, row=3)
#
#        browse_text.set("Browse maze")

# Browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, 
                       command=print("okokokok"), 
                       font="Raleway 9", bg="white", 
                       fg="black", height=1, width=8)
browse_text.set("Browse maze")
browse_btn.grid(column=0, row=2, pady=20)

#canvas = tk.Canvas(root, width=600, height=250)
#canvas.grid(columnspan=3)

root.mainloop()