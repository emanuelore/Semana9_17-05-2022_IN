import xlrd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb #genera graficos speciales

#leer el archivo
data = pd.read_excel("BI_Postulantes09.xlsx")

#convertir a DataFrame
lista = pd.DataFrame(data)

#agrupar por especialidad
segmento = data.groupby("Nom_Especialidad").size()

#solo se consideran variables especificas
#?el 1er parametro hace el proceso de segmentacion por ese campo
#?apartir del 2do parametro recien se elimina los campos indicados
data.drop(["Cod_Especialidad", "Nivel Organización", "Grado Nerviosismo", "Dependencia Internet"], 1).hist()

#muestra el histograma solo con los datos no eliminados
plt.show()

#1er param: eliminar los datos nulos
#2do param: agrupar por ese campo
#3er param: altura de la grafica
#?50px = 2 cm.
sb.pairplot(data.dropna(),
            hue="Nom_Especialidad",
            height=4,
            vars=["Apertura Nuevos Conoc.", "Participación Grupo Social", "Grado Empatía"],
            kind="scatter"
            )
plt.show()