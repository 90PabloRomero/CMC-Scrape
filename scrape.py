import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# Función para scrapear los datos
def scrape_data(base_url, num_pages):
    all_articles = []

    for page in range(1, num_pages + 1):
        url = f"{base_url}?page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar el script que contiene __NEXT_DATA__ (como la academy esta hecha en nextjs y este se trae la data desde el server, podemos extraer directamente el json que usa para mapear los articles, genial!)
        script_tag = soup.find('script', {'id': '__NEXT_DATA__'})
        if script_tag:
            # Obtener el contenido del script y extraer el JSON
            script_content = script_tag.string.strip()
            json_data = json.loads(script_content)

            # Acceder a los datos de los artículos
            if 'props' in json_data and 'pageProps' in json_data['props'] and 'response' in json_data['props']['pageProps']:
                articles_data = json_data['props']['pageProps']['response']['pages']['data']

                for article in articles_data:
                    # Obtener los campos necesarios
                    title = article.get('title', '')
                    description = article.get('meta', '')
                    source = article['author']['name'] if 'author' in article else ''
                    link = f"https://coinmarketcap.com/academy/es/{article['slug']}"
                    image = article['image']['original'] if 'image' in article else ''
                    language = article.get('language', '')
                    created_at = article.get('created_at', '')

                    # Formatear la fecha si está presente
                    if created_at:
                        created_date = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%fZ')
                        date_str = created_date.strftime('%Y-%m-%d')
                    else:
                        date_str = datetime.now().strftime('%Y-%m-%d')  # Fecha actual si no está presente

                    # Agregar el artículo con el número de página
                    all_articles.append({
                        'title': title,
                        'description': description,
                        'source': source,
                        'link': link,
                        'image': image,
                        'language': language,
                        'date': date_str,
                        'page': page  # Número de página
                    })

    return all_articles

# Función principal
def main():
    base_url = 'https://coinmarketcap.com/academy/es/categories/cmc-research'
    num_pages = 2
    articles = scrape_data(base_url, num_pages)
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"Source: {article['source']}")
        print(f"Link: {article['link']}")
        print(f"Image: {article['image']}")
        print(f"Language: {article['language']}")
        print(f"Date: {article['date']}")
        print(f"Page: {article['page']}")  # Imprimir número de página
        print("-" * 80)

if __name__ == '__main__':
    main()
