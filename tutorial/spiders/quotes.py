import scrapy

from tutorial.items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/page/1/']

    def parse(self, response, **kwargs):
        for item in response.xpath('//div[@class="quote"]'):
            tutorial_item = TutorialItem()
            tutorial_item['text'] = item.xpath('./span[@class="text"]/text()').get()
            tutorial_item['author'] = item.xpath('./span/small[@class="author"]/text()').get()
            tutorial_item['tags'] = item.xpath('./div[@class="tags"]/a/text()').getall()
            yield tutorial_item
        next_link = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').get()
        if next_link is not None:
            yield scrapy.Request('https://quotes.toscrape.com%s' % next_link)

# //div[@class="quote"]/span[@class="text"]
# //div[@class="quote"]/span/small[@class="author"]
# //div[@class="quote"]/div[@class="tags"]/a
