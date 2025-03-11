import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

movies =[
    {'id': 1, 'name': 'Os Mercenarios'},
    {'id': 2, 'name': 'Os Vingadores'},
    {'id': 3, 'name': 'O Poderoso Chefão'},
    {'id': 4, 'name': 'O Senhor dos Anéis'},
    {'id': 5, 'name': 'Titanic'},
    {'id': 6, 'name': 'O Rei Leão'},
    {'id': 7, 'name': 'O Exorcista'},
    {'id': 8, 'name': 'O Pianista'},
    {'id': 9, 'name': 'O Iluminado'},
    {'id': 10, 'name': 'O Resgate do Soldado Ryan'} 
]


def show_movies():
    st.write('Cadastrar novo Filme')

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='actors_grid',
    )

