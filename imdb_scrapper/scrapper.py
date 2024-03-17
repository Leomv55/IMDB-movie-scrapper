import logging
import re

from bs4 import BeautifulSoup

stdlogger = logging.getLogger(__name__)


class IMDBScrapper:

    def scrap_movie_ids(self, response):
        movie_ids = []
        soup = BeautifulSoup(response.text, "html.parser")
        all_movie_tags = soup.find_all("a", attrs={"class": "ipc-metadata-list-summary-item__t", "href": re.compile("title")})

        for tag in all_movie_tags:
            try:
                movie_ids.append(tag["href"].split("/")[2])
            except Exception as e:
                stdlogger.exception(e)

        return movie_ids

    def scrap_movie_details(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        try:
            movie = {}
            movie["title"] = soup.find("span", attrs={"class": "hero__primary-text"}).text
            movie["release_date"] = soup.find("a", attrs={"class": "ipc-link ipc-link--baseAlt ipc-link--inherit-color", "role": "button", "href": re.compile("releaseinfo")}).text
            movie["ratings"] = soup.find("div", attrs={"data-testid": "hero-rating-bar__aggregate-rating__score"}).find("span").text
            movie["directors"] = [director.text for director in soup.find_all("a", attrs={"class": "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link", "href": re.compile("name")})]
            return movie

        except Exception:
            stdlogger.exception(f"unable to scrap movie details for movie url: {response.url}")
            return {}
