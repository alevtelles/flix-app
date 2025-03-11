import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

genres = [
    {'id': 1, 'name': 'Ação'},
    {'id': 2, 'name': 'Animação'},
    {'id': 3, 'name': 'Aventura'},
    {'id': 4, 'name': 'Comédia'},
    {'id': 5, 'name': 'Documentário'},
    {'id': 6, 'name': 'Drama'},
    {'id': 7, 'name': 'Fantasia'},
    {'id': 8, 'name': 'Ficção Científica'},
    {'id': 9, 'name': 'Musical'},
    {'id': 10, 'name': 'Romance'},
    {'id': 11, 'name': 'Suspense'},
    {'id': 12, 'name': 'Terror'}
]

def show_genres():
    st.write('Lista de Gêneros')

    AgGrid(
        data=pd.DataFrame(genres),
        reload_data=True,
        key='genres_grid',
    )

    st.title('Cadastrar novo Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Cadastrar'):
        st.success(f'Gênero "{name}" cadastrado com sucesso')