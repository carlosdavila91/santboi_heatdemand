import requests
import pandas as pd
from bs4 import BeautifulSoup

api_url = "http://openstreetmap.org/api/0.6/map?bbox={},{},{},{}"

bbox = (2.0224, 41.3349, 2.0480, 41.3514)

response = requests.get(api_url.format(bbox[0], bbox[1], bbox[2], bbox[3]))
html_response = response.content

print(html_response)
