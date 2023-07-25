#This class is for sending SMS notification to the developer and/or emails to all users about the flight deals
#that the program finds
from twilio.rest import Client
import smtplib as sm
import requests
import os


class NotificationManager:

    #Get all the relevant information from the main data
    def __init__(self, data):
        #Customize starting city/airport
        self.cityFrom = "Dallas"
        self.cityFromIATA = "DFW"

        self.header = {
            "Authorization": os.environ["SHEETY_BEARER"]
        }
        self.data = []
        self.price = data["price"]
        self.cityTo = data["cityTo"]
        self.cityToIATA = data["flyTo"]
        self.outbound = data["route"][0]["local_departure"][:10]
        self.inbound = data["route"][len(data["route"]) - 1]["local_departure"][:10]
        self.stopover = False
        self.stopoverCity = ""
        if len(data["route"]) > 2:
            self.stopover = True
            self.stopoverCity = data["route"][1]["cityFrom"]
        self.send_emails()

    #Send a text to the developer
    def sendSMS(self):
        sid = os.environ["TWILIO_SID"]
        sms_token = os.environ["TWILIO_TOKEN"]
        client = Client(sid, sms_token)
        if self.stopover:
            message = client.messages \
                .create(
                body=f"Low price alert! Only ${self.price} to fly from {self.cityFrom}-{self.cityFromIATA} to "
                     f"{self.cityTo}-{self.cityToIATA}, from {self.outbound} to {self.inbound}."
                     f" Flight has 1 stopover, via {self.stopoverCity}.",
                from_=os.environ["BOT_NUMBER"],
                to=os.environ["DEV_NUMBER"]
            )
            print(message.status)

        else:
            message = client.messages \
                .create(
                body=f"Low price alert! Only ${self.price} to fly from {self.cityFrom}-{self.cityFromIATA} to "
                     f"{self.cityTo}-{self.cityToIATA}, from {self.outbound} to {self.inbound}.",
                from_=os.environ["BOT_NUMBER"],
                to=os.environ["DEV_NUMBER"]
            )
            print(message.status)

    #Send emails to all users
    def send_emails(self):
        response = requests.get(url="https://api.sheety.co/518a3bccbf3dabcfc20cea826ffa056d/flightDeals/users",
                                headers=self.header)
        self.data = response.json()["users"]
        for user in self.data:
            connection = sm.SMTP("smtp.gmail.com", port=587)
            connection.starttls()
            connection.login(user=os.environ["DEV_EMAIL"], password=os.environ["DEV_EMAIL_PASSWORD"])
            if self.stopover:
                connection.sendmail(
                    from_addr=os.environ["DEV_EMAIL"],
                    to_addrs=user["email"],
                    msg=f"Subject:Joseph's Flight Club!!!\n\n.Low price alert! Only ${self.price} to fly from "
                        f"{self.cityFrom}-{self.cityFromIATA} to "
                        f"{self.cityTo}-{self.cityToIATA}, from {self.outbound} to {self.inbound}."
                        f" Flight has 1 stopover, via {self.stopoverCity}.")
            else:
                connection.sendmail(
                    from_addr=os.environ["DEV_EMAIL"],
                    to_addrs=user["email"],
                    msg=f"Subject:Joseph's Flight Club!!!\n\n.Low price alert! Only ${self.price} to fly from "
                        f"{self.cityFrom}-{self.cityFromIATA} to "
                        f"{self.cityTo}-{self.cityToIATA}, from {self.outbound} to {self.inbound}.")