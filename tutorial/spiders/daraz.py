import scrapy


class DarazSpider(scrapy.Spider):
    name = 'daraz'

    start_urls = ['https://www.daraz.com.np/products/mini-wireless-sport-bluetooth-earbuds-headset-stereo-in-ear-earphone-i100064002-s1020317001.html?spm=a2a0e.11779170.just4u.2.287d2d2bsSCS9t&scm=1007.17519.116426.0&pvid=cd8ee5b2-2741-41e0-b3f2-bd9ab3ee3db6&clickTrackInfo=tcExpIds%3A249%3Btcsceneid%3AHPJFY%3Bbuyernid%3A5468579c-4c32-402a-fd54-a3d462a50d8e%3Btcbid%3A6%3Btcboost%3A0%3Bpvid%3Acd8ee5b2-2741-41e0-b3f2-bd9ab3ee3db6%3B']

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
