#Creado por Pavel Oswaldo Olage Gallegos
#-21563839

from tkinter import END, messagebox, ttk
import tkinter as tk
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap

root = tk.Tk()
root.config(width=300, height=150)
root.title("Estados")

ttk.Label(root, text = "Selecciona una opción").place(x=50, y=30)
cbEstado = ttk.Combobox(root, state="readonly", values=[
"Aguascalientes",
"Baja California",
"Baja California Sur",
"Campeche",
"Chiapas",
"Chihuahua",
"Coahuila",
"Colima",
"CDMX",
"Durango",
"Guanajuato",
"Guerrero",
"Hidalgo",
"Jalisco",
"Estado de México",
"Michoacán",
"Morelos",
"Nayarit",
"Nuevo León",
"Oaxaca",
"Puebla",
"Querétaro",
"Quintana Roo",
"San Luis Potosí",
"Sinaloa",
"Sonora",
"Tabasco",
"Tamaulipas",
"Tlaxcala",
"Veracruz",
"Yucatán",
"Zacatecas"
])
cbEstado.place(x= 50, y= 50)

def mostrarEsatdo():
    estado = cbEstado.get()
    if estado == "Jalisco":
        messagebox.showinfo(message="Eligió al estado más bélico de México: " + estado)
    if estado == "Sinaloa":
        messagebox.showinfo(message="Eligió al estado más bélico de México: " + estado)
    if estado == "Tamaulipas":
        messagebox.showinfo(message="Eligió al estado más bélico de México: " + estado)
    if estado == "Michoacán":
        messagebox.showinfo(message="Eligió al estado más bélico de México: " + estado)
    else:
        messagebox.showinfo(message="También está feo pero no es tan bélico: " + estado)


btnMostrar = ttk.Button(root, text = "Mostrar Estado seleccionado", command=mostrarEsatdo)
btnMostrar.place(x=50, y=100)
root.mainloop()