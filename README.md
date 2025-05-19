# 🎬 Movie Recommender System

This is a content-based movie recommendation system built with **Python**, **Streamlit**, and **The Movie Database (TMDB) API**. It recommends 5 movies similar to a selected movie and displays their posters. If no poster is available, a default placeholder image is shown.

## 🚀 Features

    - 🔎 Recommend top 5 similar movies based on the selected movie
    - 🎞️ Fetch movie posters from TMDB API
    - ⚠️ Automatically show a default image if the poster is unavailable
    - 🖥️ Simple and interactive UI built with Streamlit

---

## 🧠 How It Works

    1. Loads precomputed **cosine similarity matrix** from `similarity.pkl`
    2. Loads movie metadata from `movies.pkl`
    3. When a movie is selected, finds the top 5 most similar movies using the similarity matrix
    4. Fetches movie posters using the TMDB API
    5. If poster is unavailable at both `/original/` and `/w500/`, shows a fallback image

---

## 🛠️ Tech Stack

    - **Python**
    - **Streamlit**
    - **Pandas**
    - **Requests**
    - **Pickle**
    - **TMDB API**

---

## 📁 Folder Structure

    📦movie-recommender
    ┣ 📄 app.py
    ┣ 📄 movies.pkl
    ┣ 📄 similarity.pkl
    ┗ 📄 README.md


---

## 📝 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/movie-recommender.git
   cd movie-recommender
    ```
2. **Install Requirements** 
    ```bash
    pip install -r requirements.txt
    ```
3. **Get TMDB API Key**
    ```bash
    Sign up at TMDB
    Go to Settings → API → Generate an API key
    ```
4.  **Add your API key**
    ```bash
    Replace the API_KEY value in app.py with your TMDB API key.
    ```
5.  **Run the App**
    ```bash
    streamlit run app.py
    ```

⚠️ Notes
    - Make sure your movies.pkl has a column named id corresponding to TMDB movie IDs.

    - If a poster is not available, the app will show this default image:
    https://via.placeholder.com/500x750?text=No+Image


Let me know if you'd like me to create a `requirements.txt` or help you add screenshots or a deployed version link to the README.



# Movie-Recommendation-System
