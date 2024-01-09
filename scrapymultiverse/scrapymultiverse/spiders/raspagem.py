import os
import requests
from bs4 import BeautifulSoup

def get_image_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('a', {'data-bsrjs': True})
    image_links = [img['data-bsrjs'] for img in images if 'data-bsrjs' in img.attrs]
    
    return image_links

# Substitua 'https://www.example.com' pela URL do site que você deseja analisar
image_links = get_image_links(#colocar a url do site)

#for link in image_links:
#    print(link)

def download_images(image_links, download_path):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    for i, link in enumerate(image_links):
        print(f"[+] Download {link}")
        response = requests.get(link)

        with open(os.path.join(download_path, f'image{i}.jpg'), 'wb') as f:
            f.write(response.content)

# Substitua '/path/to/download' pelo caminho onde você deseja salvar as imagens
download_images(image_links, #colocar o caminho onde vai salvar as imagens)
