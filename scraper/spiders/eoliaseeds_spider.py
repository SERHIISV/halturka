# -*- coding: utf-8 -*-
import scrapy

from scraper.items import Product


class EoliaseedsSpider(scrapy.Spider):
    name = "eoliaseeds"

    start_urls = [
        'http://eoliaseeds.com.ua/price-list/'
    ]

    def parse(self, response):
        content = response.xpath('//table[@class="cart fix"]/tr[not(contains (@class, "first"))]')
        for tr in content[1:]:
            if tr.xpath('td[@class="value discount"]'):
                item = Product()
                url = tr.xpath('td[@class="title"]/p/a/@href').extract()[0].strip()
                item['URL'] = response.urljoin(url)
                item['Name'] = tr.xpath('td[@class="title"]/p/a/text()').extract()[0].strip()
                price = tr.xpath('td[@class="price"]/p[2]/text()').extract()[0].strip()
                item['Price'] = ''.join(el for el in price if el.isdigit())
                item['Brand'] = url.split('/')[2].replace('-', ' ')
                yield item
        try:
            next_page = response.xpath('//div[@id="pages"]/a[contains(span/text(),">")]/@href').extract()[0]
            yield scrapy.Request(response.urljoin(next_page),
                                 self.parse)
        except:
            pass
