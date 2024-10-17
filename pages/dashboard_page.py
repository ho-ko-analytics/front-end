# pages/dashboard_page.py
import streamlit as st
import numpy as np
import pandas as pd

from pages.components.filters import filters
from pages.components.graphs.line_chart import line_chart_Reach
from pages.components.graphs.line_chart import line_chart_Impressions
from pages.components.graphs.bar_chart import bar_chart_followers
def dashboard_page():
    selected_filters = filters()
    dates = pd.date_range(start=selected_filters['data_inicial'], end=selected_filters['data_final'])

    # Alcance
    line_chart_Reach(dates)
    # Impressão
    line_chart_Impressions(dates)
    # Seguidores
    bar_chart_followers(dates)

