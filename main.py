# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=9578c1c9b5e7287055b76d6be791d35b&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + data['poster_path']
    # eg,: https://image.tmdb.org/t/p/original/z2FnLKpFi1HPO7BEJxdkv6hpJSU.jpg
    print(data)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommend_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch_poster using API
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommend_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Select the name of the Movie to get recommendation of similar Movies:', movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown(f"<p style='text-align:center'>{names[0]}</p>", unsafe_allow_html=True)
        st.image(posters[0])
    with col2:
        st.markdown(f"<p style='text-align:center'>{names[1]}</p>", unsafe_allow_html=True)
        st.image(posters[1])
    with col3:
        st.markdown(f"<p style='text-align:center'>{names[2]}</p>", unsafe_allow_html=True)
        st.image(posters[2])
    with col4:
        st.markdown(f"<p style='text-align:center'>{names[3]}</p>", unsafe_allow_html=True)
        st.image(posters[3])
    with col5:
        st.markdown(f"<p style='text-align:center'>{names[4]}</p>", unsafe_allow_html=True)
        st.image(posters[4])

st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #0E1117;
    color: white;
    text-align: center;
    padding: 10px;
    font-size: 14px;
}

.footer a {
    color: #4CAF50;
    text-decoration: none;
    font-weight: bold;
}
</style>

<div class="footer">
    Made with ❤️ by
    <a href="https://www.linkedin.com/in/sakshamraj1/" target="_blank">
        Saksham Raj
    </a>
    | Movie Recommendation System
</div>
""", unsafe_allow_html=True)

# if st.button("Recommend"):
#     names, posters = recommend(selected_movie_name)
#
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(names[0])
#         st.image(posters[0])
#     with col2:
#         st.text(names[1])
#         st.image(posters[1])
#     with col3:
#         st.text(names[2])
#         st.image(posters[2])
#     with col4:
#         st.text(names[3])
#         st.image(posters[3])
#     with col5:
#         st.text(names[4])
#         st.image(posters[4])
#

# API Key: https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api+key>>&language=en-US