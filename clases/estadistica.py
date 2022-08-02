
import pandas as pd
import numpy as np
import re
import string
import time



def generaDataFrame(df_estadistica,campo):
    df = df_estadistica.iloc[:,[df_estadistica.columns.get_loc(campo)]]
    df = df.groupby([campo]).size().to_frame(name='Frecuencia')
    df['Porcentaje'] = ((df['Frecuencia'] / df['Frecuencia'].sum())*100).round(2)
    df['Porcentaje Valido'] = ((df['Frecuencia'] / df['Frecuencia'].sum())*100).round(2)
    df['Porcentaje Acumulado'] = df['Porcentaje'].cumsum()
    df = df.append(df[['Frecuencia', 'Porcentaje','Porcentaje Valido']].sum(numeric_only=True).rename('Total'))
    df = df.fillna('')

    return df


def devuelveGrafica(df):
    longitud = df.index.size - 1
    grafica = {}

    xvalue = []
    yvalue = []

    for i,v in enumerate(df.index):
        if i != longitud:
            xvalue.append(v)

    for x in xvalue:
        y = df._get_value(x, 'Frecuencia')
        yvalue.append(int(y))

    grafica['x'] = xvalue
    grafica['y'] = yvalue

    return grafica


def devuelveTabla(df):
    tabla = []

    for index, row in df.iterrows():
        fila = {"indice" : index}
        for k in row.keys():
            fila[k.replace(" ", "_")] = row[k]
        tabla.append(fila)

    return tabla


df_estadistica = pd.read_excel("sintomas\SINTOMAS.xlsx")
df_estadistica['3. Género'] = df_estadistica['3. Género'].str.replace('M','Masculino')
df_estadistica['3. Género'] = df_estadistica['3. Género'].str.replace('F','Femenino')

variables = {}

df_genero = generaDataFrame(df_estadistica.copy(),'3. Género')
df_vacuna = generaDataFrame(df_estadistica.copy(),'4. ¿Qué variante del Virus lo contagio?')
df_nivel_sintomas = generaDataFrame(df_estadistica.copy(),'6. ¿Nivel de intensidad que tuvo los síntomas?')
df_lugar = generaDataFrame(df_estadistica.copy(),'7. ¿En qué lugar o evento considera que se contagio?')
df_numero_vacunas = generaDataFrame(df_estadistica.copy(),'8. ¿En caso de haber estado vacunado al momento de contagiarse cuantas do0s tenia aplicadas al contagiarse?')
df_nombre_vacunas = generaDataFrame(df_estadistica.copy(),'9. ¿En caso de haber estado vacunado al momento de contagiarse Qué vacuna recibió?')

variables['Genero'] = df_genero
variables['Variante'] = df_vacuna
variables['Intensidad_Sintomas'] = df_nivel_sintomas
variables['Lugar_Contagio'] = df_lugar
variables['Numero_Vacunas'] = df_numero_vacunas
variables['Nombre_Vacunas'] = df_nombre_vacunas

#variables['grafico'] = devuelveGrafica(df_genero)
#variables['tabla'] = devuelveTabla(df_genero)

listaVariables = {}

for k, v in variables.items():
    var = {}
    var['grafico'] = devuelveGrafica(v)
    var['tabla'] = devuelveTabla(v)

    listaVariables[k] = var