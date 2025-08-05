🌍 Gestión Inteligente de Inventarios Internacionales

MVP - Aplicación Web Interactiva con Streamlit

Esta aplicación permite simular y predecir la ubicación óptima del inventario en distintas ciudades del mundo, basada en datos históricos de ventas, estacionalidad y eventos locales. Fue diseñada como un MVP (Producto Mínimo Viable) para demostrar el potencial de la analítica y modelos de machine learning en la optimización de inventario distribuido a nivel global.

📌 Objetivo

Tomar mejores decisiones sobre dónde ubicar el stock, con base en predicciones de demanda local y métricas logísticas simuladas, para:

- Maximizar disponibilidad.
- Minimizar costos.
- Anticiparse a eventos o picos de demanda por región.

⚙️ Tecnologías Utilizadas

- Python 3.9
- Streamlit
- scikit-learn, XGBoost
- pandas, numpy
- joblib
- Google Sheets API (opcional, para conexión a datos reales)

🧠 ¿Qué hace la app?

1. Simula datos de ciudades, productos y semanas.
2. Predice demanda semanal usando un modelo XGBoost previamente entrenado.
3. Muestra resultados con visualizaciones de la demanda estimada.
4. (Opcional) Conexión a Google Sheets para usar datos reales.

▶️ ¿Cómo ejecutar la app?

1. Clonar el repositorio

git clone https://github.com/tu-usuario/gestion-inventarios-int.git
cd gestion-inventarios-int

2. Instalar dependencias

Usa un entorno virtual:

python -m venv venv
source venv/bin/activate  # En Mac/Linux
venv\Scripts\activate     # En Windows

pip install -r requirements.txt

3. Ejecutar

streamlit run Gestion_inventarios_internacionales.py

🧪 Estructura del Proyecto

gestion-inventarios-int/
├── app/
│   ├── Gestion_inventarios_internacionales.py
│   ├── modelo_xgb.pkl
│   ├── columnas_modelo.pkl
├── README.md
├── requirements.txt

📈 Resultados

- MAE del modelo: 13.39
- R² Score: 0.71
- Modelo basado en variables como ciudad, semana, categoría de producto y factores estacionales.

🚀 Próximos pasos

- Mejorar la precisión del modelo con datos reales.
- Incorporar autenticación de usuarios.
- Añadir conexión directa a plataformas de e-commerce o ERPs.
- Implementar recomendaciones en tiempo real para colocación de stock.
