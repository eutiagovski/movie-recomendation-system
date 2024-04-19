"""
# Sistema de Recomendações de Filmes

Ref. 
https://moviesway.streamlit.app/
https://github.com/vikramr22/moviesway-v2/blob/main/app.py

"""
import os
import wget
import pandas as pd
import streamlit as st
from numpy import load
from recomendation import MovieRecomendation

DATA_MOVIES_URL = 'https://raw.githubusercontent.com/eutiagovski/movie-recomendation-system/master/data/movies.tsv'
DATA_COUSINE_SIM_URL = 'https://github.com/eutiagovski/movie-recomendation-system/raw/master/data/cousine_sim.npz'

##### BACKEND #####
# @st.cache_resource
# class MovieRecomendation:
#     def __init__(self):
#         self.movies = pd.read_csv('./data/movies.tsv', sep='\t')
#         self.cousine_sim = load('./data/cousine_sim.npz')['arr_0']
#         self.titles = dict(zip(self.movies.tconst, self.movies.primaryTitle_ptBr))

#     def searchMovies(self, primaryTitle):
#         """Return movies titles with the given input"""
#         movies = self.movies
#         movies = movies.loc[movies.primaryTitle_ptBr.str.lower().str.contains(primaryTitle.lower())]
#         movies =  movies.sort_values('startYear', ascending=False)
#         return movies
    
#     def getRecomendations(self, tconst):
#         """Return recomendations based on given tconst title"""
#         # reset movies index
#         movies = self.movies
#         movies.reset_index(drop=True, inplace=True)

#         # find the index for the given movie
#         indices = pd.Series(movies.index, index=movies['tconst'])
#         idx = indices[tconst]

#         # filter similar titles
#         sim_scores = list(enumerate(self.cousine_sim[idx]))
#         sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

#         # filter the most similaries titles (exclude the first one - itself)
#         sim_scores = sim_scores[1:11]

#         movie_indices = [i[0] for i in sim_scores]

#         movies = movies.iloc[movie_indices].sort_values('startYear', ascending=False)
#         return movies


@st.cache_resource
def get_data_from_github():
    try:
        movies = pd.read_csv('./data/movies.tsv', sep='\t')
    except:
        wget.download(DATA_MOVIES_URL, f'{os.path.abspath(os.getcwd())}/data')
        movies = pd.read_csv('./data/movies.tsv', sep='\t')

    try:
        cousine_sim = load('./data/cousine_sim.npz')['arr_0']        
    except: 
        wget.download(DATA_COUSINE_SIM_URL, f'{os.path.abspath(os.getcwd())}/data')
        cousine_sim = load('./data/cousine_sim.npz')['arr_0']        

    return movies, cousine_sim

##### FRONT END #####

# initial page configuration
st.set_page_config(layout="wide",
                   page_title='Recomenda Ae',
                   page_icon='🎬')

with st.columns([0.10, 0.8, 0.10])[1]:
    v = st.write(""" <h1> <b style="color:red">🎬 Recomenda Ae</b> </h1>""",unsafe_allow_html=True)
    st.write(""" <p> Olá, bem vindo ao <b style="color:red">Recomenda Ae</b>. Sistema de recomendação de filmes e séries de tv baseado em conteúdo.""",unsafe_allow_html=True)

    data_load_state = st.text("Loading movies dataset...")

    movies, cousine_sim = get_data_from_github()

    model = MovieRecomendation(movies, cousine_sim)
    data_load_state.text("")


    tab1, tab2, tab3 = st.tabs(["Recomendação", "Mais Procurados", "Sobre o Projeto"])
    st.write('#')
    st.write('####')

    with tab1:
        selected_movie = st.selectbox(label="Escolha um Filme ou Série de TV",
                                        options=model.movies,
                                        index=None,
                                        format_func=lambda t: model.titles[t])

        if selected_movie:
            st.write('######')
            st.subheader("Aqui estão alguns outros filmes que você possa gostar:")
            st.write('######')

            recomended_titles = model.getRecomendations(selected_movie)

            with st.container():
                for index, title in recomended_titles.iterrows():
                    col1, col2 = st.columns([0.20, 0.80])
                    # col1.image(title.image_url)
                    col1.write(f"""<div style="display: flex; justify-content:center;"><img src={title.image_url} /></div>""",unsafe_allow_html=True)
                    col2.write(f' <h4> {title.primaryTitle_ptBr} </h4>',unsafe_allow_html=True)
                    col2.write(f"""<p> {'Filme' if title.titleType == 'movie' else 'Série de TV'} - {title.startYear} - Score: {round(title.score, 2)} - IMDB: {round(title.averageRating, 2)}</p>""",unsafe_allow_html=True)
                    col2.write(f"""<p> {title.overview} </p>""", unsafe_allow_html=True)
                    st.divider()

    with tab2:
        st.subheader("Top 10 Filmes")
        top_movies = model.movies.sort_values(by='score', ascending=False, axis=0).loc[model.movies.titleType == 'movie'][:10]

        for index, title in top_movies.iterrows():
                    col1, col2 = st.columns([0.25, 0.75])
                    col1.image(title.image_url)
                    col2.write(f' <h4> {title.primaryTitle_ptBr} </h4>',unsafe_allow_html=True)
                    col2.write(f"""<p> {'Filme' if title.titleType == 'movie' else 'Série de TV'} - {title.startYear} - Score: {round(title.score, 2)} - IMDB: {round(title.averageRating, 2)}</p>""",unsafe_allow_html=True)
                    col2.write(f"""<p> {title.overview} </p>""", unsafe_allow_html=True)
                    st.divider() 

            
    with tab3:
        st.write("##")

        st.caption('Esse é um Sistema de Recomendação de Filmes e Séries de TV baseado em Conteúdo.')
        st.caption('A base de dados será atualizada mensalmente, o que significa que novos filmes e séries serão sempre adicionados. 😎')   #:blue[:sunglasses:]
        st.caption("A base de dados utilizada para este projeto foi construida a partir da base de dados do IMDB.")
        st.caption("Para maiores informações acesse o projeto no github ⭐ at https://github.com/eutiagovski/movie-recomendation-system")