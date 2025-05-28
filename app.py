import requests
import json

JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any"

def get_joke() -> str:
    """
    JokeAPI'yi kullanarak rastgele bir şaka alır.
    """
    headers = {
        'Content-Type': 'application/json'
    }

    # API'yi çağır
    response = requests.get(JOKE_API_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data['type'] == 'single':
            return data['joke']  # Tek satırlık şaka
        elif data['type'] == 'twopart':
            return f"{data['setup']} - {data['delivery']}"  # Setup ve delivery kısmı
    else:
        return "Şaka alınırken bir hata oluştu."
