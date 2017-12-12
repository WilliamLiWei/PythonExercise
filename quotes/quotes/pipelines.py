# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class QuotesPipeline(object):
    def process_item(self, item, spider):
        print('+++++++++++++++++++++++++++++++++++')
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line.decode("unicode_escape"))
        print('+++++++++++++++++++++++++++++++++++')

        return item

    def __init__(self):
        print('file create success')
        self.file = codecs.open('data.json', mode='wb', encoding='utf-8')  # 数据存储到data.json



