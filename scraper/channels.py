from bs4 import BeautifulSoup
from .base import get_html

BASE_URL = "https://usatvgo.live/"

def get_channels():
    """Extrae la lista de canales de la página principal."""
    html = get_html(BASE_URL)
    channels = []
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        # Buscamos los enlaces que contengan el patrón "channel.php?id="
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if "channel.php?id=" in href:
                channel_name = a_tag.find("p")
                channel_name = channel_name.get_text(strip=True) if channel_name else "Sin nombre"
                # Construir la URL completa
                channel_url = BASE_URL.rstrip("/") + "/" + href.lstrip("/")
                channels.append({
                    "name": channel_name,
                    "url": channel_url
                })
    else:
        print("No se pudo obtener el HTML de la página principal.")
    return channels
