import requests
import pandas as pd
from datetime import datetime
import os

url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 48.85, "longitude": 2.35, "hourly": "temperature_2m"}  # Paris
os.makedirs("../data", exist_ok=True)  # Création du dossier

r = requests.get(url, params)
data = r.json()

# Conversion en df
df = pd.DataFrame(
    {"time": data["hourly"]["time"], "temperature": data["hourly"]["temperature_2m"]}
)
df["time"] = pd.to_datetime(df["time"])  # Convertir en datetime

# Sauvegarde csv
today = datetime.now().strftime("%d-%m-%Y")
output_file = f"../data/weather_data_{today}.csv"
df.to_csv(output_file, index=False)
print(f"Données sauvegardées dans {output_file}")
