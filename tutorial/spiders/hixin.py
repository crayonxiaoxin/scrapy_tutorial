import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HixinSpider(CrawlSpider):
    name = 'hixin'
    allowed_domains = ['hixin.cc']
    start_urls = ['https://hixin.cc/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[contains(@class,"a-thumb")]'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath('//h1[contains(@class,"title")]/text()').get()
        item['content'] = response.xpath('//div[contains(@class,"content")]').get()
        # print(item['title'])
        # print(item['content'])
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item
