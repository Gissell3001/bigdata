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
                     color_continuous_scale="Blues",
                     title="Número de medallas por país (NOC)")
st.plotly_chart(fig2)

# ---------- 3. Gráfico de barras de los países con más medallas ----------
st.header("📊 Gráfico de barras de los países con más medallas")

# Limpiar datos: solo registros con medalla
df_medallas = df.dropna(subset=["Medal"])

# Filtrar países con más medallas
top_n = st.slider("Número de países a mostrar", min_value=5, max_value=25, value=20)
top_paises = (
    df_medallas.groupby("NOC")["Medal"]
    .count()
    .sort_values(ascending=False)
    .head(top_n)
    .index
)
df_filtrado = df_medallas[df_medallas["NOC"].isin(top_paises)]

# Agrupar
df_grouped = df_filtrado.groupby(["NOC", "Medal"]).size().reset_index(name="Count")

# Gráfico
fig = px.bar(
    df_grouped,
    x="NOC",
    y="Count",
    color="Medal",
    barmode="group",
    title="Distribución de los países con más medallas",
    color_discrete_map={
        "Gold": "FFD700",
        "Silver": "#C0C0C0",
        "Bronze": "#CD7F32"
    }
)

# Mostrar
st.plotly_chart(fig)


# ---------- 3. Diagrama de dispersión Altura vs Peso ----------
st.header("⚖ Altura vs Peso")
fig3 = px.scatter(df, x="Height", y="Weight", color="Sex",
                  labels={
                      "Height": "Altura (cm)",
                      "Weight": "Peso (kg)"
                  }
                  hover_data=["Name", "Team", "Sport"],
                  title="Relación entre altura y peso")
st.plotly_chart(fig3)
