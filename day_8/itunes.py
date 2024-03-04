"""
using the requests package to fetch data from APIs'
"""

import sys
import json
import requests

if len(sys.argv) != 2:
    sys.exit()

url = "https://itunes.apple.com/search?entity=song&limit=1&term" + sys.argv[1]
response = requests.get(url)
print(json.dumps(response.json()))
