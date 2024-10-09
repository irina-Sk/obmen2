import requests
import json
import pprint

resault = requests.get('https://open.er-api.com/v6/latest/USD')
data = json.loads(resault.text)
p = pprint.PrettyPrinter(indent=4)

p.pprint(data)
