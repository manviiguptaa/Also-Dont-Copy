import requests
from bs4 import BeautifulSoup
import json
import csv

url = "https://www.levi.in/stores"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

store_json = soup.find("div", {"id": "storeJSON"}).text
stores = json.loads(store_json)
store = stores[55]

store_name = store["storename"]
address = store["address1"]
postal_code = store["postalCode"]
phone_number = store["phone"]
latitude = store["latitude"]
longitude = store["longitude"]
hours = store["hours"]


with open("store_info.csv", mode= "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Store Name", "Address", "Postal Code", "Phone Number", "Latitude", "Longitude", "Hours"])
    writer.writerow([store_name, address, postal_code, phone_number, latitude, longitude, hours])
