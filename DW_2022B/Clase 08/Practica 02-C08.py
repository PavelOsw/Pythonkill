import pandas as pd
import numpy as np

diccionario = pd.DataFrame(
{
    'Nombre': ['Ramirez','Lopez','Hernandez','Vargas','Topete','Suarez' ],
    'RangoMilitar': ['Cabo','Sargento','Teniente','Teniente Segundo','Mayor','Almirante' ],
    'Estado': ['Guanajuato','Mexico','Mexico','Sinaloa','Jalisco','Jalisco' ]
}, 
    columns=['Nombre', 'RangoMilitar', 'Estado'], index=[7, 6, 4, 5, 2, 1]
)

print ("Diccionario: \n%s" % diccionario)