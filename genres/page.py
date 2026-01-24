import streamlit as st


genres = [
    {
        'id': 1,
        'name': 'Ação'
    },
    {
        'id': 2,
        'name': 'Comédia'
    },
    {
        'id': 3,
        'name': 'Terror'
    },
]

def show_genres():
    st.write('Lista de Gêneros:')

    st.table(genres)

    st.title('Registar novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Registar'):
        st.success(f'Gênero "{name}" registado com sucesso')