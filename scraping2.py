import requests
from bs4 import BeautifulSoup
import pandas as pd 
from urllib.parse import urljoin


url = "https://aliss.do/belleza-y-cuidado-personal/fragancias"

# Hacer la solicitud GET a la URL
soli = requests.get(url)
# Verificar el estado de la solicitud
soup = BeautifulSoup(soli.text, 'html.parser')



#extraer el titulo de la pagina
titulo = soup.title.string
print("el titulo de la pagina es:", {titulo})





# Buscar productos y precios con su imagenes
productos = soup.find_all('a', class_='product-item-link')
precios = soup.find_all('span', class_='price-container price-final_price tax weee')
imagenes= soup.find_all('img', class_='product-image-photo')

print("\nPRODUCTOS Y PRECIOS ENCONTRADOS:")

#para obtener el texto y no el html
for producto,precio,imagenes in zip(productos, precios, imagenes):
    producto_texto = producto.text.strip()
    precio= precio.text.strip()
    link_producto = urljoin(url, producto.get('href'))#combinamos el url con el href
    imagenes= imagenes.get('src')#buscar los link de las imgaenes
    

    #imprimos el producto y el precio
    print(f"\nPRODUCTO: {producto_texto}")
    print(f"PRECIO: {precio}")
    print(f"IMAGENES: {imagenes}")
    print(f"ENLACE DEL PRODUCTO: {link_producto}")
    print("\n")
 


# creamos un contador para limitar la cantidad de links que se imprimen
contador_maximo=5
contador=0
# Buscar todos los enlaces en la página
links = soup.find_all('a')
print ("\nlos links encontrados de la pagina son:")

for link in links:
  if contador >= contador_maximo:
    break
 
  link_url = urljoin(url, link.get('href'))#combinamos el url con el href
  print("\n" , link_url)
  contador += 1