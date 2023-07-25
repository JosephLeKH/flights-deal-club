import requests
import os

print("Welcome to Joseph's Flight Club\n\
We find the best flight deals and email them to you.")

fName = input("What is your first name? ")
lName = input("What is your last name? ")

temp = input("What is your email? ")
email = input("Type your email again. ")

if email != temp:
  print("The emails didn't match, please try again.")
else:
  params = {
    "user": {
      "firstName": fName,
      "lastName": lName,
      "email": email
    }
  }
  header = {
    "Authorization": os.environ["BEARER"]
  }
  response = requests.post(url=os.environ["APIKEY"], json=params,
                          headers=header)
  print("You're in the club!")
