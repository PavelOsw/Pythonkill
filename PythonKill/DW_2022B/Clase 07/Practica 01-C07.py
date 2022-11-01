#Creado por Pavel Oswaldo Olage Gallegos
#-21563839

from tkinter import END, messagebox, ttk
import tkinter as tk

root = tk.Tk()
root.config(width=300, height=300)
root.title("Calculadora")

ttk.Label(root, text = "Ingrese el numero 1: ").place(x=75, y=30)
txtNumero1 = ttk.Entry()
txtNumero1.place(x=75, y=50)

ttk.Label(root, text = "Ingrese el numero 2: ").place(x=75, y=80)
txtNumero2 = ttk.Entry()
txtNumero2.place(x=75, y=100)

ttk.Label(root, text = "Resultado: ").place(x=75, y=130)
txtResultado = ttk.Entry()
txtResultado.place(x=75, y=150)

def suma():
    resultado = 0
    n1 = int(txtNumero1.get())
    n2 = int(txtNumero2.get())
    resultado = n1 + n2
    txtResultado.delete(0, END)
    txtResultado.insert(0, resultado)
    
def resta():
    resultado = 0
    n1 = int(txtNumero1.get())
    n2 = int(txtNumero2.get())
    resultado = n1 - n2
    txtResultado.delete(0, END)
    txtResultado.insert(0, resultado)
    
def multi():
    resultado = 0
    n1 = int(txtNumero1.get())
    n2 = int(txtNumero2.get())
    resultado = n1 * n2
    txtResultado.delete(0, END)
    txtResultado.insert(0, resultado)
    
def div():
    resultado = 0
    n1 = int(txtNumero1.get())
    n2 = int(txtNumero2.get())
    resultado = n1 / n2
    txtResultado.delete(0, END)
    txtResultado.insert(0, resultado)
    
def porcen():
    resultado = 0
    n1 = int(txtNumero1.get())
    n2 = int(txtNumero2.get())
    resultado = n2 * 100 / n1
    txtResultado.delete(0, END)
    txtResultado.insert(0, resultado)    
    

        
btnCalcular = ttk.Button(root, text = "+", command=suma)
btnCalcular.place(x=50, y=200)

btnCalcular = ttk.Button(root, text = "-", command=resta)
btnCalcular.place(x=150, y=200)

btnCalcular = ttk.Button(root, text = "x", command=multi)
btnCalcular.place(x=50, y=225)

btnCalcular = ttk.Button(root, text = "/", command=div)
btnCalcular.place(x=150, y=225)

btnCalcular = ttk.Button(root, text = "%", command=porcen)
btnCalcular.place(x=100, y=250)

root.mainloop()