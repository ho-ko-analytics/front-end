import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pytz

def line_chart_Reach(dates, timezone='America/Sao_Paulo'):
    # Definir o fuso horário
    tz = pytz.timezone(timezone)
    dates = dates.tz_localize('UTC').tz_convert(tz)

    # Gerar valores aleatórios para o alcance (reach) das redes sociais
    facebook_reach = np.random.randint(1000, 3000, size=len(dates))
    instagram_reach = np.random.randint(1500, 2500, size=len(dates))

    # Criar um DataFrame para armazenar esses dados
    reach_data = pd.DataFrame({
        'Data': dates,
        'Facebook': facebook_reach,
        'Instagram': instagram_reach
    })

    fig = px.line(reach_data, x='Data', y=['Facebook', 'Instagram'], 
                  labels={'value': 'Alcance', 'variable': 'Plataformas'},
                  title="Alcance")

    # Configurar o layout para ser mais legível
    fig.update_layout(hovermode='x unified') 
    st.plotly_chart(fig, use_container_width=True)


def line_chart_Impressions(dates, timezone='America/Sao_Paulo'):
    # Definir o fuso horário
    tz = pytz.timezone(timezone)
    dates = dates.tz_localize('UTC').tz_convert(tz)

    # Gerar valores aleatórios para o Impressão (impressions) das redes sociais
    facebook_impressions = np.random.randint(1500, 3500, size=len(dates))
    instagram_impressions = np.random.randint(2500, 3000, size=len(dates))
    googleAnalytics_impressions = np.random.randint(3000, 5000, size=len(dates))

    # Criar um DataFrame para armazenar esses dados
    reach_data = pd.DataFrame({
        'Data': dates,
        'Facebook': facebook_impressions,
        'Instagram': instagram_impressions,
        'Google Analytics': googleAnalytics_impressions
    })

    fig = px.line(reach_data, x='Data', y=['Facebook', 'Instagram', 'Google Analytics'], 
                  labels={'value': 'Impressões', 'variable': 'Plataformas'},
                  title="Impressões")

    # Configurar o layout para ser mais legível
    fig.update_layout(hovermode='x unified') 
    st.plotly_chart(fig, use_container_width=True)