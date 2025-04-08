#scraping

import requests
from bs4 import BeautifulSoup
import pandas as pd 
from urllib.parse import urljoin


url = "https://iadpa.org/"


# Hacer la solicitud GET a la URL
soli = requests.get(url)
# Verificar el estado de la solicitud
soup = BeautifulSoup(soli.text, 'html.parser')

#extraer el titulo de la pagina
titulo=soup.title.string
print("EL TITULO DE LA PAGINA ES:", titulo)

# Buscar productos y precios
productos = soup.find_all('a', class_='product-item__title')
print("\nPRODUCTOS ENCONTRADOS:")
for producto in productos:
    print(producto.text.strip())

#buscar los precios
precios=soup.find_all('span', class_='price')
print("\nPRECIOS ENCONTRADOS:")
for precio in precios:
    print(precio.text.strip())


"""
    #extraer link de la pagina
link= soup.find_all("a" , class_="link")
for li in link:
    print(li.get("href"))
"""