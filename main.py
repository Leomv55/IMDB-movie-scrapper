import argparse

from imdb_scrapper.controller import IMDBController


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="String to be queried in IMDB", type=str)
    args = parser.parse_args()

    controller = IMDBController()
    movie_ids = controller.get_movie_ids(args.query)
    for movie_id in movie_ids:
        movie = controller.get_movie_details(movie_id)
        print(movie)


if __name__ == "__main__":
    main()
