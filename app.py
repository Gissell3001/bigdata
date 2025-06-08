import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv('dataset_olympics.csv')  

# Limpiar datos
df = df.dropna(subset=['Age'])

# Título
st.title("Análisis de los participantes de los Juegos Olímpicos")

# ---------- 1. Boxplot de edades ----------
st.header("🎯 Boxplot de Edades por Sexo")
fig1 = px.box(df, x="Sex", y="Age", color="Sex", points="all")
st.plotly_chart(fig1)

# ---------- 2. Mapa de países con medallas ----------
st.header("🌍 Mapa de Países con Medallas")

# Medallas por país
medallas = df[df["Medal"].notna()].groupby("NOC").size().reset_index(name="Medals")

# Mapa
fig2 = px.choropleth(medallas, 
                     locations="NOC", 
                     color="Medals", 
                     color_continuous_scale="Oranges", 
                     title="Número de medallas por país (NOC)")
st.plotly_chart(fig2)

# ---------- 3. Diagrama de dispersión Altura vs Peso ----------
st.header("⚖ Altura vs Peso")
fig3 = px.scatter(df, x="Height", y="Weight", color="Sex", 
                  hover_data=["Name", "Team", "Sport"], 
                  title="Relación entre altura y peso")
st.plotly_chart(fig3)
