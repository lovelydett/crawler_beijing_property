'''
This is a property price crawler which is to crawl property price
tt
2022.5.15
'''

import time
import requests
import re

def getPage(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Referer': 'https://wuhan.anjuke.com/community/?from=navigation',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    response = requests.get(url, headers=headers, timeout=30)
    return response.text

def getPrice(html):
    pattern = re.compile(r'<p class="property-price-average" data-v-d4f07c36>([\s\S]+?)</p>')
    prices = re.findall(pattern, html)
    return prices

def getLocation(html):
    pattern = re.compile(r'<p class="property-content-info-comm-name" data-v-d4f07c36>([\s\S]+?)</p>')
    locations = re.findall(pattern, html)
    return locations

def do_crawling():
    numPage = 50
    with open("price.txt", "w") as outFile:
        for i in range(1, numPage + 1):
            url = "https://beijing.anjuke.com/community/p" + str(i)
            html = getPage(url)
            locations = getLocation(html)
            prices = getPrice(html)
            assert len(prices) == len(locations)
            assert len(prices) != 0
            for idx in range(len(prices)):
                outFile.write(f"{locations[idx]} {prices[idx].replace('元/㎡', '')}\n")
            time.sleep(1)

if __name__ == "__main__":
    do_crawling()





