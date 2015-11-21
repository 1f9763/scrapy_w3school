__author__ = '2200621'
coding='utf-8'

from scrapy.spiders import Spider
from scrapy.selector import Selector
# from scrapy import log

from w3school.items import W3SchoolItem

class W3schoolSpider(Spider):
    name='w3school'
    allowed_domains=['w3school.com.cn']
    start_urls=[
        'http://www.w3school.com.cn/xml/xml_syntax.asp'
    ]

    def parse(self, response):
        sel=Selector(response)
        sites=sel.xpath('//div[@id="navsecond"]/div[@id="course"]/ul[1]/li')
        items=[]

        for site in sites:
            item=W3SchoolItem()

            # title=site.xpath('a/text()').extract()
            # link=site.xpath('a/@href').extract()
            # desc=site.xpath('a/@title').extract()

            item['title']=site.xpath('a/text()').extract()
            item['link']=site.xpath('a/@href').extract()
            item['desc']=site.xpath('a/@title').extract()

            # print item['title']
            # item['title']=[t.encode('utf-8') for t in title]
            # # print item['title']
            # item['link']=[l.encode('utf-8') for l in link]
            # item['desc']=[d.encode('utf-8') for d in desc]

            items.append(item)
            # log.msg('Appending item...',level='INFO')

        # log.msg('Appending done',level='INFO')
        # print items
        return items