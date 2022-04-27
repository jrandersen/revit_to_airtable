#Airtable function through NoCodeAPI
import requests

def postData(url, data):
    r = requests.post(url = url, params = {}, json = data)
    result = r.json()
    return result