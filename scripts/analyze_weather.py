import pandas as pd
import matplotlib.pyplot as plt
import os

# Charger le CSV le plus récent
data_dir = "../data"
files = [f for f in os.listdir(data_dir) if f.startswith("weather_data")]
if not files:
    raise FileNotFoundError("Aucun fichier weather_data trouvé dans /data")

latest_file = sorted(files)[-1]
df = pd.read_csv(os.path.join(data_dir, latest_file), parse_dates=["time"])

filtre_date = pd.to_datetime("2025-08-15")  # Le 2025-08-15 00:00:00
df = df[df["time"] <= filtre_date]  # Filtre avant la date

# Analyse
avg_temp = df["temperature"].mean()
min_temp = df["temperature"].min()
max_temp = df["temperature"].max()

print(f"Analyse du fichier {latest_file}")
print(f"Température moyenne : {avg_temp:.1f}°C")
print(f"Température minimale : {min_temp}°C")
print(f"Température maximale : {max_temp}°C")

# Graphique
plt.figure(figsize=(10, 5)),
plt.plot(df["time"], df["temperature"], marker="o")
plt.xlabel("Heure")
plt.ylabel("Température °C")
plt.title("Évolution de la température sur la journée")
plt.tight_layout()

output_plot = "../diagrams/temperature_plot.png"
os.makedirs("../diagrams", exist_ok=True)  # Création du dossier
plt.savefig(output_plot)  # Sauvegarde du diagramme
print(f"Diagramme sauvegardées dans {output_plot}")
