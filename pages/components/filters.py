import streamlit as st
from datetime import date

def date_inputs():
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
        return {"data_inicial": date.today(), "data_final": date.today()}
    else:
        return {"data_inicial": data_inicial, "data_final": data_final}

def gender():
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        option_man = st.checkbox(label="Homem", value=True)
    with col2:
        option_woman = st.checkbox(label="Mulher", value=True)

    # Retorna as opções de gênero
    return {
        "genero_homem": option_man,
        "genero_mulher": option_woman
    }

def filters():
    filters_obj = {}

    # Obtendo o dicionário de datas e adicionando ao objeto
    date_data = date_inputs()
    if date_data:
        filters_obj.update(date_data)

    # Obtendo o dicionário de gênero e adicionando ao objeto
    gender_data = gender()
    filters_obj.update(gender_data)

    # Retornando o objeto completo
    return filters_obj
