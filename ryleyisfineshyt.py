import requests
def getCard(Card):
    response = requests.get(f"https://api.clashroyale.com/v1/{Card.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
#     return {
#         "name": data["name"],
#         "height": data["height"],
#         "weight": data["weight"],
#         "types": [t["type"]["name"] for t in data["types"]]
#     }

# pokemon = getPoke("Bulbasaur")
# print(pokemon)``
