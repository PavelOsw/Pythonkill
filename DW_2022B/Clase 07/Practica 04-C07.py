#Creado por Pavel Oswaldo Olage Gallegos
#-21563839

from tkinter import END, messagebox, ttk
import tkinter as tk
from statistics import mode, pstdev

root = tk.Tk()
root.config(width=300, height=300)
root.title("Mediciones")

ttk.Label(root, text = "Conjunto de valores: [1,2,3,4,5,6,7,6,9]").place(x=15, y=10)

ttk.Label(root, text = "Selecciona una opción").place(x=50, y=50)
cbOpe = ttk.Combobox(root, state="readonly", values=["Media", "Mediana", "Moda", "Desviacón media"])
cbOpe.place(x= 50, y= 75)

conjunto = [1,2,3,4,5,6,7,6,9]

def operaciones():
    medicion = cbOpe.get()
    if medicion == "Media":
        aux = 0
        x = 0
        while x < 9:
            aux += conjunto[x]
            x+=1
        res = aux/9
        messagebox.showinfo(message="Media: " + str(res))
        
    if medicion == "Mediana":
        aux = 0
        x = 0
        while x < 9:
            aux += conjunto[x]
            x+=1
        res = aux/2
        messagebox.showinfo(message="Mediana: " + str(res))
        
    if medicion == "Moda":
        res = mode(conjunto)
        messagebox.showinfo(message="Moda: " + str(res))
    
    if medicion == "Desviacón media":
        res = pstdev(conjunto)
        messagebox.showinfo(message="Desviacón media: " + str(res))


btnMostrar = ttk.Button(root, text = "Calcular", command=operaciones)
btnMostrar.place(x=50, y=150)
root.mainloop()