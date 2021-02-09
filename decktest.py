import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6"

payload={}
headers = {
          'Cookie': '__cfduid=d61c5d08ddde5c335c11082a3b89991451608437535'
          }

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

deck = response.json()
deck_id = deck['deck_id']
print(deck_id)
