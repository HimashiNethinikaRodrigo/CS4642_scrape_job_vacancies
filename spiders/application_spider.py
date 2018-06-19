import scrapy


class ApplicationSpider(scrapy.Spider):
    name = "applications"

    def start_requests(self):

        start_urls = [
            'https://www.applications.lk/job-vacancies',
        ]
        for i in range(2, 201):
            print(i)
            start_urls.append('https://www.applications.lk/job-vacancies/page/'+str(i))

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        print('RESPONSE --------------------------------------- : ', response.url)

        if 'https://www.applications.lk/job-vacancies' == response.url or 'https://www.applications.lk/job-vacancies/page/' in response.url:
            jobs = response.xpath('//article/div[@class="entry-content-wrapper"]/header[@class="entry-header"]/'
                                  'h2[@class="entry-title"]/a/@href').extract()
            for job in jobs:
                yield scrapy.Request(job, callback=self.parse)

        else:
            title = response.xpath('//article/header[@class="entry-header"]/h1[@class="entry-title"]'
                                   '/text()').extract_first()

            posted_date = response.xpath('//article/header[@class="entry-header"]/div[@class="entry-meta"]'
                                         '/span[@class="posted-on"]/a/time[@class="entry-date published updated"]/'
                                         'text()').extract_first()
            if posted_date == 'None':
                posted_date = response.xpath('//article/header[@class="entry-header"]/div[@class="entry-meta"]'
                                             '/span[@class="posted-on"]/a/time[@class="entry-date published"]/'
                                             'text()').extract_first()

            posted_time = response.xpath('//article/header[@class="entry-header"]/div[@class="entry-meta"]'
                                         '/span[@class="posted-on"]/a/time/@datetime').extract_first()
            author = response.xpath('//article/header[@class="entry-header"]/div[@class="entry-meta"]'
                                    '/span[@class="byline"]/span[@class="author vcard"]'
                                    '/a[@class="url fn n"]/text()').extract_first()
            closing_date = response.xpath('//article/div[@class="entry-content-wrapper"]/div[@class="entry-content"]'
                                          '/p/strong/span/text()').extract_first()

            yield {
                'title': title,
                'posted_date': posted_date,
                'posted_time': posted_time,
                'author': author,
                'closing_date': closing_date
            }