#This class is responsible for talking to the Google Sheet.
import requests
import os


class DataManager:

    def __init__(self, data):
        header = {
            "Authorization": os.environ["SHEETY_BEARER"]
        }

        for row in data:
            sheety_params = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            id = row["id"]
            endpoint = f"https://api.sheety.co/518a3bccbf3dabcfc20cea826ffa056d/flightDeals/prices/{id}"

            requests.put(url=endpoint, json=sheety_params, headers=header)
