# -*- coding: utf-8 -*-
import scrapy
from fashion_quotes_spider.items import QuoteItems


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['www.goodreads.com']
    start_urls = ['http://www.goodreads.com/quotes/tag/fashion/']

    def parse(self, response):

        quotes = response.xpath('//*[@class="quote mediumText "]')

        for quote in quotes:

            my_image_urls = []

            quote_item = QuoteItems()

            quote_item['text'] = quote.css('.quoteText::text').extract()
            quote_item['author'] = quote.xpath('.//*[@class="quoteText"]/a/text()').extract_first()
            quote_item['tags'] = quote.xpath('.//div[@class="greyText smallText left"]/a/text()').extract()
            quote_item['likes'] = quote.xpath('.//div[@class="quoteFooter"]/div[@class="right"]/a/text()').extract_first()

            img_url = quote.xpath('.//*[@class="leftAlignedImage"]/img/@src').extract_first()
            my_image_urls.append(img_url)
            quote_item['image_urls'] = my_image_urls
            quote_item['images'] = []

            yield quote_item

        # NEXT PAGE

        '''
        next_page_url = response.xpath('//*[@class="next_page"]/@href').extract_first()
        if next_page_url:
            absolute_next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(absolute_next_page_url)
        '''