import aiohttp
import requests

from .config import IMDB_CONFIG


class IMDBClient:

    def __init__(self, imdb_config={}):
        config = imdb_config or IMDB_CONFIG
        self.base_url = config["base_url"]
        self.headers = config["headers"]

    def search(self, query):
        search_url = f"{self.base_url}/search/title/?title={query}"
        response = requests.get(search_url, headers=self.headers)
        return response.text

    def get_movie_details(self, movie_id):
        movie_url = f"{self.base_url}/title/{movie_id}"
        response = requests.get(movie_url, headers=self.headers)
        return response.text

    async def search_async(self, query):
        search_url = f"{self.base_url}/search/title/?title={query}"
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(search_url) as response:
                return await response.text()

    async def get_movie_details_async(self, movie_id):
        movie_url = f"{self.base_url}/title/{movie_id}"
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(movie_url) as response:
                return await response.text()
