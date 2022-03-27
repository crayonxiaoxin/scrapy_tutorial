import scrapy


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/rank/yuepiao']

    def parse(self, response):
        print(response.text)
        for item in response.xpath('//div[@class="book-img-text"]/ul/li'):
            name = item.xpath('./div[@class="book-mid-info"]/h2/a/text()').get()
            print(name)
        pass
