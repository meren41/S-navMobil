import http.client
import urllib.parse
import json

RAPIDAPI_HOST = "mangapi3.p.rapidapi.com"
RAPIDAPI_KEY = "5d9b487097msh41cca179c3ca6c6p12abcjsn08033da29783"

def translate_text(text: str, to: str) -> str:
    """
    MangAPI3 Translate API kullanarak text'i hedef dile çevirir.
    """
    conn = http.client.HTTPSConnection(RAPIDAPI_HOST)

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

    try:
        # JSON cevabı dict olarak döndür
        return json.loads(result)
    except json.JSONDecodeError:
        return {"error": "Geçersiz JSON cevap", "raw": result}
