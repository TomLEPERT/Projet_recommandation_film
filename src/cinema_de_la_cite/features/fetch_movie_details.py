import requests

TMDB_API_KEY = "80bdcfa3b71bee1feef4976da6ba525a"
BASE_URL = "https://api.themoviedb.org/3"

def get_movie_details(tmdb_id: int):
    url = f"{BASE_URL}/movie/{tmdb_id}"
    params = {
        "api_key": TMDB_API_KEY,
        "language": "fr-FR"
    }

    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        print("Erreur TMDB :", e)
        return None

    return {
        "summary": data.get("overview"),
        "poster": (
            f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
            if data.get("poster_path") else None
        )
    }