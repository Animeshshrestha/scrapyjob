import scrapy


class MeroJobSpider(scrapy.Spider):
    name = 'merojob'

    start_urls = ['https://merojob.com/search/?q=django']

    def parse(self, response):
        # follow links to job pages
        for href in response.css('h1.h4 a::attr(href)'):
            yield response.follow(href, self.parse_job_link)

        # follow pagination links
        for href in response.css('a.pagination-next::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_job_link(self, response):
        print(response)

        yield {
            'Link':response,
            'Job Company Name': response.css('a.text-white span.ml-3::text').get(),
            'Experience':response.css('table.table')[1].css('tr')[1].css('td')[2].css('span::text').get(),
            'Requirements':response.css('div.card-text')[0].css('li::text').get()
        }
