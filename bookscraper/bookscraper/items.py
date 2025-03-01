# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# def stars(value):
#     if value == 'one':
#         return 1
#     elif value == 'two':
#         return 2
#     elif value == 'three':
#         return 3
#     elif value == 'four':
#         return 4
#     elif value == 'five':
#         return 5


class BookItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    available = scrapy.Field()
    stars_count = scrapy.Field()
    category = scrapy.Field()
    product_type = scrapy.Field()
    price_without_tax = scrapy.Field()
    price_with_tax = scrapy.Field()
    tax = scrapy.Field()
    number_of_reviews = scrapy.Field()
