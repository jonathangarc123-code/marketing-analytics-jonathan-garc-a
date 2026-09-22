#archivo base para despliegue del agente de streamlit
#Librerias
import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

#Er. stremlit vamos a agregar un titulo a la pagina web
st.title("Configuracion inicial")
#agregamos un textbox a nuestra pagina web
st.write("Primera prueba de uso de streamlit y ambiente de MA2026")

#El Slider de stremlit me permite ingresar por un slider el parametro inversión
gasto=st.slider("Seleccine nivel de gasto en publicicdad", 10,200,50)   

#Variables de nuestro modelo
variable_x = np.array([[10], [20], [30], [40],[50]])
variable_y = np.array([15,25,35,45,55])
modelo_lr = LinearRegression()# Archivo base para el despliegue del Agente en Streamlit

#Entrenamiento de nuestro modelo LR
modelo_lr.fit(variable_x,variable_y)

#En stremlit tenemos un boton que dice predecir y al dar click activará la linea del codigo del if
if st.button("Predecir"):
 resultado = modelo_lr.predict([[gasto]])
 
 #Stremlit muestra un mensaje de exito en verde bonito usando succes
 st.success(f"Las ventas proyectadas para una inversion de ${gasto} son:${resultado[0]}")