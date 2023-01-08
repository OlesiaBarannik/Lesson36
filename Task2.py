import requests
import json

response = requests.get("https://api.pushshift.io/reddit/comment/search/?subreddit=askhistorians")

response.json()

with open("response.json", "w") as response_file:
    json.dump(response.json(), response_file, indent=4)