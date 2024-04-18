"""
# Sistema de Recomendações de Filmes

Ref. 
https://moviesway.streamlit.app/
https://github.com/vikramr22/moviesway-v2/blob/main/app.py

"""

import streamlit as st
import pandas as pd
from numpy import load

DATA_MOVIES_URL = './data/movies.tsv'
DATA_COUSINE_SIM_URL = './data/cousine_sim.npz'

##### BACKEND #####
@st.cache_resource
class MovieRecomendation:
    def __init__(self):
        self.movies = pd.read_csv(DATA_MOVIES_URL, sep='\t')
        self.cousine_sim = load(DATA_COUSINE_SIM_URL)['arr_0']
        self.titles = dict(zip(self.movies.tconst, self.movies.primaryTitle_ptBr))

    def searchMovies(self, primaryTitle):
        """Return movies titles with the given input"""
        movies = self.movies
        movies = movies.loc[movies.primaryTitle_ptBr.str.lower().str.contains(primaryTitle.lower())]
        movies =  movies.sort_values('startYear', ascending=False)
        return movies
    
    def getRecomendations(self, tconst):
        """Return recomendations based on given tconst title"""
        # reset movies index
        movies = self.movies
        movies.reset_index(drop=True, inplace=True)

        # find the index for the given movie
        indices = pd.Series(movies.index, index=movies['tconst'])
        idx = indices[tconst]

        # filter similar titles
        sim_scores = list(enumerate(self.cousine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # filter the most similaries titles (exclude the first one - itself)
        sim_scores = sim_scores[1:11]

        movie_indices = [i[0] for i in sim_scores]

        movies = movies.iloc[movie_indices].sort_values('startYear', ascending=False)
        return movies


##### FRONT END #####

# initial page configuration
st.set_page_config(layout="centered",
                   page_title='Recomenda Ae',
                   page_icon='🎬')

# st.title('Recomenda Aê')
# st.subheader('Sistema de recomendação de filmes e séries e tv baseado em conteúdo.')
v = st.write(""" <h2> <b style="color:red">🎬 Recomenda Ae</b> </h2>""",unsafe_allow_html=True)
st.write(""" <p> Olá, bem vindo ao <b style="color:red">Recomenda Ae</b>. Sistema de recomendação de filmes e séries de tv baseado em conteúdo.""",unsafe_allow_html=True)

data_load_state = st.text("Loading movies dataset...")
model = MovieRecomendation()
data_load_state.text("")

selected_movie = st.selectbox(label="Escolha um filme ou série de tv",
                                   options=model.movies,
                                   index=None,
                                   format_func=lambda t: model.titles[t])

if selected_movie:
    st.write('######')
    st.subheader("Aqui estão alguns outros filmes que você possa gostar:")
    st.write('######')

    recomended_titles = model.getRecomendations(selected_movie)

    c = st.container()
    for index, title in recomended_titles.iterrows():
        col1, col2 = c.columns([0.25, 0.75])
        col1.image(title.image_url)
        col2.write(f' <h4> {title.primaryTitle_ptBr} </h4>',unsafe_allow_html=True)
        col2.write(f"""<p> {'Filme' if title.titleType == 'movie' else 'Série de TV'} - {title.startYear} - {round(title.score, 2)} </p>""",unsafe_allow_html=True)
        col2.write(f"""<p> {title.overview} </p>""", unsafe_allow_html=True)
        c.divider()