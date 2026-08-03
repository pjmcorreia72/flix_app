import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


actors = [
    {
        'id': 1,
        'name': 'Titanic'
    },
    {
        'id': 2,
        'name': 'Os Mercenários'
    },
    {
        'id': 3,
        'name': 'De Volta para o Futuro'
    },
]

def show_movies():
    st.write('Lista de Filmes:')

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid',
        )