import requests

response = requests.get("https://pythonfetch.000webhostapp.com/pilot_to_server/server_to_drone.json")
print(response.json())