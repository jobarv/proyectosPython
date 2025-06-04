# 1. Ingresar la cantidad en USD.
# 2. Realizar la fomula matematica par aconvertir a EUR.
# 3. Imprimir el resultado en la consola, se debe realizar con un boton.

import streamlit as st

st.title("Conversion de Dolares a Euros")

dolares=st.number_input("Ingrese la cantidad de dolares")

euros=dolares*2
euros=str(euros)

st.button("Procesar", on_click=print("Aqui se imprimira el resultado: " + euros))