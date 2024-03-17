# IMDb Scraper
<div>
<img src="./assets/IMDB_logo.png" width="50"></img>
<img src="./assets/Python_logo.png" width="30"></img>
</div>


## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Description
The IMDB Scraper is a Python script that allows you to scrape movie data from the IMDb website. It retrieves information such as movie titles, ratings, cast members, and saves it in a structured format for further analysis or use.

## Features
1. Scrapes movie data from IMDb
2. Retrieves movie titles, ratings, directors, and cast members
3. Saves data in a structured format JSON format

## Installation
1. Clone the repository: `git clone https://github.com/Leomv55/IMDB-movie-scrapper.git`
2. Navigate to the project folder: `cd IMDB-movie-scrapper`
2. Install the required dependencies: `pip3 install pipenv && pipenv install`

## Usage
1. Run the script: `pyenv run python main.py "<query>"`, where `<query>` is the movie title you want to search for.
3. The script will scrape the data and save it in `output` dir.


## Example
Sample output:

```
[
    {
        "title": "The Matrix",
        "release_date": "1999",
        "ratings": "8.7",
        "directors": [
            "Lana Wachowski",
            "Lilly Wachowski"
        ],
        "cast": [
            "Keanu Reeves",
            "Laurence Fishburne",
            "Carrie-Anne Moss"
        ],
        "plot_summary": "When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence."
    },...
]
```

Recording:
<img src="./assets/recording.gif"></img>

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any questions or inquiries, please contact [leomv3@gmail.com](mailto:leomv3@gmail.com).
