import http.client
import urllib.parse

RAPIDAPI_HOST = "mangapi3.p.rapidapi.com"
RAPIDAPI_KEY = "5d9b487097msh41cca179c3ca6c6p12cabcjsn08033da29783"

def translate_text(text: str, to: str):
    conn = http.client.HTTPSConnection(RAPIDAPI_HOST)

    # Form verisi olarak text ve to parametreleri gönderilecek
    payload = urllib.parse.urlencode({
        "text": text,
        "to": to.upper()
    })

    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': RAPIDAPI_HOST,
        'Content-Type': "application/x-www-form-urlencoded"
    }

    conn.request("POST", "/api/translate", payload, headers)

    res = conn.getresponse()
    data = res.read()
    result = data.decode("utf-8")

    # JSON formatında string dönüyor, istersen JSON’a çevir
    import json
    try:
        return json.loads(result)
    except Exception:
        return {"error": "Geçersiz JSON cevap", "raw": result}
