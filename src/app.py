import joblib
import pickle
import streamlit as st
import requests
import os
import pandas as pd
import numpy as np

def fetch_poster(movie_id):
    base_url = "https://image.tmdb.org/t/p/original"
    api_key = "94b22dc37c19aa244c8e511128fce6cf"
    posters = []
    for id in movie_id:
        response = requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key={api_key}")
        data = response.json()
        poster_path = data['poster_path']
        poster_url = base_url + poster_path
        posters.append(poster_url)
    return posters

# Movie Recommendation Function
def recommend_movies(movies, similarity, query, num_recommendations=5):
    # Find movies that match the given title (partial match support)
    matching_movies = movies[movies['title'].str.contains(query, case=False, na=False)]
    
    if matching_movies.empty:
        return "Movie not found!"
    
    recommendations = []
    movie_posters = []
    for idx in matching_movies.index:
        similarity_scores = list(enumerate(similarity[idx]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        top_movies = [movies.iloc[i[0]]['title'] for i in similarity_scores[1:num_recommendations+1]]
        top_movie_ids = [movies.iloc[i[0]]['movie_id'] for i in similarity_scores[1:num_recommendations+1]]
        recommendations.extend(top_movies)
        movie_posters.extend(fetch_poster(top_movie_ids))
    
    return list(recommendations), list(movie_posters)  # Remove duplicates


st.header("Content-based Movie Recommender")

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Construct the absolute paths to the pickle files
movies_path = os.path.join(current_dir, "../artifacts/movies_list.pkl")
similarity_path = os.path.join(current_dir, "../artifacts/movies_similarity.pkl")

# movies = joblib.load(movies_path)
# similarity = joblib.load(similarity_path)

movies = pickle.load(open(movies_path, "rb"))
similarity = pickle.load(open(similarity_path, "rb"))

movie_list = movies["title"].values
selected_movie = st.selectbox("Select a movie", movie_list)

if st.button("Recommend Movies"):
    recommendations, posters = recommend_movies(movies, similarity, selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5, gap="large")
    with col1:
        # st.write(recommendations[0])
        st.image(posters[0], width=150, caption=recommendations[0])
    with col2:
        # st.write(recommendations[1])
        st.image(posters[1], width=150, caption=recommendations[1])
    with col3:
        # st.write(recommendations[2])
        st.image(posters[2], width=150, caption=recommendations[2])
    with col4:
        # st.write(recommendations[3])
        st.image(posters[3], width=150, caption=recommendations[3])
    with col5:
        # st.write(recommendations[4])
        st.image(posters[4], width=150, caption=recommendations[4])