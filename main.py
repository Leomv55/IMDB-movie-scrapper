import argparse
import logging

from imdb_scrapper.controller import IMDBController
from imdb_scrapper.utils import write_to_json

logging.basicConfig(level=logging.INFO)
stdlogger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="string to be queried in IMDB", type=str)
    args = parser.parse_args()

    controller = IMDBController()

    stdlogger.info(f"Searching for '{args.query}' in IMDB ...")
    movie_ids = controller.get_movie_ids(args.query)
    stdlogger.info(f"Found {len(movie_ids)} movies for '{args.query}'")

    movie_details = []
    for movie_id in movie_ids:
        movie_detail = controller.get_movie_details(movie_id)
        if not movie_detail:
            continue

        movie_details.append(movie_detail)
        stdlogger.info(f"Scrapped details for movie: {movie_detail['title']} ({movie_id})")

    try:
        movie_file = write_to_json(movie_details)
    except Exception:
        stdlogger.exception("Failed to write movie details to file")
        return

    stdlogger.info(f"Successfully written movie details to {movie_file.name}")


if __name__ == "__main__":
    main()
