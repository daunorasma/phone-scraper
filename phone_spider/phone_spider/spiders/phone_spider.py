import scrapy
from ..items import PhoneDataItem

class PhoneSpider(scrapy.Spider):
    name = 'phone_spider'
    start_urls = ["https://www.productindetail.com/phones"]

    def parse(self, response, *args, **kwargs):
        # Start with picking up the main component to later map through
        phone_links = response.css('div.card-body > a:first-of-type::attr(href)').extract()

        for phone_link in phone_links:
            # Follow each phone link and call parse_phone_details function
            yield response.follow(phone_link, callback=self.parse_phone_details)

        # Check if there's a "Next" page link and follow it
        # Comment out if you do not want a very long process
        next_page = response.css('li.page-item.active + li.page-item a.page-link::attr(href)').extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_phone_details(self, response):
        item = PhoneDataItem()
        item['title'] = response.xpath('//title/text()').get().split(' - ')[0]
        item['brand'] = response.xpath('//title/text()').get().split(' ', 1)[0]
        item['description'] = response.xpath('//th[contains(., "Product Type")]/following-sibling::td/small/text()').get()
        item['operating_system'] = response.xpath('//div[contains(.//small, "Operating System")]/small/text()').get()
        item['display_technology'] = response.xpath('//th[contains(., "Display Technology")]/following-sibling::td/small/text()').get()
        item['image_url'] = response.xpath('//div[@class="col-sm-3 col-lg-3 col-xl-3"]/img/@src').get()
        yield item
