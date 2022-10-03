import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from read_maze import Laberinto

root = tk.Tk()

# Window general configuration
root.title('Maze Solver')

# Size of canvas
canvas = tk.Canvas(root, width=962, height=601)
canvas.grid(columnspan=10, rowspan=10)
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
title.grid(column=1, row=0)
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

# To search files and possible to return maze
''''Aca se lee el laberinto y se imprime en consola cuando
damos click al boton Select maze. Es decir, lab es nuestro
laberinto que se pasaría a las respectivas busquedas. Más 
abajo están los botones para ejecutar cada una de las busquedas'''
def open_file():
   a = clicked.get()
   lab=Laberinto(int(a))
   lab.imprimirMatriz()

# Drop list
clicked = tk.IntVar()
clicked.set(5)
drop = tk.OptionMenu(root, clicked, 5, 10, 50, 100, 400)
drop.grid(column=0, row=1)
drop_text = tk.StringVar()
drop_btn = tk.Button(root, textvariable=drop_text, 
                       command=open_file,
                       font="Raleway 9", bg="white", 
                       fg="black", height=2, width=12)
drop_text.set("Select maze")
drop_btn.grid(column=1, row=1)

# Depth button
depth_text = tk.StringVar()
depth_btn = tk.Button(root, textvariable=depth_text, 
                       command=print("ok depth"), # Esto se tiene que cambiar para que ejecute la función de búsqueda en profundidad
                       font="Raleway 9", bg="white", 
                       fg="black", height=2, width=12)
depth_text.set("Depth")
depth_btn.grid(column=0, row=2)

# Width button
width_text = tk.StringVar()
width_btn = tk.Button(root, textvariable=width_text, 
                       command=print("ok width"), # Esto se tiene que cambiar para que ejecute la función de búsqueda en anchura
                       font="Raleway 9", bg="white", 
                       fg="black", height=2, width=12)
width_text.set("Width")
width_btn.grid(column=1, row=2)

# Iterative depth button
iterative_depth_text = tk.StringVar()
iterative_depth_btn = tk.Button(root, textvariable=iterative_depth_text, 
                       command=print("ok iterative depth"), # Esto se tiene que cambiar para que ejecute la función de búsqueda en profundidad iterativa
                       font="Raleway 9", bg="white", 
                       fg="black", height=2, width=12)
iterative_depth_text.set("Ite. Depth")
iterative_depth_btn.grid(column=0, row=3)

# Uniform cost button
uniform_cost_text = tk.StringVar()
uniform_cost_btn = tk.Button(root, textvariable=uniform_cost_text, 
                       command=print("ok uniform cost"), # Esto se tiene que cambiar para que ejecute la función de búsqueda en costo uniforme
                       font="Raleway 9", bg="white", 
                       fg="black", height=2, width=12)
uniform_cost_text.set("Unif. Cost")
uniform_cost_btn.grid(column=1, row=3)

# Greedy button
greedy_text = tk.StringVar()
greedy_btn = tk.Button(root, textvariable=greedy_text, 
                       command=print("ok greedy"), # Esto se tiene que cambiar para que ejecute la función de búsqueda en greedy
                       font="Raleway 9", bg="white", 
                       fg="black", height=2, width=12)
greedy_text.set("Greedy")
greedy_btn.grid(column=0, row=4)

# A* button
aStar_text = tk.StringVar()
aStar_btn = tk.Button(root, textvariable=aStar_text, 
                       command=print("ok aStar"), # Esto se tiene que cambiar para que ejecute la función de búsqueda en A*
                       font="Raleway 9", bg="white", 
                       fg="black", height=2, width=12)
aStar_text.set("A*")
aStar_btn.grid(column=1, row=4)

# Maze solved, print
''''Imprimir el laberinto'''

root.mainloop()