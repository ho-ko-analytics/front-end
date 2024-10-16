import streamlit as st
from datetime import date

def filters():
    # Dividindo a tela em duas colunas para a data inicial e data final
    col1, col2 = st.columns(2)

    # Input para data inicial na primeira coluna
    with col1:
        data_inicial = st.date_input('Data inicial', value=date.today())

    # Input para data final na segunda coluna
    with col2:
        data_final = st.date_input('Data final', value=date.today())

    # Verificando se a data inicial é maior que a final
    if data_inicial > data_final:
        st.error('A data inicial não pode ser posterior à data final!')
        return None
    else:
        return {"data_inicial": data_inicial, "data_final": data_final}

