import json
import requests

url = "https://api.windy.com/api/point-forecast/v2"
api_key = "nXrBaP3RqsRZGHm62CDvHSh4BoyxW9cq"

headers = {
    "Content-Type": "application/json",
    "Authorization": api_key
}

payload = {
    "lat": 41.0082,        # Örnek: İstanbul
    "lon": 28.9784,
    "model": "gfs",        # Örnek model
    "parameters": ["temp", "wind", "pressure"],
    "levels": ["surface"],
    "key": api_key
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    data = response.json()
    with open("forecast.json", "w") as outfile:
        json.dump(data, outfile, indent=4)
    print("Veri başarıyla kaydedildi.")
else:
    print(f"Hata: {response.status_code} - {response.text}")
