import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pytz

def bar_chart_followers(dates, timezone='America/Sao_Paulo'):
    # Definir o fuso horário
    tz = pytz.timezone(timezone)
    dates = dates.tz_localize('UTC').tz_convert(tz)
    
    # Gerar valores aleatórios de seguidores para cada data
    facebook_followers = np.random.randint(1000, 5000, size=len(dates))
    instagram_followers = np.random.randint(2000, 7000, size=len(dates))

    # Criar um DataFrame para armazenar os dados de seguidores
    followers_data = pd.DataFrame({
        'Data': dates,
        'Facebook': facebook_followers,
        'Instagram': instagram_followers
    })

    # Transformar o DataFrame no formato longo para o gráfico de barras
    followers_data_melted = followers_data.melt(id_vars='Data', 
                                                value_vars=['Facebook', 'Instagram'], 
                                                var_name='Plataforma', 
                                                value_name='Seguidores')

    # Criar o gráfico de barras
    fig = px.bar(followers_data_melted, x='Data', y='Seguidores', color='Plataforma',
                 title='Seguidores')

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)