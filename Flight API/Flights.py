import requests
import json
from datetime import datetime

def printflight(departure, arrival, duration, i):
    print("Departure --> " + departure)
    print("Arrival --> " + arrival)
    print("From --> " + response['data'][i]['flyFrom'])
    print("To --> " + response['data'][i]['flyTo'])
    print("Duration --> " + str(duration))
    print("Price --> " + str(response['data'][i]['price']))
    print("\n")

url = "https://tequila-api.kiwi.com/v2/search?"

querystring = {"fly_from":"prague_cz",
               "fly_to":"milan_it",
               "date_from":"25/05/2022",
               "date_to":"25/05/2022"
}

header = {
	"apikey": "GAFEy8Ht18oCCfyxrW6xifhsTAyGH8kI"
}

response = requests.get(url, params=querystring, headers=header)
response = json.loads(response.text)

for i in range(len(response['data'])):
    departure = response['data'][i]['local_departure']
    dep = datetime.strptime(departure, "%Y-%m-%dT%H:%M:%S.%fZ")
    departure = datetime.strptime(departure, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d/%m/%Y %H:%M:%S")
      
    arrival = response['data'][i]['local_arrival']
    arr = datetime.strptime(arrival, "%Y-%m-%dT%H:%M:%S.%fZ")
    arrival = datetime.strptime(arrival, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d/%m/%Y %H:%M:%S")
    
    duration = arr - dep
    

print(response)