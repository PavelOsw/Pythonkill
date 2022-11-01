import pandas as pd

diccionario = pd.DataFrame(

{
'Nombre': ['Ramirez','Lopez','Hernandez','Vargas','Topete','Suarez' ],
'RangoMilitar': ['Cabo','Sargento','Teniente','Teniente Segundo','Mayor','Almirante' ],
'Estado': ['Guanajuato','Mexico','Mexico','Sinaloa','Jalisco','Jalisco' ]
}, columns=['Nombre', 'RangoMilitar', 'Estado'], index=[7, 6, 4, 5, 2, 1]
)

print ("Diccionario: \n%s" % diccionario)
print("------------------------------------")
print ("Diccionario: \n%s" % diccionario.tail)
print("------------------------------------")
print ("Diccionario: \n%s" % diccionario.head)
print("------------------------------------")
print ("Diccionario: \n%s" % diccionario.columns)
print("------------------------------------")
print (diccionario.shape)
