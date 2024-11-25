import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re


def scrape_mercadolibre(file_path_or_url):
    """
    Extrae información de productos desde una URL o archivo HTML local.

    Args:
        file_path_or_url: La URL de la página o la ruta del archivo HTML.

    Returns:
        Una lista de diccionarios con la información extraída o un mensaje de error.
    """
    try:
        # Si es una URL
        if file_path_or_url.startswith("http://") or file_path_or_url.startswith("https://"):
            response = requests.get(file_path_or_url)
            response.raise_for_status()
            html_content = response.content
        else:
            # Si es un archivo local
            with open(file_path_or_url, "r", encoding="utf-8") as f:
                html_content = f.read()

        # Analizar el HTML
        soup = BeautifulSoup(html_content, "html.parser")

        # Extraer productos
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


def crear_grafico_precios(resultados):
    """
    Crea un gráfico de barras con los precios de los productos.

    Args:
        resultados: Lista de diccionarios con 'Título' y 'Precio' de los productos.
    """
    # Extraer títulos y precios
    titulos = [producto["Título"] for producto in resultados]

    precios = []
    for producto in resultados:
        precio_texto = producto["Precio"]
        precio_texto = re.sub(r"\d+% OFF", "", precio_texto)
        precio_texto = re.sub(r"[^\d.,]", "", precio_texto)
        precio_texto = precio_texto.replace(".", "").replace(",", ".")
        precios.append(float(precio_texto))

    # Crear el gráfico
    plt.figure(figsize=(12, 6))
    plt.bar(titulos, precios, color="skyblue")
    plt.xlabel("Productos")
    plt.ylabel("Precio (COP)")
    plt.title("Precios de los Productos en Mercado Libre")
    plt.xticks(rotation=90, ha="right")
    plt.tight_layout()
    plt.show()
