import streamlit as st
import pandas as pd


if "table_data" not in st.session_state:
    
    st.session_state.table_data=pd.DataFrame(
        columns=["prodcuto","precio","cantidad","subtotal"]
        )
    
st.title("Supermercado el buen vivir")

with st.form("producto_form"):
    producto_nombre=st.text_input("Ingrese el nombre del producto")
    producto_precio=st.number_input("Ingrese el precio del producto")
    producto_cantidad=st.number_input("Ingrese la cantidad de productos")
    
    subtotal_button=st.form_submit_button("Comprar Producto")
