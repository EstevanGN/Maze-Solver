import csv
 
class Laberinto:
  def __init__(self,tamaño): 
    self.tamaño=tamaño
    self.rep=list()
    self.inicio=(1,2)
    self.final=(self.tamaño,self.tamaño-1)
    self.CrearMatriz(tamaño)

  def CrearMatriz(self,tamaño):  
    if(tamaño == 5):      
      cadena="maze_5x5.csv"
    elif(tamaño == 10):      
      cadena="maze_10x10.csv"
    elif(tamaño == 50):  
      cadena="maze_50x50.csv"
    elif(tamaño == 100):      
      cadena="maze_100x100.csv"
    elif(tamaño == 400):      
      cadena="maze_400x400.csv"
    primera_fila=list()
    for i in range(tamaño):
      primera_fila.append(1)
    self.rep.append(primera_fila)  
    with open(cadena, newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
          if(row != []):
            fila=list()
            for c in row:
              if(c=="c"):
                fila.append(0)
              else:
                fila.append(1)
            self.rep.append(fila)      

  def imprimirMatriz(self):
    print(self.rep)