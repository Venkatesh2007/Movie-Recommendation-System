import streamlit as st
import pickle
import requests
import pandas as pd
import gzip


API_KEY = 'f620d691cd9f3bd55423dc165c00a7bd'  

def fetch_poster(movie_id):
    fallback_image = "https://via.placeholder.com/500x750?text=No+Image"

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return fallback_image
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch poster for movie ID {movie_id}: {e}")
        return fallback_image



def recommend(movie):
    movie = movie.lower()
    index = movies[movies['title'].str.lower() == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_titles = []
    recommended_posters = []
    
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id  # Ensure you have a 'movie_id' column in your DataFrame
        recommended_titles.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    
    return recommended_titles, recommended_posters


# Streamlit frontend
st.title("🎬 Movie Recommender System")

# Load movie data and similarity matrix
with gzip.open('movies.pkl.gz', 'rb') as f:
    movies = pickle.load(f)
with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)

# Dropdown menu to select movie
movie_list = movies['title'].str.title().values
selected_movie = st.selectbox("Select a movie:", movie_list)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)
    st.subheader("Top 5 similar movies:")
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i], use_container_width=True)
            st.caption(names[i])


