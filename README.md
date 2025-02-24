# Content-based Movie Recommendation System

## Overview
The Movie Recommendation System is a content-based recommendation engine that suggests movies based on user input. Users can search for movies using a title, actor name, or any relevant keyword, and the system will find the most similar movies using TF-IDF vectorization and cosine similarity.

## Technical Architecture

**Data Collection:** A dataset of 5000 movies with titles, actor names, and descriptions.

**Preprocessing:**
* Text cleaning (removal of punctuation and stopwords, lemmatization)
* TF-IDF vectorization to convert text into numerical representation
* Dimensionality reduction using Truncated SVD

**Modeling:**
* Cosine similarity to compute movie similarities
* On-the-fly query vectorization and comparison with the movie database

**Deployment:**

* Streamlit app for user interaction
* Backend API handling recommendation queries

**API Endpoints**
* TMDB API: This is used to fetch recommended movie posters

**Dependencies**
* Python 3.8+
* pandas
* numpy
* nltk
* scikit-learn
* streamlit
* re (Regular Expressions for text cleaning)
