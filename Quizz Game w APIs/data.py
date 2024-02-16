import requests
PARAMETERS = {
    "amount":10,
    "type":"boolean"
}
api_ask = requests.get(url="https://opentdb.com/api.php",params=PARAMETERS)
api_ask.raise_for_status()
question_data = api_ask.json()["results"]