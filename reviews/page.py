import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


reviews = [
    {
        'id': 1,
        'stars': 5
    },
    {
        'id': 2,
        'stars': 4
    },
    {
        'id': 3,
        'stars': 3
    },
]

def show_reviews():
    st.write('Lista de Avaliações:')

    AgGrid(
        data=pd.DataFrame(reviews),
        reload_data=True,
        key='reviews_grid',
        )

    st.title('Registar novo(a) Ator/Atriz')
    name = st.text_input('Nome do(a) Ator/Atriz')
    if st.button('Registar'):
        st.success(f'Ator/Atriz "{name}" registado(a) com sucesso')