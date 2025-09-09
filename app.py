import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("🚀 Demo CI/CD con Streamlit y Render")
st.write("Este es un ejemplo simple para mostrar cómo desplegar una app en Render.")


# Generar datos de ejemplo
x = np.linspace(0, 10, 100)
y = np.cos(x)

df = pd.DataFrame({"x": x, "y": y})


st.subheader("📊 Datos generados")
st.dataframe(df.head())

# Gráfico interactivo con Plotly Express
fig = px.line(df, x="x", y="y", title="Ejemplo de gráfico con Plotly Express", labels={"x": "Eje X", "y": "sin(x)"})
fig.update_traces(line_color="blue", name="sin(x)")



