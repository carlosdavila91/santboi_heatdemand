import requests
import pandas as pd
from bs4 import BeautifulSoup

buildings = pd.read_csv("../santboi/data/1906SB_collection_clean.csv")

# print(buildings.head())
refs = buildings.ref_cat
# Clean refcats to 14 items
refs = [r.strip()[:15] for r in refs]

api_url = "http://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx/Consulta_CPMRC"

html_responses = []
for r in refs:
    params = {
        "Provincia" : "BARCELONA",
        "Municipio" : "SANT BOI DE LLOBREGAT",
        "SRS": "EPSG:4258",
        "RC":str(r)
    }
    response = requests.get(api_url, params=params)
    html_responses.append(response.content)

coordinates_dict = {
    "ref_cat":refs,
    "x_coord":[],
    "y_coord":[]
}

for html in html_responses:
    soup = BeautifulSoup(html, "html.parser")
    try:
        x = soup.find("xcen").string
    except:
        x = None
    try:
        y = soup.find("ycen").string
    except:
        y = None

    coordinates_dict["x_coord"].append(x)
    coordinates_dict["y_coord"].append(y)

coordinates_df = pd.DataFrame.from_dict(coordinates_dict)

coordinates_df.to_csv("scrape/coordinates.csv", index=False)
