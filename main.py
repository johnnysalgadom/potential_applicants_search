import requests
import pandas as pd
import json

# People search from LinkedIn
def people_search_linkedin():

    apify_client_id = "apify_api_3F3cV1hZLr3Ze774rXnEI9ftAS8jOt0ywkMk"
    url = f"https://api.apify.com/v2/acts/curious_coder~linkedin-people-search-scraper/runs/last/dataset/items?token={apify_client_id}"
    res = requests.get(url)
    #print(res.text)


    # Parsear el texto JSON a un diccionario de Python
    data = json.loads(res.text)

    # Convertir el diccionario a un DataFrame de pandas
    df = pd.DataFrame(data)

    print(df)

    # Especificar el nombre del archivo Excel de destino
    nombre_archivo_excel = 'candidatos_data.xlsx'

    # Exportar el DataFrame a un archivo de Excel
    df.to_excel(nombre_archivo_excel, index=False)

    print(f'Los datos se han exportado a {nombre_archivo_excel} exitosamente.')


# Main function  
if __name__ == '__main__':
    query = 'developer'
    people_search_linkedin() 
