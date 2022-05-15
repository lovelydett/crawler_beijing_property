'''
This is a property price crawler which is to crawl property price
tt
2022.5.15
'''

import time
import requests
import re
import random
from urllib.parse import quote

USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 4.2.1; M040 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.59 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    ]

def getPage(url):
    user_agent = USER_AGENTS[random.randint(0, 100) % len(USER_AGENTS)] # Anti-anti-crawler
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Referer': 'https://beijing.anjuke.com/community/?from=navigation',
        'User-Agent': user_agent,
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

def getDate(html):
    q = quote("年建造")
    pattern = re.compile(r'<p class="property-content-info-text" data-v-d4f07c36>([\s\S]+?)' + q + '</p>')
    dates = re.findall(pattern, html)
    return dates

def crawl_sale():
    numPage = 50
    with open("price.txt", "w") as outFile:
        for i in range(1, numPage + 1):
            url = "https://beijing.anjuke.com/sale/p" + str(i)
            html = getPage(url)
            locations = getLocation(html)
            prices = getPrice(html)
            dates = getDate(html)
            assert len(prices) == len(locations)
            assert len(prices) == len(dates)
            if len(prices) == 0:
                print(i)
            for idx in range(len(prices)):
                outFile.write(f"{locations[idx]} {dates[idx].strip().replace('年建造', '')} {prices[idx].strip().replace('元/㎡', '')}\n")
            time.sleep(1)

if __name__ == "__main__":
    # crawl_sale()
    html = getPage("https://beijing.anjuke.com/sale/p1")
    locations = getLocation(html)
    prices = getPrice(html)
    dates = getDate(html)
    print(locations)
    print(prices)
    print(dates)