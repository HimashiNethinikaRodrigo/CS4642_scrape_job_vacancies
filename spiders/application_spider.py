import scrapy


class ApplicationSpider(scrapy.Spider):
    name = "applications"

    start_urls = [
        'https://www.applications.lk/job-vacancies/'
    ]
    for i in range(2, 10):
        start_urls.append('https://www.applications.lk/job-vacancies/page/'+str(i))

    def parse(self, response):
        print(response)
