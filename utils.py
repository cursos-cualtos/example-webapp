import requests

url = 'https://flask-cloud-test.mybluemix.net/hello'

def get_message():
    response = requests.get(url)
    return response.json()