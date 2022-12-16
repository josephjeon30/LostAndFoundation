import requests

KEY = open('keys/key_watchmode.txt', 'r').read().strip()
SITES = ['Netflix', 'Amazon', 'Hulu', 'HBO Max', 'Disney+', 'iTunes']
# returns info about streaming services in dict
def get_streaming(imdb_id):
  url = f'https://api.watchmode.com/v1/title/{imdb_id}/sources/?apiKey={KEY}'
  streaming = requests.get(url).json()
  ret = []
  for d in streaming:
    if d['name'] in SITES:
      ret.append( (d['name'], d['web_url']) )
  return ret

def get_trailer(imdb_id):
  url = f'https://api.watchmode.com/v1/title/{imdb_id}/details/?apiKey={KEY}'
  return requests.get(url).json().get('trailer')
