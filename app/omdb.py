import requests

KEY = open('keys/key_omdb.txt', 'r').read().strip()

def get_info(title):
    url = f"http://www.omdbapi.com/?apikey={KEY}&t={title}"
    return requests.get(url).json()