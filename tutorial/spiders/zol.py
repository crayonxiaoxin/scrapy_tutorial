import scrapy


class ZolSpider(scrapy.Spider):
    name = 'zol'
    allowed_domains = ['zol.com.cn']
    start_urls = ['https://desk.zol.com.cn/bizhi/9895_118950_2.html']

    def parse(self, response):
        image_url = response.xpath('//img[@id="bigImg"]/@src').getall()
        image_name = response.xpath('string(//div[contains(@class,"photo-tit")]/h3)').get()
        image_name = image_name.strip().replace("\n", "").replace("\r", "").replace("\t", "").replace("/", "_")
        yield {
            'image_urls': image_url,    # imagesPipeline 规定了字段名 image_urls
            'image_name': image_name,
        }
        next_url = response.xpath('//a[@id="pageNext"]/@href').get()
        # 如果有下一页，则继续下载下一页
        if next_url.find(".html") != -1:
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)
