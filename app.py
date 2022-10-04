import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from read_maze import Laberinto
import Busqueda

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
logo_label.grid(column=1, row=0)

# Project
title = tk.Label(root, text="Maze Solver", 
                 font="Raleway 32 bold", bg="#171d2d",
                 fg="white", justify=tk.LEFT)
title.grid(column=2, row=0)
# Names
creators = tk.Label(root, 
                    text="Daniel Estevan Garcia Niño\nJaime Andres Macias Sanchez\nSantiago Tovar Mosquera", 
                 font="Raleway 12 bold", bg="#171d2d",
                 fg="white", justify=tk.LEFT)
creators.grid( column=3, row=8)
# University
university = Image.open('logo-unal.png')
basewidth = 250
wpercent = (basewidth/float(university.size[0]))
hsize = int((float(university.size[1])*float(wpercent)))
university = university.resize((basewidth,hsize), Image.ANTIALIAS)
university = ImageTk.PhotoImage(university)
university_label = tk.Label(image=university)
university_label.image = university
university_label.grid(column=0, row=8)

# To search files and possible to return maze
''''Aca se lee el laberinto y se imprime en consola cuando
damos click al boton Select maze. Es decir, lab es nuestro
laberinto que se pasaría a las respectivas busquedas. Más 
abajo están los botones para ejecutar cada una de las busquedas'''


def open_file(alg):
   a = clicked.get()
   lab=Laberinto(int(a))
   mat=lab.rep
   d1 = Busqueda.GridProblem(initial=Busqueda.convertir(mat)[1],goal=Busqueda.convertir(mat)[2],obstacles=Busqueda.convertir(mat)[0])
   if(alg=="depth"):
      path = Busqueda.path_states(Busqueda.breadth_first_search(d1))
   elif(alg=="width"):
      path = Busqueda.path_states(Busqueda.depth_limited_search(d1))
   elif(alg=="iterative depth"):
      path = Busqueda.path_states(Busqueda.depth_first_recursive_search (d1))
   elif(alg=="uniform cost"):         
      path = Busqueda.path_states(Busqueda.uniform_cost_search(d1))
   elif(alg=="greedy"):         
      path = Busqueda.path_states(Busqueda.greedy_bfs(d1))
   elif(alg=="aStar"):         
      path = Busqueda.path_states(Busqueda.astar_search(d1))   
   ab = Busqueda.estados(path, mat)
   Busqueda.plt.rcParams["figure.figsize"] = [7.00, 3.50]
   Busqueda.plt.rcParams["figure.autolayout"] = True
   fig, ax = Busqueda.plt.subplots()

   def update(i):
      im_normed = ab[i]
      ax.imshow(im_normed)
      ax.set_axis_off()

   anim = Busqueda.FuncAnimation(fig, update, frames=len(ab), interval=50)

   Busqueda.plt.show()



# Drop list
clicked = tk.IntVar()
clicked.set(5)
drop = tk.OptionMenu(root, clicked, 5, 10, 50, 100, 400)
drop.grid(column=2, row=1)



def alg_depth(): open_file("depth")
def alg_width(): open_file("width")
def alg_iterative_depth(): open_file("iterative depth")
def alg_uniform_cost(): open_file("uniform cost")
def alg_greedy(): open_file("greedy")
def alg_aStar(): open_file("aStar")

# Depth button
depth_text = tk.StringVar()
depth_btn = tk.Button(root, textvariable=depth_text, 
                       command=alg_depth, # Esto se tiene que cambiar para que ejecute la función de búsqueda en profundidad
                       font="Raleway 9", bg="white", 
                       fg="black", height=2, width=12)
depth_text.set("Depth")
depth_btn.grid(column=1, row=2)

# Width button
width_text = tk.StringVar()
width_btn = tk.Button(root, textvariable=width_text, 
                       command=alg_width, # Esto se tiene que cambiar para que ejecute la función de búsqueda en anchura
                       font="Raleway 9", bg="white", 
                       fg="black", height=2, width=12)
width_text.set("Width")
width_btn.grid(column=2, row=2)

# Iterative depth button
iterative_depth_text = tk.StringVar()
iterative_depth_btn = tk.Button(root, textvariable=iterative_depth_text, 
                       command=alg_iterative_depth, # Esto se tiene que cambiar para que ejecute la función de búsqueda en profundidad iterativa
                       font="Raleway 9", bg="white", 
                       fg="black", height=2, width=12)
iterative_depth_text.set("Ite. Depth")
iterative_depth_btn.grid(column=1, row=3)

# Uniform cost button
uniform_cost_text = tk.StringVar()
uniform_cost_btn = tk.Button(root, textvariable=uniform_cost_text, 
                       command=alg_uniform_cost, # Esto se tiene que cambiar para que ejecute la función de búsqueda en costo uniforme
                       font="Raleway 9", bg="white", 
                       fg="black", height=2, width=12)
uniform_cost_text.set("Unif. Cost")
uniform_cost_btn.grid(column=2, row=3)

# Greedy button
greedy_text = tk.StringVar()
greedy_btn = tk.Button(root, textvariable=greedy_text, 
                       command=alg_greedy, # Esto se tiene que cambiar para que ejecute la función de búsqueda en greedy
                       font="Raleway 9", bg="white", 
                       fg="black", height=2, width=12)
greedy_text.set("Greedy")
greedy_btn.grid(column=1, row=4)

# A* button
aStar_text = tk.StringVar()
aStar_btn = tk.Button(root, textvariable=aStar_text, 
                       command=alg_aStar, # Esto se tiene que cambiar para que ejecute la función de búsqueda en A*
                       font="Raleway 9", bg="white", 
                       fg="black", height=2, width=12)
aStar_text.set("A*")
aStar_btn.grid(column=2, row=4)

# Maze solved, print
''''Imprimir el laberinto'''

root.mainloop()