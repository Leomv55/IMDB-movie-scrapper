import argparse
import logging
import asyncio

from imdb_scrapper.controller import IMDBController
from imdb_scrapper.exceptions import IMDBRequestException
from imdb_scrapper.utils import write_to_json

logging.basicConfig(level=logging.INFO)
stdlogger = logging.getLogger(__name__)


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="string to be queried in IMDB", type=str)
    args = parser.parse_args()

    controller = IMDBController()
    stdlogger.info(f"Searching for '{args.query}' in IMDB ...")

    try:
        movie_ids = await controller.get_movie_ids_async(args.query)
        stdlogger.info(f"Found {len(movie_ids)} movies for '{args.query}'")

        movie_details = await asyncio.gather(*[
            controller.get_movie_details_async(movie_id)
            for movie_id in movie_ids
        ])
        movie_details = [movie_detail for movie_detail in movie_details if movie_detail]

    except IMDBRequestException as e:
        stdlogger.error(e)
        return

    try:
        movie_file = write_to_json(movie_details)
    except Exception:
        stdlogger.exception("Failed to write movie details to file")
        return

    stdlogger.info(f"Successfully written movie details to {movie_file.name}")


if __name__ == "__main__":
    asyncio.run(main())
