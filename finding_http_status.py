import requests


user_data = input("Vvedite status kod: ")
api_of_status_codes = "https://http.cat/"
api_status_code = api_of_status_codes + user_data
with open("deta.png", "wb") as file:
    file.write(requests.get(api_status_code).content)
