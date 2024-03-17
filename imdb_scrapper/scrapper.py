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
        movie = {
            "title": "",
            "release_date": None,
            "ratings": None,
            "directors": [],
            "cast": [],
            "plot_summary": ""
        }

        soup = BeautifulSoup(response.text, "html.parser")
        try:
            # Movie title is mandatory
            movie["title"] = soup.find("span", attrs={"class": "hero__primary-text"}).text

            release_el = soup.find("a", attrs={"class": "ipc-link ipc-link--baseAlt ipc-link--inherit-color", "role": "button", "href": re.compile("releaseinfo")})
            if release_el:
                movie["release_date"] = release_el.text

            rating_element = soup.find("div", attrs={"data-testid": "hero-rating-bar__aggregate-rating__score"})
            if rating_element:
                movie["ratings"] = rating_element.find("span").text

            directors_section = soup.find('span', text='Directors')
            if directors_section:
                movie["directors"] = [director.text for director in directors_section.parent.find_all("a", attrs={"class": "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link", "href": re.compile("name")})]

            casts_section = soup.find('a', text='Stars')
            if casts_section:
                movie["cast"] = [cast.text for cast in casts_section.parent.find_all("a", attrs={"class": "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link", "href": re.compile("name")})]

            plot_summary = soup.find("span", attrs={"data-testid": "plot-l"})
            if plot_summary:
                movie["plot_summary"] = plot_summary.text

            return movie

        except Exception:
            stdlogger.exception(f"unable to scrap movie details for movie url: {response.url}")
            return movie
