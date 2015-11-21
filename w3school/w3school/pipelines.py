# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import json
# import codecs
from openpyxl import Workbook

class W3SchoolPipeline(object):
    # pass
    def __init__(self):
        self.wb=Workbook()
        self.ws=self.wb.active
        # self.ws.append(['title','link','desc'])                 #设置表头

    def process_item(self, item, spider):
        # print item
        # print item['title'][0]
        line=[item['title'][0],item['link'][0],item['desc'][0]]
        print line
        self.ws.append(line)

        self.wb.save(r'D:\pb\py\spider\scrapy\w3school\result.xlsx')
        return item
