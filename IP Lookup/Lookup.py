import urllib.request
import json

while True:
    ip = input("Inserire un indirizzo IP --> ")
    url = "http://ip-api.com/json/"
    risposta = urllib.request.urlopen(url + ip)
    dati = risposta.read()
    valori = json.loads(dati)

    print ("IP --> " + valori['query'])
    print ("Nazione --> " + valori['country'])
    print ("Regione --> " + valori['regionName'])
    print ("Città --> " + valori['city'])
    print ("Provider di Rete --> " + valori['isp'])
    print ("Organizzazione --> " + valori['org'])

    break
    
