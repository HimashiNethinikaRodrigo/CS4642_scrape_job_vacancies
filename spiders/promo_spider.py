import scrapy


class PromoSpider(scrapy.Spider):
    name = "promo"

    def start_requests(self):
        urls = [

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response)
