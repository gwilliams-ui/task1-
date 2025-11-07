#Use the template below to get started
import requests 

url = "https://api.nationalize.io/?name=nathaniel"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)

else:
    print(f"Error code: {response.status_code}")


name = data['result'][0]["name"]['first']
print(name)