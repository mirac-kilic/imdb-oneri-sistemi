import pandas as pd
import numpy as np
import requests
from sklearn.metrics.pairwise import cosine_similarity


genre_translation = {
    "action": "Aksiyon",
    "adventure": "Macera",
    "animation": "Animasyon",
    "biography": "Biyografi",
    "comedy": "Komedi",
    "crime": "Suç",
    "drama": "Dram",
    "family": "Aile",
    "fantasy": "Fantastik",
    "history": "Tarih",
    "horror": "Korku",
    "music": "Müzik",
    "musical": "Müzikal",
    "mystery": "Gizem",
    "romance": "Romantik",
    "sci-fi": "Bilimkurgu",
    "sport": "Spor",
    "thriller": "Gerilim",
    "war": "Savaş",
    "western": "Western"
}


def get_movie_with_api(title, api_key):
    url_api = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    response = requests.get(url_api)
    data = response.json()

    if data['Response'] == 'True':
        return {
            'title': data['Title'],
            'genres': data['Genre'].lower().replace(" ", ""),
            'imdb_rating': float(data['imdbRating']) if data['imdbRating'] != "N/A" else 0,
            'num_votes': int(data['imdbVotes'].replace(",", "")) if data['imdbVotes'] != "N/A" else 0
        }
    else:
        print("❌ Film bulunamadı:", data['Error'])
        return None


def print_entered_movie_info(movie_info):
    print("\n🎬 Film Bilgisi")
    print("----------------------------")
    print(f"🎞️ Film Adı     : {movie_info['title']}")
    print(f"🎭 Türü         : {translated_genres(movie_info['genres'])}")
    print(f"⭐ IMDb Puanı   : {movie_info['imdb_rating']}")
    print(f"👥 Oy Sayısı    : {movie_info['num_votes']}")


def weighted_similarity(input_vector, matrix, weights):
    input_weighted = input_vector * weights
    matrix_weighted = matrix * weights
    return cosine_similarity(input_weighted, matrix_weighted)


def prepare_input_vector(movie_info, genre_columns):
    genre_vector = pd.Series(0, index=genre_columns)
    for g in movie_info['genres'].split(','):
        if g in genre_columns:
            genre_vector[g] = 1

    rating = movie_info['imdb_rating']
    log_votes = np.log10(movie_info['num_votes'] + 1)

    full_vector = np.concatenate([
        genre_vector.values,
        [rating, log_votes]
    ]).reshape(1, -1)

    return full_vector


def recommend_from_user_input(title, api_key, df, genre_columns, weights, X_combined, top_n=5):
    movie_info = get_movie_with_api(title, api_key)
    if movie_info is None:
        return

    print_entered_movie_info(movie_info)
    input_vector = prepare_input_vector(movie_info, genre_columns)
    similarities = weighted_similarity(input_vector, X_combined, weights)[0]
    sorted_indices = similarities.argsort()[::-1]

    input_title_lower = movie_info['title'].strip().lower()
    filtered_indices = [i for i in sorted_indices if df.iloc[i]['title'].strip().lower() != input_title_lower]
    similar_indices = filtered_indices[:top_n]
    print(f"\n🎯 '{movie_info['title']}' filmine en çok benzeyen {top_n} öneri:")

    j=1
    for i in similar_indices:
        row = df.iloc[i]
        print("{}. {} - IMDb: {}, Oy: {}".format(j,row['title'],row['averageRating'],row['numVotes']))
        j+=1
def translated_genres(genre_str):
    genres = genre_str.split(',')
    translated = [genre_translation.get(g.strip(), g.strip()) for g in genres]
    return ', '.join(translated)


if __name__ == "__main__":
    # 1. CSV verisini yükle
    df = pd.read_csv("data.csv")
    """pd.set_option('display.max_columns',500)
    pd.set_option('display.width',500)
    print(df.head())"""

    df['genres'] = df['genres'].str.lower().str.replace(" ", "")
    df['genres_tr'] = df['genres'].apply(translated_genres)
    genre_split = df['genres'].str.get_dummies(sep=',')
    df = pd.concat([df, genre_split], axis=1)
    genre_columns = genre_split.columns
    df['log_votes'] = np.log10(df['numVotes'] + 1)
    weights = np.array([1.0] * len(genre_columns) + [0.3, 0.3])
    X_combined = np.concatenate([
        df[genre_columns].values,
        df[['averageRating', 'log_votes']].values
    ], axis=1)

    api_key = "c292e310"
    while True:
        film_adi = input('\nFilm Adını Giriniz: ')
        if film_adi.lower()=='q':
            break
        recommend_from_user_input(film_adi, api_key, df, genre_columns, weights, X_combined)
        print('------------------------------------------------------')




