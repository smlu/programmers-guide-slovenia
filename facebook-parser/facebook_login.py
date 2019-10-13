import requests

def login_into_facebook(username, password):
    url = "https://www.facebook.com"
    response = requests.get(url)
