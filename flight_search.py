#This class is responsible for talking to the Flight Search API.
import requests
import os


class FlightSearch:

    def __init__(self, city):
        self.params = {
            "term": city,
            "location_types": "airport"
        }
        self.header = {
            "accept": "application/json",
            "apikey": os.environ["KIWI_APIKEY"]
        }
        self.getIATA()


    #With the given city, return the airport's IATA Code
    def getIATA(self):
        response = requests.get(url="https://api.tequila.kiwi.com/locations/query",
                                params=self.params, headers=self.header)

        return response.json()["locations"][0]["id"]
