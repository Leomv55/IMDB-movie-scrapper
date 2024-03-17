from unittest import TestCase
from pathlib import Path

from .exceptions import IMDBRequestException
from .clients import IMDBClient
from .scrapper import IMDBScrapper


class IMDBScrapperTest(TestCase):
    def setUp(self):
        self.scrapper = IMDBScrapper()

    def test_scrap_movie_ids(self):
        response_text = Path("samples/search_response.html").read_text()
        movie_ids = self.scrapper.scrap_movie_ids(response_text)
        # IMDB shows 50 movies in a page as default for matrix movie search
        self.assertEqual(len(movie_ids), 50)
        self.assertEqual(movie_ids, ['tt0133093', 'tt10838180', 'tt0234215', 'tt0242653', 'tt30749809', 'tt0106062', 'tt16385248', 'tt9847360', 'tt0410519', 'tt30849138', 'tt0277828', 'tt0364888', 'tt0365467', 'tt0390244', 'tt0109151', 'tt0451118', 'tt0303678', 'tt2579522', 'tt0274085', 'tt11574780', 'tt0295432', 'tt12355912', 'tt0211096', 'tt1675286', 'tt1499960', 'tt30689209', 'tt9642498', 'tt29542010', 'tt11749868', 'tt0439783', 'tt0970173', 'tt27796295', 'tt3959436', 'tt5968306', 'tt1830850', 'tt27496886', 'tt13549048', 'tt10933090', 'tt12740804', 'tt1974203', 'tt1595473', 'tt13285880', 'tt2990982', 'tt5325370', 'tt13773598', 'tt2121323', 'tt31123035', 'tt5319308', 'tt6641942', 'tt12093002'])

    def test_scrap_movie_details(self):
        original_response_text = Path("samples/movie_detail.html").read_text()
        movie_details_1 = self.scrapper.scrap_movie_details(original_response_text)
        movie_details_2 = {
            "title": "Matrix",
            "release_date": "1993",
            "ratings": "7.5",
            "directors": [],
            "cast": [
                "Nick Mancuso",
                "Phillip Jarrett",
                "Carrie-Anne Moss"
            ],
            "plot_summary": "Steven Matrix is one of the underworld's foremost hitmen until his luck runs out, and someone puts a contract out on him. Shot in the forehead by a .22 pistol, Matrix \"dies\" and finds himself in \"The City In Between\", where he is shown the faces of all the men and women he's murd... Read all"
        }
        self.assertEqual(movie_details_1, movie_details_2)

    def test_scrap_movie_details_error(self):
        original_response_text = Path("samples/movie_detail.html").read_text()
        release_date_element = '''<a class="ipc-link ipc-link--baseAlt ipc-link--inherit-color" role="button" tabindex="0" aria-disabled="false" href="/title/tt0106062/releaseinfo?ref_=tt_ov_rdat">1993</a>'''
        response_text = original_response_text
        response_text_without_release_date = response_text.replace(release_date_element, "")
        movie_details_1 = self.scrapper.scrap_movie_details(response_text_without_release_date)
        movie_details_2 = {
            "title": "Matrix",
            "release_date": None,
            "ratings": "7.5",
            "directors": [],
            "cast": [
                "Nick Mancuso",
                "Phillip Jarrett",
                "Carrie-Anne Moss"
            ],
            "plot_summary": "Steven Matrix is one of the underworld's foremost hitmen until his luck runs out, and someone puts a contract out on him. Shot in the forehead by a .22 pistol, Matrix \"dies\" and finds himself in \"The City In Between\", where he is shown the faces of all the men and women he's murd... Read all"
        }
        self.assertEqual(movie_details_1, movie_details_2)

        rating_element = '''<span class="sc-bde20123-1 cMEQkK">7.5</span>'''
        response_text = original_response_text
        response_text_without_rating = response_text.replace(rating_element, "")
        movie_details_1 = self.scrapper.scrap_movie_details(response_text_without_rating)
        movie_details_2 = movie_details_2 = {
            "title": "Matrix",
            "release_date": "1993",
            "ratings": None,
            "directors": [],
            "cast": [
                "Nick Mancuso",
                "Phillip Jarrett",
                "Carrie-Anne Moss"
            ],
            "plot_summary": "Steven Matrix is one of the underworld's foremost hitmen until his luck runs out, and someone puts a contract out on him. Shot in the forehead by a .22 pistol, Matrix \"dies\" and finds himself in \"The City In Between\", where he is shown the faces of all the men and women he's murd... Read all"
        }
        self.assertEqual(movie_details_1, movie_details_2)

        cast_element = '''Carrie-Anne Moss'''
        response_text = original_response_text
        response_text_without_cast = response_text.replace(cast_element, "")
        movie_details_1 = self.scrapper.scrap_movie_details(response_text_without_cast)
        movie_details_2 = {
            "title": "Matrix",
            "release_date": "1993",
            "ratings": "7.5",
            "directors": [],
            "cast": [
                "Nick Mancuso",
                "Phillip Jarrett"
            ],
            "plot_summary": "Steven Matrix is one of the underworld's foremost hitmen until his luck runs out, and someone puts a contract out on him. Shot in the forehead by a .22 pistol, Matrix \"dies\" and finds himself in \"The City In Between\", where he is shown the faces of all the men and women he's murd... Read all"
        }
        self.assertEqual(movie_details_1, movie_details_2)

        plot_element = '''<p data-testid="plot" class="sc-466bb6c-3 fOUpWp"><span role="presentation" data-testid="plot-xs_to_m" class="sc-466bb6c-0 hlbAws">Steven Matrix is one of the underworld&#x27;s foremost hitmen until his luck runs out, and someone puts a contract out on him. Shot in the forehead by a .22 pistol, Matrix &quot;dies&quot; and finds himsel...<!-- --> <a class="ipc-link ipc-link--baseAlt" role="button" tabindex="0" aria-disabled="false" data-testid="plot-read-all-link" href="plotsummary?ref_=tt_ov_pl">Read all</a></span><span role="presentation" data-testid="plot-l" class="sc-466bb6c-1 dWufeH">Steven Matrix is one of the underworld&#x27;s foremost hitmen until his luck runs out, and someone puts a contract out on him. Shot in the forehead by a .22 pistol, Matrix &quot;dies&quot; and finds himself in &quot;The City In Between&quot;, where he is shown the faces of all the men and women he&#x27;s murd...<!-- --> <a class="ipc-link ipc-link--baseAlt" role="button" tabindex="0" aria-disabled="false" data-testid="plot-read-all-link" href="plotsummary?ref_=tt_ov_pl">Read all</a></span><span role="presentation" data-testid="plot-xl" class="sc-466bb6c-2 chnFO">Steven Matrix is one of the underworld&#x27;s foremost hitmen until his luck runs out, and someone puts a contract out on him. Shot in the forehead by a .22 pistol, Matrix &quot;dies&quot; and finds himself in &quot;The City In Between&quot;, where he is shown the faces of all the men and women he&#x27;s murdered and a sea of fire. He&#x27;s informed that he will be given a second chance. He must earn ...<!-- --> <a class="ipc-link ipc-link--baseAlt" role="button" tabindex="0" aria-disabled="false" data-testid="plot-read-all-link" href="plotsummary?ref_=tt_ov_pl">Read all</a></span></p> '''
        response_text = original_response_text
        response_text_without_plot = response_text.replace(plot_element, "")
        movie_details_1 = self.scrapper.scrap_movie_details(response_text_without_plot)
        movie_details_2 = {
            "title": "Matrix",
            "release_date": "1993",
            "ratings": "7.5",
            "directors": [],
            "cast": [
                "Nick Mancuso",
                "Phillip Jarrett",
                "Carrie-Anne Moss"
            ],
            "plot_summary": ""
        }
        self.assertEqual(movie_details_1, movie_details_2)

        title_element = '''<span class="hero__primary-text" data-testid="hero__primary-text">Matrix</span>'''
        response_text = original_response_text
        response_text_without_title = response_text.replace(title_element, "")
        movie_details_1 = self.scrapper.scrap_movie_details(response_text_without_title)
        movie_details_2 = {}  # Title is mandatory
        self.assertEqual(movie_details_1, movie_details_2)


class IMDBClientTest(TestCase):
    def setUp(self):
        self.client = IMDBClient()

    def test_search(self):
        response_text = self.client.search("matrix")
        self.assertNotEqual("", response_text)
        # The title of the movie is present in the response and the response is valid
        self.assertIn("The Matrix", response_text)

    def test_search_error(self):
        self.client.base_url = "https://www.imdb.com/invalid"
        with self.assertRaises(IMDBRequestException):
            self.client.search("matrix")

    def test_get_movie_details(self):
        response_text = self.client.get_movie_details("tt0133093")
        self.assertNotEqual("", response_text)
        # The title of the movie is present in the response and the response is valid
        self.assertIn("The Matrix", response_text)

    def test_get_movie_details_error(self):
        self.client.base_url = "https://www.imdb.com/invalid"
        with self.assertRaises(IMDBRequestException):
            self.client.get_movie_details("tt0133093")
