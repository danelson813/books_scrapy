import scrapy
from ..items import BooksScrapyItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):
        items = BooksScrapyItem()
        products = response.css('article')
        print(f'there are {len(products)} books in products.')
        for book in products:
            title = book.css('h3 a::attr(title)').extract()
            price = book.css('p.price_color::text')[:2].extract()
            items["title"] = title
            items["price"] = price

            yield items

        # get the url of the next page from the next button
        next_page_link = response.css('li.next a::attr(href)').get()
        if next_page_link is not None:
            yield response.follow(next_page_link, callback=self.parse)
