import requests

KEY = open('keys/key_watchmode.txt', 'r').read().strip()
SITES = ['Netflix', 'Amazon', 'Hulu', 'HBO Max', 'Disney+', 'iTunes']
# returns info about streaming services in dict
def get_streaming(imdb_id):
  try:
    url = f'https://api.watchmode.com/v1/title/{imdb_id}/sources/?apiKey={KEY}'
    print(url)
    streaming = requests.get(url, verify = False).json()
    ret = []
    for d in streaming:
      tupl = (d['name'], d['web_url'])
      print(tupl)
      if d['name'] in SITES and tupl not in ret:
        ret.append(tupl)
    return ret
  except:
    return ();

def get_trailer(imdb_id):
  url = f'https://api.watchmode.com/v1/title/{imdb_id}/details/?apiKey={KEY}'
  trailer = requests.get(url, verify = False).json().get('trailer')
  if trailer:
    trailer = trailer[:trailer.find('watch')] + 'embed/' + trailer[trailer.find('=') + 1:]
  return trailer 