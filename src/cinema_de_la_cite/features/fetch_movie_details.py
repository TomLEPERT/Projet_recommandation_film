import requests

def get_movie_details(imdb_id: str):
    """
    Récupère poster + résumé depuis IMDb API

    Paramètre
    ---------
    imdb_id : str
        ex: 'tt0211915'

    Retour
    ------
    dict:
        {
            'summary'
            'poster'
        }
    """    
    BASE_URL = "https://api.imdbapi.dev"

    # ---------- Resumé ----------
    title_url = f"{BASE_URL}/titles/{imdb_id}"

    try:
        title_resp = requests.get(title_url, timeout=10)
        title_resp.raise_for_status()
        title_data = title_resp.json()
    except Exception as e:
        print(f"Erreur IMDb title: {e}")
        return None

    plot_data = title_data.get("plot")

    plot = (
        plot_data.get("plotText", {}).get("plainText")
        if isinstance(plot_data, dict)
        else plot_data if isinstance(plot_data, str)
        else None
    )

    # ---------- 2. Images ----------
    images_url = f"{BASE_URL}/titles/{imdb_id}/images"

    poster = None
    try:
        images_resp = requests.get(images_url, timeout=10)
        images_resp.raise_for_status()
        images_data = images_resp.json()

        images = images_data.get("images", [])
        if images:
            # On prend le premier poster disponible
            poster = images[0].get("url")

    except Exception as e:
        print(f"Erreur IMDb images: {e}")

    return {
        "summary": plot,
        "poster": poster
    }