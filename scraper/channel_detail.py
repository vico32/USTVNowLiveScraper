from utils.selenium_utils import get_webdriver
import time
from bs4 import BeautifulSoup

def get_channel_details(channel_url):
    """Extrae la URL del directo y la EPG de la página de cada canal."""
    driver = get_webdriver()
    details = {}
    try:
        driver.get(channel_url)
        time.sleep(5)  # Ajusta el tiempo de espera según sea necesario

        # Extraer el HTML cargado con Selenium
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        # Buscar el iframe del video (streaming)
        iframe = soup.find("iframe")
        if iframe and iframe.get("src"):
            details["direct_url"] = iframe.get("src")
        else:
            details["direct_url"] = None
        
        # Buscar el widget de EPG; se asume que tiene una clase específica
        epg_section = soup.find("div", class_="tv-schedule-widget")
        if epg_section:
            # Extraer el texto del EPG (por ejemplo, los programas "Now" y "Next")
            epg_items = []
            for p in epg_section.find_all("p"):
                epg_items.append(p.get_text(strip=True))
            details["epg"] = " | ".join(epg_items)
        else:
            details["epg"] = None
    except Exception as e:
        print(f"Error al procesar {channel_url}: {e}")
        details = None
    finally:
        driver.quit()
    return details
