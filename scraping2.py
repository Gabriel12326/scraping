import requests
from bs4 import BeautifulSoup
import pandas as pd 
from urllib.parse import urljoin


url = "https://do.ebay.com/b/Basketballs/21208/bn_1993978"

# Hacer la solicitud GET a la URL
soli = requests.get(url)
# Verificar el estado de la solicitud
soup = BeautifulSoup(soli.text, 'html.parser')



#extraer el titulo de la pagina
titulo = soup.find('title')
print("el titulo de la pagina es:", titulo.text.strip())




# Buscar productos y precios
productos = soup.find_all('h3', class_='textual-display')
precios = soup.find_all('span', class_='bsig__price')

print("\nPRODUCTOS Y PRECIOS ENCONTRADOS:")


#para que solo lea el texto y no el html
for producto, precio, in zip(productos, precios):

    #obtener el texto del producto y el precio
    producto_texto = producto.text.strip()
    precio_texto = precio.text.strip()
    

    #obtener el enlace del producto
    producto_url = producto.get('href')
    link = urljoin(url, producto_url) #une la url de la pagina con el enlace del producto


    print(f"\nPRODUCTO: {producto_texto}")
    print(precio_texto)
    print(link)
print(   )





link= soup.find_all('a', class_='link')
for link in link:
    link_texto = urljoin(url, link.get('href')) #une la url de la pagina con el enlace del producto
    print(link_texto)