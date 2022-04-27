#Airtable function through NoCodeAPI
import requests

def postData(url, data):
    url = url
    params = {}
    data = data
    r = requests.post(url = url, params = params, json = data)
    result = r.json()
    return result