from cgitb import text

import scrapy


class midshptspider(scrapy.Spider):
    name = 'midsh'
    start_urls = [
        'https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1',
        'https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=2'
    ]

    def parse(self, response):

        doller = response.css('div.price-rating-container div.catalog-item-price span.price ::text').extract()
        title = response.css(".catalog-item-name::text").extract()
        brand = response.css(".catalog-item-brand::text").extract()
        stock = response.css(".out-of-stock::text").extract()


        for i in range(len(title)):

            if stock[i] == "Out of Stock":
                det = {
                    'price': doller[i],
                    'title': title[i],
                    'stock': False,
                    'maftr': brand[i],
                }
            else:
                det = {
                    'price': doller[i],
                    'title': title[i],
                    'stock': True,
                    'maftr': brand[i],
                }
            yield det
        