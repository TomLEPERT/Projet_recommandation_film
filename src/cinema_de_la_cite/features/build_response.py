import ast

from cinema_de_la_cite.features.fetch_movie_details import get_movie_details
from cinema_de_la_cite.features.clean_list_column import clean_list_column

def build_response(movie_row):
    imdb_id = movie_row["imdb_id"]

    imdb_data = get_movie_details(imdb_id)
    
    genres_data = movie_row["genres_list"]
    if isinstance(genres_data, str):
        genres = ast.literal_eval(genres_data)
    else:
        genres = genres_data

    return {
        "imdb_id": imdb_id,
        "title": movie_row["original_title"],
        "year": int(movie_row["year"]),
        "genres": genres,
        "actors": clean_list_column(movie_row["actor_list"]),
        "producers": clean_list_column(movie_row["production_companies_name_list"]),
        "writers": clean_list_column(movie_row.get("writer_list", "")),
        "summary": imdb_data["summary"] if imdb_data else None,
        "poster": imdb_data["poster"] if imdb_data else None
    }