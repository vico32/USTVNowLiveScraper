from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_webdriver():
    """Inicializa y retorna un driver de Selenium en modo headless."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    # Ajusta la ruta del driver si es necesario
    driver = webdriver.Chrome(options=options)
    return driver
