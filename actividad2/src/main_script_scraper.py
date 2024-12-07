from scraper import scrape_mercadolibre, crear_grafico_precios


def main():
    """
    Función principal que coordina la extracción y visualización de datos.
    """
    # Especifica la ruta del archivo local o la URL de la página
    file_path_or_url = "tests/pagina.html"  # Cambiar según el origen de datos

    # Llama a la función para extraer los datos
    resultados = scrape_mercadolibre(file_path_or_url)

    # Verifica que los resultados sean válidos antes de intentar graficar
    if isinstance(resultados, list) and len(resultados) > 0:
        print("Datos extraídos correctamente. Generando gráfico...")
        crear_grafico_precios(resultados)
    else:
        print("Error en la extracción de datos:", resultados)


if __name__ == "__main__":
    main()
