import requests
from bs4 import BeautifulSoup


def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = []

    for item in soup.select('.ui-search-result__wrapper'):
        title = item.select_one('.ui-search-item__title').text
        price = item.select_one('.price-tag').text
        products.append({"Título": title, "Precio": price})

    return products


if __name__ == "__main__":
    url = "https://www.mercadolibre.com.co/tarjetas-graficas"
    data = scrape_data(url)
    print(data)
