import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from reviews.service import ReviewService
from movies.service import MovieService


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()
    

    if reviews: 
        st.write('Lista de Avaliações')

        reviews_df = pd.json_normalize(reviews)

        AgGrid(
            data=reviews_df,
            reload_data=True,
            key='actors_grid',
        )
    else:
        st.warning('Nenhuma avaliação encontrada.')

    st.title('Cadastrar nova avaliação')
    
    movie_service = MovieService()
    movies = movie_service.get_movies()
    movies_titles = {movie['title']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Filme', list(movies_titles.keys()))

    stars = st.number_input('Estrelas', min_value=1, max_value=5, step=1)
    comment = st.text_area('Comentário')

    if st.button('Cadastrar'):
        new_review = review_service.create_review(
            movie=movies_titles[selected_movie_title],
            stars=stars,
            comment=comment,
        )
        if new_review:
            st.rerun()
        else:
            st.error('Erro ao cadastrar avaliação.')


