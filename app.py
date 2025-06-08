import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Histograma de Kilometraje de Vehículos')
if st.button('Construir histograma'):
    st.write('Creando histograma...')
    fig = px.histogram(
        car_data,
        x='odometer',
        title='Distribución de Kilometraje'
    )
    st.plotly_chart(fig, use_container_width=True)
# ----------------------------------------------------------------------------------------------------------------------

st.sidebar.header('Filtros de datos')
# Rango de kilometraje
min_odometer = st.sidebar.slider(
    'Kilometraje mínimo',
    int(car_data['odometer'].min()),
    int(car_data['odometer'].max()),
    int(car_data['odometer'].min())
)
max_odometer = st.sidebar.slider(
    'Kilometraje máximo',
    int(car_data['odometer'].min()),
    int(car_data['odometer'].max()),
    int(car_data['odometer'].max())
)

# Rango de precio
min_price = st.sidebar.number_input(
    'Precio mínimo',
    min_value=int(car_data['price'].min()),
    max_value=int(car_data['price'].max()),
    value=int(car_data['price'].min())
)
max_price = st.sidebar.number_input(
    'Precio máximo',
    min_value=int(car_data['price'].min()),
    max_value=int(car_data['price'].max()),
    value=int(car_data['price'].max())
)

# ----------------------------------------------------------------------------------------------------------------------

filtered = car_data[
    (car_data['odometer'] >= min_odometer) &
    (car_data['odometer'] <= max_odometer) &
    (car_data['price'] >= min_price) &
    (car_data['price'] <= max_price)
]

# -----------------------------------------------------------------------------------------------------------------------

if st.button('Construir gráfico de dispersión filtrado'):
    st.write('Creando gráfico filtrado...')
    fig_scatter_filt = px.scatter(
        filtered,
        x='odometer',
        y='price',
        title='Precio vs Kilometraje (Filtrado)',
        trendline='ols'
    )
    st.plotly_chart(fig_scatter_filt, use_container_width=True)