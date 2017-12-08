import requests
from lxml import etree

from selenium import webdriver
import time

s = requests.Session()
for id in range(0, 100, 20):
    url = 'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=' + str(id)
    r = s.get(url)
    r.encoding = 'utf-8'
    root = etree.HTML(r.content)
    
    items = root.xpath('//*[@id="content"]/div/div[1]/div/div[4]/div/a[@class="item"]')
    
    for item in items:
        title = item.xpath('./div[@class="info"]//a/span[@class="title"]/text()')
        name = title[0].encode('gb2312', 'ignore').decode('gb2312')
        # rank = item.xpath('./div[@class="pic"]/em/text()')[0]
        rating = item.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]
        print(name, rating)
