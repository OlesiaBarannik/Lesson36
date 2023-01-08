import requests

response = requests.get("https://twitter.com/robots.txt")
open("robots.txt", "wb").write(response.content)

