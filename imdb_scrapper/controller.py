from .clients import IMDBApiClient
from .scrapper import IMDBScrapper


class IMDBController:
    def __init__(self) -> None:
        self.scrapper = IMDBScrapper()
        self.api_client = IMDBApiClient()

    def get_movie_ids(self, query):
        response = self.api_client.search(query)
        movie_ids = self.scrapper.scrap_movie_ids(response)
        return movie_ids

    def get_movie_details(self, movie_id):
        response = self.api_client.get_movie(movie_id)
        movie = self.scrapper.scrap_movie_details(response)
        return movie
