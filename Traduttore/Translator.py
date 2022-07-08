import urllib.request
import json

while True:
    testo = input("Inserire testo --> ")
    testo = testo.replace(" ", "%20")
    lang = input("Inserire codice lingua --> ")
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20200310T173250Z.00056dd291c36c21.acbf636f30779ee673020cc1b254eded4011ffb5&text="
    risposta = urllib.request.urlopen(url + testo + "&lang=" + lang)
    dati = risposta.read()
    valori = json.loads(dati)

    traduzione = valori ['text']
    print ("Traduzione --> ", traduzione)

    lingua = valori ['lang']
    print("Lingua --> ", lingua)

    break

