import scrapy
from quotes.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):

        for quote in response.xpath('//div[@class="quote"]'):
            item = QuotesItem()
            '''            
            yield {
                'text': quote.xpath('span[@class="text"]/text()').extract_first(),
                'author': quote.xpath('span/small[@class="author"]/text()').extract_first(),
            }
            '''
            item['title'] = quote.xpath('span[@class="text"]/text()').extract_first()
            item['author'] = quote.xpath('span/small[@class="author"]/text()').extract_first()
            yield item

        next_page = response.xpath('//li[@class="next"]/@herf').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)