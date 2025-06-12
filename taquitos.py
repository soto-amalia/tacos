#Encontrar los mejores taocos de llaciudad de Mexico
#Quisimos llevar nuestro proyecto a un nuevo nivel, ya que nos preguntamos si existia la posibilidad de 
#encontrar los datos de el API de google, ya que de los dacos que las personas y los negocios
#nos proporcionan dia a dia son demaciado valiosos.
#En Cdmx y área conurbana existe màs de 1000 taquerias las cueales se dividen entre locales y
#negocios callejeros, así que logramos extraer una miestra de 3000 mil datos
#de los cuales nos surguieron las siguientes preguntas: 
#¿Cuàles son los mejores tacos de la ciudad de méxico? 
#¿Cuáles son los mejores tacos cerca de Escom? 

#¿Cuales son los tacos màs caros? 
#¿Cuales son los màs baratos?
#CUáles son los más pupulares? 
#Cuáles son los mmas recomendados? 


print("taquitos de pastor")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo limpio y ya ordenado
df = pd.read_csv("tacos_CDMX_sorted.csv")

print("Columnas disponibles:")
print(df.columns.tolist())

# Mostrar el DataFrame completo
print(df)

# Importar datos
df = pd.read_csv("tacos_CDMX_sorted.csv")#le dices que lea el dataset
df.dropna(inplace=True)#Borrar los nulos 
df.head()

df["bean_origin"].unique()



