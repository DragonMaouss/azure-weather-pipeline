from azure.storage.blob import BlobServiceClient
import os

# Connexion Azurite locale (clé par défaut)
connect_str = (
    "DefaultEndpointsProtocol=http;"
    "AccountName=devstoreaccount1;"
    "AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;"
    "BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"
)

container_name = "weather-data"

# Client
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Créer le container
container_client = blob_service_client.get_container_client(container_name)
try:
    container_client.create_container()
    print(f"Container '{container_name}' créé")
except Exception:
    print(f"Container '{container_name}' déjà existant")

# Charger le CSV le plus récent
data_dir = "../data"
files = [f for f in os.listdir(data_dir) if f.startswith("weather_data")]
if not files:
    raise FileNotFoundError("Aucun fichier weather_data trouvé dans /data")

latest_file = sorted(files)[-1]
file_path = os.path.join(data_dir, latest_file)

# Upload
blob_client = blob_service_client.get_blob_client(
    container=container_name, blob=latest_file
)
with open(file_path, "rb") as data:
    blob_client.upload_blob(data)

print(f"Fichier {latest_file} uploadé dans le container '{container_name}'")
