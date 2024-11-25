import os
import requests
from bs4 import BeautifulSoup


def scrape_mercadolibre(file_path_or_url):
    """
    Extrae información de productos desde una URL o archivo HTML local.

    Args:
        file_path_or_url: La URL de la página o la ruta del archivo HTML.

    Returns:
        Una lista de diccionarios con la información extraída o un mensaje de error.
    """
    try:
        # Si el argumento parece una URL, usa requests; de lo contrario, lee el archivo local
        if file_path_or_url.startswith("http://") or file_path_or_url.startswith("https://"):
            response = requests.get(file_path_or_url)
            response.raise_for_status()
            html_content = response.content
        else:
            # Leer archivo local
            with open(file_path_or_url, "r", encoding="utf-8") as f:
                html_content = f.read()

        # Analizar el HTML con BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")

        # Resto de la lógica de extracción de datos
        productos = soup.find_all("li", class_="ui-search-layout__item")
        resultados = []
        for producto in productos:
            titulo_elemento = producto.find(
                "h2", class_="poly-box poly-component__title")
            titulo = titulo_elemento.text.strip() if titulo_elemento else "Título no encontrado"

            precio_elemento = producto.find(
                "div", class_="poly-price__current")
            precio = precio_elemento.text.strip() if precio_elemento else "Precio no encontrado"

            resultados.append({"Título": titulo, "Precio": precio})

        return resultados

    except requests.exceptions.RequestException as e:
        return f"Error al obtener la URL: {e}"
    except AttributeError as e:
        return f"Error al analizar el HTML: {e}. Verifica el selector CSS."
    except Exception as e:
        return f"Error inesperado: {e}"
