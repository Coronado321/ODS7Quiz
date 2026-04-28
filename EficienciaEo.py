# Importar librerías necearias
import numpy as np
import streamlit as st
import pandas as pd

# Insertamos título
st.write(''' # ODS 7: Energía Asequible y no contaminante''')
# Insertamos texto con formato
st.markdown("""
Esta aplicación utiliza **Machine Learning** para predecir la eficiencia energetica eólica según la velocidad del viento **ODS 7**.
""")
# Insertamos una imagen
st.image("eolica.jpg")



# Definimos cómo ingresará los datos el usuario
# Usaremos un deslizador
st.sidebar.header("Parámetro")
# Definimos los parámetros de nuestro deslizador:

Vel_input = st.sidebar.slider("Velocidad del viento (m/s)", 0, 140)

# Cargamos el archivo con los datos (.csv)
df =  pd.read_csv('EnergiaEolica.csv', encoding='latin-1')
# Seleccionamos las variables
X = df['Velocidad_Viento_ms']
y = df['Eficiencia_Energetica_kWh']

# Creamos y entrenamos el modelo
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
LR = LinearRegression()
LR.fit(X_train,y_train)

# Hacemos la predicción con el modelo y la velocidad seleccionada por el usuario
b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*Vel_input

# Presentamos loa resultados
st.subheader('Eficiencia energética en kWh')
st.write(f'La eficiencia energética en kWh es: {prediccion}')
