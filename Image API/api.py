import requests, json

url = "https://serpapi.com/search.json?engine=google&q=Coffee&google_domain=google.com&tbm=isch&api_key=18dd95a8eb4ab0b7fcb61390a5ccb1ac963eff7f3b5335d2ee1c3d66119230ca"

response = requests.get(url)
response = json.loads(response.text)

print(response)