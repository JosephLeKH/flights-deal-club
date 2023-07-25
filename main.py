"""
Purpose: Create a program that checks airline prices online and compares it to desired prices on a Google Sheet.
If the prices are lower, send emails to all users to notify them about the deal.
"""
import requests
import datetime as dt
from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
import os

#Customize starting city/airport
HOME_IATA = "DFW"

sheet_data = FlightData().data
header = {
            "accept": "application/json",
            "apikey": os.environ["KIWI_APIKEY"]
}

#If the IATA codes haven't been filled in, fill them in
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        code = FlightSearch(row["city"]).getIATA()
        row["iataCode"] = code
    DataManager(sheet_data)

#Find a cheaper flight anytime from now to 6 months from now. Must be a round trip and must be
#between 7-28 days
for row in sheet_data:
    tequila_params = {
        "fly_from": HOME_IATA,
        "fly_to": row["iataCode"],
        "date_from": dt.datetime.now().strftime("%d/%m/%Y"),
        "date_to": (dt.datetime.now() + dt.timedelta(days=180)).strftime("%d/%m/%Y"),
        "price_to": row["lowestPrice"],
        "max_stopovers": 2,
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "curr": "USD",
        "flight_type": "round"
    }

    #If a cheaper flight matching the parameters is found, send the notification
    response = requests.get(url="https://api.tequila.kiwi.com/v2/search", params=tequila_params, headers=header)
    if len(response.json()["data"]) > 0:
        NotificationManager(response.json()["data"][0])

