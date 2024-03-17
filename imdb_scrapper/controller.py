from .clients import IMDBClient
from .scrapper import IMDBScrapper


class IMDBController:
    def __init__(self) -> None:
        self.scrapper = IMDBScrapper()
        self.client = IMDBClient()

    def get_movie_ids(self, query):
        response = self.client.search(query)
        movie_ids = self.scrapper.scrap_movie_ids(response)
        return movie_ids

    def get_movie_details(self, movie_id):
        response = self.client.get_movie_details(movie_id)
        movie = self.scrapper.scrap_movie_details(response.text)
        return movie

    async def get_movie_ids_async(self, query):
        response_text = await self.client.search_async(query)
        movie_ids = self.scrapper.scrap_movie_ids(response_text)
        return movie_ids

    async def get_movie_details_async(self, movie_id):
        response_text = await self.client.get_movie_details_async(movie_id)
        movie = self.scrapper.scrap_movie_details(response_text)
        return movie
