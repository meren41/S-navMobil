# Manga Translator MCP

Bu MCP, MangAPI3 Translate API kullanarak manga metinlerini bir dilden başka dile çevirir.

## Kullanım

- POST /translate endpoint'ine JSON body ile `text` ve `to` parametreleri gönderilir.
- MCP, RapidAPI üzerinden çeviri yapar ve sonucu JSON olarak döner.

## Gereksinimler

- Python 3.9+
- Flask
- Requests
