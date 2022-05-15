'''
Query Baidu API for positions
tt
2022.5.15
'''
import time

from utils import loadConf

from urllib.request import urlopen
from urllib.parse import quote
import json

# Remember not to upload your own ak to Github!
confs = loadConf("crawler.conf")
ak = confs["ak"]

def queryPosition(address, max_try=5):
    try_count = 0
    lat, lng = None, None
    url = 'http://api.map.baidu.com/geocoding/v3/'
    output = 'json'
    add = quote(str(address))  # Quote cuz you dont directly type Chinese in url
    uri = url + '?' + 'address=' + add + '&output=' + output + '&ak=' + ak

    while try_count < max_try:
        try:
            req = urlopen(uri, timeout=30)
            res = req.read().decode()
            res = json.loads(res)
            lat = res['result']['location']['lat']
            lng = res['result']['location']['lng']
            break
        except:
            try_count += 1
            print(f"Request failed for {address}, retry after 10 seconds")
            time.sleep(10)
    return lat, lng

def queryPositionBatch(batch):
    res = []
    for address in batch:
        lat, lng = queryPosition(address)
        res.append((lat, lng))
        time.sleep(1)

if __name__ == "__main__":
    address = "天安门"
    lat, lng = queryPosition(address)
    print(f"Query for {address}: latitude = {lat}, longitude = {lng}")
