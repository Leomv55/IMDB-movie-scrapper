import requests

from .config import IMDB_CONFIG


class IMDBApiClient:

    def __init__(self, imdb_config={}):
        config = imdb_config or IMDB_CONFIG
        self.base_url = config["base_url"]
        self.headers = config["headers"]

    def search(self, query):
        search_url = f"{self.base_url}/search/title/?title={query}"
        response = requests.get(search_url, headers=self.headers)
        return response

    def get_movie(self, movie_id):
        movie_url = f"{self.base_url}/title/{movie_id}"
        response = requests.get(movie_url, headers=self.headers)
        return response
