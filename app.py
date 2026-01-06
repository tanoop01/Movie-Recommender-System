import os
import pickle
import streamlit as st
import pandas as pd

BASE_DIR = os.path.dirname(__file__)


def load_data():
    movies_dict = pickle.load(
        open(os.path.join(BASE_DIR, "movie_dict.pkl"), "rb")
    )
    movies = pd.DataFrame(movies_dict)

    similarity = pickle.load(
        open(os.path.join(BASE_DIR, "similarity.pkl"), "rb")
    )

    return movies, similarity


movies, similarity = load_data()


# Recommendation function
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:11]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# UI
st.header("Watch some movies... 🎬")

selected_movie_name = st.selectbox(
    "Get movies of your genre... 📋",
    movies["title"].values
)

if st.button("Bring it on... 🍿"):
    recommended_movie_names = recommend(selected_movie_name)

    for movie in recommended_movie_names:
        st.write(movie)
