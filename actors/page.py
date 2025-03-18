import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from actors.service import ActorService


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de Atores/Atrizes')
        actors_df = pd.json_normalize(actors)

        AgGrid(
            data=actors_df,
            reload_data=True,
            key='actors_grid',
        )
    else:
        st.warning('Nenhum ator/atriz encontrado.')

    st.title('Cadastrar novo Ator/Atriz')
    name = st.text_input('Nome do Ator/Atriz')
    birthday = st.date_input(
        label='Data de Nascimento',
        value=datetime.today(),
        min_value=datetime(1900, 1, 1),
        max_value=datetime.today(),
        format='DD/MM/YYYY',
    )
    nationality_dropdown = [
        'EUA',
        'BRAZIL',
        'ARG',
        'MEX',
        'COL',
        'ES',
        'FRA',
        'ITA',
        'GER',
        'UK',
        'PR',
        'AU', 
        'ZA', 
        'NZ', 
        'Nova Zelândia',
        ]
    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown,
    )
    biography = st.text_area('Biografia')
    if st.button('Cadastrar'):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality,
            biography=biography
        )
        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao cadastrar ator/atriz.')
