from flask import request
import pandas as pd
import joblib
from flask import Flask
from flask import Response
from flask_cors import CORS 

movies, cousine_sim = joblib.load('../models/model_v1.joblib')

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    html = ''
    with open('./templates/index.html', encoding='utf-8') as f:
        for i in f:
            html += i
    html = html.encode('utf-8')
    return html

@app.route('/about')
def about():
    return "Hello, About!"

@app.route('/search', methods=['GET'])
def search_movies():
    req_title = str(request.args.get('title', ''))

    s_movies = movies.loc[movies.primaryTitle_ptBr.str.lower().str.contains(req_title)]
    s_movies =  s_movies.sort_values('startYear', ascending=False)

    return Response(s_movies.to_json(orient="records"), mimetype='application/json')

@app.route('/recomend', methods=['GET'])
def get_recomendations():
    # get tconst from url args
    tconst = str(request.args.get('tconst', ''))

    # reset movies index
    movies.reset_index(drop=True, inplace=True)

    # find the index for the given movie
    indices = pd.Series(movies.index, index=movies['tconst'])
    idx = indices[tconst]

    # filter similar titles
    sim_scores = list(enumerate(cousine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:11]

    movie_indices = [i[0] for i in sim_scores]

    r_movies = movies.iloc[movie_indices].sort_values('startYear', ascending=False)

    return Response(r_movies.to_json(orient="records"), mimetype='application/json')

@app.route('/movies', methods=['GET'])
def get_movies():
    return Response(movies.to_json(orient="records"), mimetype='application/json')