import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {"latitude": 48.85, "longitude": 2.35, "hourly": "temperature_2m"}  # paris

response = requests.get(url, params)

if response.status_code == 200:
    print("Api fonctionnelle")
    print(response.json()["hourly"]["time"][:5])
    print(response.json()["hourly"]["temperature_2m"][:5])
else:
    print("Erreur API", response.status_code)
