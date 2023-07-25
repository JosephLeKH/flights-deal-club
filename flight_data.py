#This class is for getting the price data and destination cities from the Google Sheet
import requests
import os


class FlightData:

    def __init__(self):
        self.header = {
            "Authorization": os.environ["SHEETY_BEARER"]
        }
        self.response = requests.get(url="https://api.sheety.co/518a3bccbf3dabcfc20cea826ffa056d/flightDeals/prices",
                                     headers=self.header)
        self.data = self.response.json()["prices"]


