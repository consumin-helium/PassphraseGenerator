import requests
import json

url = "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"

response = requests.get(url)
words = response.content.decode().splitlines()

# Remove numbers from the beginning of each word
words = [word.split("\t")[1] for word in words]

# Save words to a JSON file
with open("words.json", "w") as f:
    json.dump(words, f)
