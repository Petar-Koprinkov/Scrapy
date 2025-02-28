import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        books = response.css('article.product_pod')

        for book in books:
            book_url = book.css('h3 a ::attr(href)').get()

            book_page = 'https://books.toscrape.com/' + book_url

            yield response.follow(book_page, callback=self.parse_book)

        next_page = response.css('li.next a::attr(href)').get()

        if next_page:
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page

            yield response.follow(next_page_url, callback=self.parse)

    def parse_book(self, response):
        book_details = response.css('.product_main')
        boarder = response.css('.breadcrumb')
        table_rows = response.css('table tr')

        yield {
            'title': book_details.css("h1::text").get(),
            'price': book_details.css(".price_color::text").get(),
            'available': book_details.xpath("normalize-space(//p[@class='instock availability'])").get(),
            'stars_count': book_details.css(".star-rating::attr(class)").get().split()[1].lower(),
            'category': boarder.xpath("//li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
            'product_type': table_rows[1].css("td::text").get(),
            'price_without_tax': table_rows[2].css("td::text").get(),
            'price_with_tax': table_rows[3].css("td::text").get(),
            'tax': table_rows[4].css("td::text").get(),
            'number_of_reviews': table_rows[6].css("td::text").get(),
        }
