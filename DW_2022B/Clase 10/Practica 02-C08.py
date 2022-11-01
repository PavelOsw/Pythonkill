from tkinter import *
from tkinter import ttk, filedialog
import pandas as pd

root = Tk()
root.config(width=850, height=400)
root.title("Estadísticas")

data = pd.read_csv('datos.csv')

frame = Frame(root)
frame.pack(pady = 5)
frame.place(x = 25, y = 50)

vista = ttk.Treeview(frame)

def clear():
    vista.delete(*vista.get_children())

def tabla():
    clear()
    
    vista["column"] = list(data.columns)
    vista["show"] = "headings"
    
    for column in vista["column"]:
        vista.heading(column, text=column)
       
    data_rows = data.to_numpy().tolist()
    for row in data_rows:
        vista.insert("", "end", values=row)
        
    
def filtros():
    clear()
    
    seleccion = menuFiltro.get()
    
    if seleccion == "Edad":
        Edades = data[['edad']].sort_values('edad')
        recuentoEdad = pd.crosstab(index = data['edad'], columns = 'Recuento de edades').sort_values('edad')
        filtroEdad = pd.merge(Edades, recuentoEdad, left_on='edad', right_on='edad')
        
        vista["column"] = list(filtroEdad.columns)
        vista["show"] = "headings"
        
        for column in vista["column"]:
            vista.heading(column, text = column)
            
        data_rows = filtroEdad.to_numpy().tolist()
        for row in data_rows:
            vista.insert("", "end", values = row)
            
    if seleccion == "Ocupación":
        Ocupaciones = data[['ocupacion']].sort_values('ocupacion')
        recuentoOcup = pd.crosstab(index = data['ocupacion'], columns = 'Recuento de ocupaciones').sort_values('ocupacion')
        filtroOcup = pd.merge(Ocupaciones, recuentoOcup, left_on='ocupacion', right_on='ocupacion')
        
        vista["column"] = list(filtroOcup.columns)
        vista["show"] = "headings"
        
        for column in vista["column"]:
            vista.heading(column, text = column)
            
        data_rows = filtroOcup.to_numpy().tolist()
        for row in data_rows:
            vista.insert("", "end", values = row)
    
tabla()
vista.pack()

ttk.Label(root, text = "Selecciona filtro: ").place(x=25, y=5)

menuFiltro = ttk.Combobox(root, state="readonly", values=["Edad", "Ocupación"])
menuFiltro.place (x =25, y = 25)

btnFiltro = ttk.Button(root, text = "Filtrar", command=filtros)
btnFiltro.place(x=25, y= 300)

btnTabla = ttk.Button(root, text = "Todo", command=tabla)
btnTabla.place(x=150, y= 300)

root.mainloop()