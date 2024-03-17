import aiohttp
import requests

from .config import IMDB_CONFIG
from .exceptions import IMDBRequestException


class IMDBClient:

    def __init__(self, imdb_config={}):
        config = imdb_config or IMDB_CONFIG
        self.base_url = config["base_url"]
        self.headers = config["headers"]

    def search(self, query):
        search_url = f"{self.base_url}/search/title/?title={query}"
        response = requests.get(search_url, headers=self.headers)
        if response.status_code != 200:
            raise IMDBRequestException(
                "Error while fetching movie list",
                status_code=response.status_code
            )
        return response.text

    def get_movie_details(self, movie_id):
        movie_url = f"{self.base_url}/title/{movie_id}"
        response = requests.get(movie_url, headers=self.headers)
        if response.status_code != 200:
            raise IMDBRequestException(
                "Error while fetching movie details",
                status_code=response.status_code
            )
        return response.text

    async def search_async(self, query):
        search_url = f"{self.base_url}/search/title/?title={query}"
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(search_url) as response:
                if response.status != 200:
                    raise IMDBRequestException(
                        "Error while fetching movie list",
                        status_code=response.status
                    )
                return await response.text()

    async def get_movie_details_async(self, movie_id):
        movie_url = f"{self.base_url}/title/{movie_id}"
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(movie_url) as response:
                if response.status != 200:
                    raise IMDBRequestException(
                        "Error while fetching movie details",
                        status_code=response.status
                    )
                return await response.text()
