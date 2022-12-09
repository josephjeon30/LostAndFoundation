import requests

def get_duck():
  link = 'https://random-d.uk/api/v2/random?Type=jpg'
  return requests.get(link).json().get('url')
