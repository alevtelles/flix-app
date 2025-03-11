import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

actors =[
    {'id': 1, 'name': 'Tom Hanks'},
    {'id': 2, 'name': 'Leonardo DiCaprio'},
    {'id': 3, 'name': 'Meryl Streep'},
    {'id': 4, 'name': 'Denzel Washington'},
    {'id': 5, 'name': 'Julia Roberts'},
    {'id': 6, 'name': 'Will Smith'},
    {'id': 7, 'name': 'Angelina Jolie'},
    {'id': 8, 'name': 'Brad Pitt'},
    {'id': 9, 'name': 'Johnny Depp'},
    {'id': 10, 'name': 'Sandra Bullock'},
    {'id': 11, 'name': 'Tom Cruise'},
    {'id': 12, 'name': 'Harrison Ford'},    
]


def show_actors():
    st.write('Lista de Atores/Atrizes')

    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        key='actors_grid',
    )

    st.title('Cadastrar novo Ator/Atriz')
    name = st.text_input('Nome do Ator/Atriz')
    if st.button('Cadastrar'):
        st.success(f'Ator/Atriz "{name}" cadastrado com sucesso')
