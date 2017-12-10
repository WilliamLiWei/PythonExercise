#by 寒小阳(hanxiaoyang.ml@gmail.com)
import sys
import scrapy
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qqnews.items import QqnewsItem


class QQNewsSpider(scrapy.Spider):
    # 爬虫名称
    name = "tutorial"
    # 设置下载延时
    download_delay = 1
    # 允许域名
    allowed_domains = ["news.cnblogs.com"]
    # 开始URL
    start_urls = [
        "https://news.cnblogs.com"
    ]
    # 爬取规则,不带callback表示向该类url递归爬取
    rules = (
        Rule(SgmlLinkExtractor(allow=(r'https://news.cnblogs.com/n/page/\d',))),
        Rule(SgmlLinkExtractor(allow=(r'https://news.cnblogs.com/n/\d+',)), callback='parse_content'),
    )

    # 解析内容函数
    def parse_content(self, response):
        item = QqnewsItem()
        print('qq')
        # 当前URL
        title = response.selector.xpath('//*[@id="news_title"]/a')[0].extract().decode('utf-8')
        item['title'] = title
        print(title)

        author = response.selector.xpath('//div[@id="news_info"]/span/a/text()')[0].extract().decode('utf-8')
        item['author'] = author

        releasedate = response.selector.xpath('//div[@id="news_info"]/span[@class="time"]/text()')[0].extract().decode(
            'utf-8')
        item['release_date'] = releasedate

        yield item