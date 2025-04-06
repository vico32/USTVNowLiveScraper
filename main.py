from scraper.channels import get_channels
from scraper.channel_detail import get_channel_details

def main():
    print("Obteniendo la lista de canales...")
    channels = get_channels()
    
    print(f"Se encontraron {len(channels)} canales:")
    for channel in channels:
        print(f"- {channel['name']} => {channel['url']}")
    
    # Para cada canal, obtener detalles (URL directo y EPG)
    for channel in channels:
        print(f"\nProcesando canal: {channel['name']}")
        details = get_channel_details(channel['url'])
        if details:
            print(f"Directo: {details.get('direct_url', 'No encontrado')}")
            print(f"EPG: {details.get('epg', 'No encontrado')}")
        else:
            print("No se pudo extraer detalles.")

if __name__ == "__main__":
    main()
