from tkinter import *
from tkinter import ttk, filedialog
import pandas as pd

root = Tk()
root.config(width=850, height=400)
root.title("Data Frame")

data = pd.read_csv('datos.csv')

frame = Frame(root)
frame.pack(pady=15)
frame.place(x = 25, y = 50)

vista = ttk.Treeview(frame)

def tabla():
    
    clear()
    
    vista["column"] = list(data.columns)
    vista["show"] = "headings"
    
    for column in vista["column"]:
        vista.heading(column, text=column)
       
    data_rows = data.to_numpy().tolist()
    for row in data_rows:
        vista.insert("", "end", values=row)
    vista.pack()

def filters():
    
    clear()
    
    Filtro = menuFiltros.get()
    
    if Filtro == "Nombre":
        filtroNom = data[['Id','Nombre']]
        
        vista["column"] = list(filtroNom.columns)
        vista["show"] = "headings"
        
        for column in vista["column"]:
            vista.heading(column, text=column)
            
        data_rows = filtroNom.to_numpy().tolist()
        for row in data_rows:
            vista.insert("", "end", values = row)
            
    if Filtro == "Edad":
        filtroEdad = data[['Id','Edad']]
        
        vista["column"] = list(filtroEdad.columns)
        vista["show"] = "headings"
        
        for column in vista["column"]:
            vista.heading(column, text=column)
            
        data_rows = filtroEdad.to_numpy().tolist()
        for row in data_rows:
            vista.insert("", "end", values = row)
            
    if Filtro == "Ocupación":
        filtroOcup = data[['Id','Ocupacion']]
        
        vista["column"] = list(filtroOcup.columns)
        vista["show"] = "headings"
        
        for column in vista["column"]:
            vista.heading(column, text=column)
            
        data_rows = filtroOcup.to_numpy().tolist()
        for row in data_rows:
            vista.insert("", "end", values = row)
            
    vista.pack()
    
def clear():
    vista.delete(*vista.get_children())
    
tabla()
    
ttk.Label(root, text = "Filtro mostrar solo: ").place(x=25, y=5)

menuFiltros = ttk.Combobox(root, state="readonly", values=["Nombre", "Edad", "Ocupación"])
menuFiltros.place (x =25, y = 25)

btnFiltro = ttk.Button(root, text = "Filtrar", command=filters)
btnFiltro.place(x=25, y= 300)

btnTabla = ttk.Button(root, text = "Todo", command=tabla)
btnTabla.place(x=150, y= 300)

root.mainloop()