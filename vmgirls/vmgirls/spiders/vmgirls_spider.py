# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class VmgirlsSpiderSpider(CrawlSpider):
    name = 'vmgirls_spider'
    allowed_domains = ['vmgirls.com']
    start_urls = ['https://vmgirls.com/']

    rules = (
        # Rule(LinkExtractor(allow=r'https://www.vmgirls.com/'), follow=True),
        # Rule(LinkExtractor(allow=r'https://www.vmgirls.com/+d.html'), callback='parse_item', follow=False),
    )

    def parse(self, response):
        print('=' * 30)
        print(response)
        print('=' * 30)

    def parse_item(self, response):
        print('=' * 30)
        print(response)
        print('=' * 30)
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item

    if __name__ == '__main__':
        from scrapy import cmdline

        cmdline.execute('scrapy crawl vmgirls_spider'.split())
