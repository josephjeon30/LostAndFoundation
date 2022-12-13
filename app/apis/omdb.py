import requests

KEY = open('keys/key_omdb.txt', 'r').read().strip()

def get_info(id):
    url = f"http://www.omdbapi.com/?apikey={KEY}&i={id}"
    return requests.get(url).json()

def search(title):
    url = f"http://www.omdbapi.com/?apikey={KEY}&s={title}&p=1"
    return requests.get(url).json()

#print(get_info('tt0120338'))
