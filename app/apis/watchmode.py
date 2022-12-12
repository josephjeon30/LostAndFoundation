import requests

KEY = open('keys/key_watchmode.txt', 'r').read().strip()

# returns info about streaming services in dict
def get_streaming(imdb_id):
  url = f'https://api.watchmode.com/v1/title/{imdb_id}/sources/?apiKey={KEY}'
  return requests.get(url).json()

def get_trailer(imdb_id):
  url = f'https://api.watchmode.com/v1/title/{imdb_id}/details/?apiKey={KEY}'
  return requests.get(url).json().get('trailer')