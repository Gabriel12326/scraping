""""
Scraping a una Pagina web con Python & beautifulsoup
"""""
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
titulo = soup.title.string
print("el titulo de la pagina es:", titulo)
    


# Buscar productos y precios
productos = soup.find_all('a', class_='product-item__title')
precios = soup.find_all('div', class_='product-item__price-list price-list')

print("\nPRODUCTOS Y PRECIOS ENCONTRADOS CON SUS LINK:")

# para interactuar con los productos y precios
for producto, precio in zip(productos, precios):
    producto_texto = producto.text.strip()
    producto_url = producto.get('href')  # Obtener el enlace del producto
    link = urljoin(url, producto_url)
   
    # Extraer el precio original y el precio con descuento
    precio_original = precio.find('span', class_='price price--compare')  # Precio original
    precio_actual = precio.find('span', class_='price price--highlight')  # Precio actual (sin descuento)

    # cuando el producto tiene ambos
    if precio_original and precio_actual:
        original = precio_original.text.strip()
        actual = precio_actual.text.strip()
        print(f"\nPRODUCTO: {producto_texto}")
        print(original.upper())  
        print(actual.upper())  
        print(link)

    # cuando el producto no tiene descuento
    elif precio_actual:
        actual = precio_actual.text.strip()
        print(f"\nPRODUCTO: {producto_texto}")
        print(actual.upper()) 
        print(link)

    print(   )

#de la categoria de iglesia

iglesia = "https://iadpa.org/collections/iglesia"

# Hacer la solicitud GET a la URL
soli = requests.get(iglesia)
# Verificar el estado de la solicitud
soup = BeautifulSoup(soli.text, 'html.parser')

productos = soup.find_all('a', class_='product-item__title')
precios = soup.find_all('span', class_='price')
print("\nPRODUCTOS DE LA CATEGORIA DE IGLESIA SON:")
# Buscar productos y precios
for producto, precio in zip(productos, precios):
    producto_texto = producto.text.strip()
    precio_texto = precio.text.strip()
    producto_url = producto.get('href')  # Obtener el enlace del producto
    link = urljoin(url, producto_url)


    print(f"\nPRODUCTO: {producto_texto}")
    print(precio_texto)
    print(link)
   
    
    print(   )