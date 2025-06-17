[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/meren41-s-navmobil-badge.png)](https://mseep.ai/app/meren41-s-navmobil)

# Manga Translator MCP

Bu MCP, MangAPI3 Translate API kullanarak manga metinlerini bir dilden başka dile çevirir.

## Kullanım

- POST /translate endpoint'ine JSON body ile `text` ve `to` parametreleri gönderilir.
- MCP, RapidAPI üzerinden çeviri yapar ve sonucu JSON olarak döner.

## Gereksinimler

- Python 3.9+
- Flask
- Requests
