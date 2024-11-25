import unittest
from src.scraper import scrape_data


class TestScraper(unittest.TestCase):
    def test_scrape_data(self):
        url = "https://www.mercadolibre.com.co/tarjetas-graficas"
        result = scrape_data(url)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)


if __name__ == "__main__":
    unittest.main()
