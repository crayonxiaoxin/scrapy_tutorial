import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BaiduHotSpider(CrawlSpider):
    name = 'baidu_hot'
    allowed_domains = ['baidu.com','top.baidu.com','haokan.baidu.com']
    start_urls = ['https://top.baidu.com/board?tab=realtime']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[contains(@class,"content_1YWBm")]/a'),
             follow=False),
        # Rule(LinkExtractor(restrict_xpaths='//div[contains(@class,"carousel-container_161Jl")]/div/a'),
        #      callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        # print(response.text)
        item['title'] = response.xpath('string(//p[@class="title_2e25d"])').get()
        # item['title'] = response.xpath('//h1[@class="videoinfo-title"]/text()').get()
        print(item['title'])
        return item
