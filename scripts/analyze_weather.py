import pandas as pd

# Charger le csv
file = "../data/weather_data_14-08-2025.csv"
df = pd.read_csv(file, sep=",")

# Analyse
avg_temp = df["temperature"].mean()
min_temp = df["temperature"].min()
max_temp = df["temperature"].max()

print(f"Analyse du fichier {file}")
print(f"Température moyenne : {avg_temp:.1f}°C")
print(f"Température minimale : {min_temp}°C")
print(f"Température maximale : {max_temp}°C")
