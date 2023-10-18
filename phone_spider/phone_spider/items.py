import scrapy


class PhoneDataItem(scrapy.Item):
    title = scrapy.Field()
    brand = scrapy.Field()
    description = scrapy.Field()
    operating_system = scrapy.Field()
    display_technology = scrapy.Field()
    image_url = scrapy.Field()
