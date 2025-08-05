import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Cargar modelo y columnas
model = joblib.load("modelo_xgb.pkl")
columnas_modelo = joblib.load("columnas_modelo.pkl")

st.set_page_config(page_title="Predicción de Demanda Global", layout="centered")
st.title("🌍 Predicción de Demanda Internacional")
st.markdown("Predice la demanda esperada según variables de país, cliente y condiciones locales.")

# Inputs individuales
st.header("🔢 Ingreso Manual de Datos")
cliente = st.selectbox("Cliente", ["Amazon", "Walmart", "MercadoLibre"])
producto = st.selectbox("Producto", ["Laptop", "Celular", "Tablet"])
pais = st.selectbox("País de destino", ["México", "Brasil", "Alemania", "India"])
semana = st.slider("Semana del año", 1, 52, 30)
precio = st.number_input("Precio promedio de venta (USD)", 50.0, 3000.0, 500.0)
temporada_alta = st.checkbox("¿Es temporada alta?", value=False)
evento_local = st.checkbox("¿Hay evento local?", value=False)

# Codificación y predicción individual
entrada = pd.DataFrame([{
    "cliente": cliente,
    "producto": producto,
    "pais": pais,
    "semana": semana,
    "precio": precio,
    "temporada_alta": int(temporada_alta),
    "evento_local": int(evento_local)
}])

entrada_encoded = pd.get_dummies(entrada, columns=["cliente", "producto", "pais"])
for col in columnas_modelo:
    if col not in entrada_encoded.columns:
        entrada_encoded[col] = 0
entrada_encoded = entrada_encoded[columnas_modelo]

prediccion = model.predict(entrada_encoded)[0]

st.metric("📦 Predicción de demanda", f"{prediccion:.0f} unidades")

# Descargar CSV individual
resultado = entrada.copy()
resultado["prediccion"] = round(prediccion)
csv_individual = resultado.to_csv(index=False).encode("utf-8")
st.download_button("📥 Descargar predicción en CSV", csv_individual, file_name="prediccion_individual.csv")

# Carga de CSV masivo
st.header("📁 Carga de Archivo CSV (Predicción Masiva)")
archivo_csv = st.file_uploader("Sube un archivo .csv con columnas: cliente, producto, pais, semana, precio, temporada_alta, evento_local")

if archivo_csv is not None:
    df_masivo = pd.read_csv(archivo_csv)
    df_masivo["temporada_alta"] = df_masivo["temporada_alta"].astype(int)
    df_masivo["evento_local"] = df_masivo["evento_local"].astype(int)

    df_encoded = pd.get_dummies(df_masivo, columns=["cliente", "producto", "pais"])
    for col in columnas_modelo:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    df_encoded = df_encoded[columnas_modelo]

    df_masivo["prediccion"] = model.predict(df_encoded)
    st.dataframe(df_masivo)

    csv_masivo = df_masivo.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Descargar predicciones masivas", csv_masivo, file_name="predicciones_masivas.csv")
