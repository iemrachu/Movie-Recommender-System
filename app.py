import streamlit as st
import pickle
import requests

st.set_page_config(layout="wide")

def fetch_poster(movie_id):
   response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=05b28ac8dfd9b2fd7562d31022fe3116&language=en-US&external_source=imdb_id'.format(movie_id))
   data = response.json()
   return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_l = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    #print(movies_l)
    recommended_movies = []
    recommended_posters = []
    for i in movies_l:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch poster from api
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_posters

movies = pickle.load(open('moviess.pkl','rb'))
movies_list = movies['title'].values

st.title('Movie Recommender System')

similarity = pickle.load(open('similarity.pkl','rb'))
selected_movie = st.selectbox(
    'Which movie would you like to watch?'
    ,movies_list
)

if st.button('Recommend'):
    names,posters = recommend(selected_movie)
    col1, col2, col3, col4,col5 = st.columns(5)

    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[2])
        st.image(posters[2])
    with col4:
        st.header(names[3])
        st.image(posters[3])
    with col5:
        st.header(names[4])
        st.image(posters[4])
    # Add chart #4
