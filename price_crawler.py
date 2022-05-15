'''
This is a property price crawler which is to crawl property price
tt
2022.5.15
'''

import time
import requests
import re
import random

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
        'Referer': 'https://beijing.anjuke.com/sale/?from=navigation',
        'User-Agent': user_agent,
    }
    response = requests.get(url, headers=headers, timeout=30)
    return response.text

def getPrice(html):
    pattern = re.compile(r'<span class="price">([\s\S]+?)<span class="unit">元/平')
    prices = re.findall(pattern, html)
    return prices

def getLocation(html):
    pattern = re.compile(r'<strong class="g-overflow">([\s\S]+?)</strong>')
    locations = re.findall(pattern, html)
    return locations

def getDate(html):
    pattern = re.compile(r'<label class="date">([\s\S]+?)</label>')
    dates = re.findall(pattern, html)
    return dates

def do_crawling():
    numPage = 50
    with open("price.txt", "w") as outFile:
        for i in range(1, numPage + 1):
            url = "https://beijing.anjuke.com/community/p" + str(i)
            html = getPage(url)
            locations = getLocation(html)
            prices = getPrice(html)
            dates = getDate(html)
            assert len(prices) == len(locations)
            if len(prices) == 0:
                print(html)
            for idx in range(len(prices)):
                outFile.write(f"{locations[idx]} {dates[idx].replace('年建造', '')} {prices[idx].replace('元/㎡', '')}\n")
            time.sleep(1)

if __name__ == "__main__":
    do_crawling()