#Creado por Pavel Oswaldo Olage Gallegos
#-21563839

from tkinter import END, messagebox, ttk
import tkinter as tk
import math

root = tk.Tk()
root.config(width=300, height=300)
root.title("Factorial")

ttk.Label(root, text = "Ingrese numero para calcular el factorial:").place(x=50, y=30)
txtNumero1 = ttk.Entry()
txtNumero1.place(x= 75, y= 50)

ttk.Label(root, text = "Ingrese numero:").place(x=75, y=125)
txtNumero2 = ttk.Entry()
txtNumero2.place(x= 75, y= 150)

ttk.Label(root, text = "Elevar a la potencia de:").place(x=75, y=175)
txtNumero3 = ttk.Entry()
txtNumero3.place(x= 75, y= 200)
    
def factorial():
    x = 1
    rango = int(txtNumero1.get())
    fact = 1
    for i in range(x, rango):
        fact = fact*(i+1)
    messagebox.showinfo(message="El factorial es: "+str(fact))
    
def potencia():
    n1 = int(txtNumero2.get())
    n2 = int(txtNumero3.get())
    messagebox.showinfo(message="El factorial es: "+str(pow(n1, n2)))


btnCalcular1 = ttk.Button(root, text = "Factorial", command=factorial)
btnCalcular1.place(x= 100, y= 75)

btnCalcular2 = ttk.Button(root, text = "Calcular", command=potencia)
btnCalcular2.place(x= 100, y= 225)

root.mainloop()