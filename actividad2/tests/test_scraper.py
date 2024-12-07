import os
import unittest
from src.scraper import scrape_mercadolibre


class TestScraper(unittest.TestCase):
    def test_scrape_data(self):
        """Prueba la función scrape_mercadolibre con un archivo HTML local."""
        # Ruta relativa al archivo de prueba
        test_file_path = os.path.join(os.getcwd(), "tests", "pagina.html")

        # Llama a la función con la ruta del archivo
        result = scrape_mercadolibre(test_file_path)

        # Validar los resultados
        self.assertIsInstance(result, list, "El resultado no es una lista")
        self.assertGreater(len(result), 0, "La lista de resultados está vacía")
        self.assertIn(
            "Título", result[0], "Falta el campo 'Título' en los resultados")
        self.assertIn(
            "Precio", result[0], "Falta el campo 'Precio' en los resultados")


if __name__ == "__main__":
    unittest.main()
