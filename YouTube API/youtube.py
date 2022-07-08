#!C:\Users\Teo\AppData\Local\Programs\Python\Python310\python.exe

import cgi,cgitb
from urllib import response
import requests,json

###############################################################################

url = "https://serpapi.com/search.json?engine=youtube&search_query=Coffee&api_key=18dd95a8eb4ab0b7fcb61390a5ccb1ac963eff7f3b5335d2ee1c3d66119230ca"

response = requests.get(url)

print(response.text)

###############################################################################

for i in range(len(response["video_results"])):
    print(response["video_results"][i]["link"])
    print(response["video_results"][i]["thumbnail"]["static"])