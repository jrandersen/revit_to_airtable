#Airtable function through NoCodeAPI
import requests
import utils


def postData(url, data):
    result = []
    r = requests.post(url = url, params = {}, json = data)
    result.append(r.json())
    return utils.listSmash(result)

def getData(url):
    result = []
    r = requests.get(url = url, params = {})
    result.append(r.json())
    return result

def putData(url, data):
    result = []
    r = requests.put(url = url, params = {}, json = data)
    result.append(r.json())
    return result