import streamlit as st

st.title("¡Hola mundo desde Streamlit")

# Campos de entrada para los números
num1 = st.number_input('Número 1', value=0)
num2 = st.number_input('Número 2', value=0)

# Botón para calcular la suma
if st.button('Calcular Suma'):
    suma = num1 + num2
    st.header(f'La suma es: {suma}')
