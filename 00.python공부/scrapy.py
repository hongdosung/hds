# Scrapy는 강력한 웹 스크래핑 및 크롤링 프레임워크로, 복잡한 웹 사이트에서 대량의 데이터를 추출하는 데 유용

# pip install scrapy

# [Scrapy 프로젝트 생성]
# scrapy startproject scrapy_project
# cd scrapy_project

# scrapy_project/spiders 디렉토리에 example_spider.py 파일을 생성하고, 스파이더를 정의합니다.

import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['http://example.com']

    def parse(self, response):
        # 제목 추출
        title = response.css('title::text').get()
        print(f"Title: {title}")

        # 모든 링크 추출
        links = response.css('a::attr(href)').getall()
        for link in links:
            print(link)

# 스파이더를 실행하여 데이터를 추출합니다.
# scrapy crawl example
# 위 명령어는 example 스파이더를 실행하고, 정의된 URL에서 데이터를 추출합니다.

#####################################################################################
# [Scrapy 항목 및 파이프라인]
# Scrapy를 사용하여 더 복잡한 데이터를 추출하고, 
# 항목(Item)과 파이프라인(Pipeline)을 정의하여 데이터를 처리할 수 있습니다.

# items.py 파일 생성
import scrapy

class ExampleItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()

# example_spider.py 파일 수정
import scrapy
from scrapy_project.items import ExampleItem

class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['http://example.com']

    def parse(self, response):
        item = ExampleItem()
        item['title'] = response.css('title::text').get()
        item['link'] = response.url
        yield item

        links = response.css('a::attr(href)').getall()
        for link in links:
            yield response.follow(link, self.parse)
            
# pipelines.py 파일 생성
class ExamplePipeline:
    def process_item(self, item, spider):
        print(f"Title: {item['title']}, Link: {item['link']}")
        return item

# settings.py 파일 수정
# ITEM_PIPELINES 설정 추가
ITEM_PIPELINES = {
    'scrapy_project.pipelines.ExamplePipeline': 300,
}


#####################################################################################
# Scrapy를 사용한 상품 정보 스크래핑

import scrapy
from scrapy_project.items import ProductItem

class ProductSpider(scrapy.Spider):
    name = 'product'
    start_urls = ['http://ecommerce.example.com']

    def parse(self, response):
        products = response.css('.product')
        for product in products:
            item = ProductItem()
            item['name'] = product.css('.product-name::text').get()
            item['price'] = product.css('.product-price::text').get()
            yield item

# items.py 파일 정의
import scrapy

class ProductItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()

# pipelines.py 파일 수정
class ProductPipeline:
    def process_item(self, item, spider):
        print(f"Product: {item['name']} - Price: {item['price']}")
        return item

# settings.py 파일 수정
ITEM_PIPELINES = {
    'myproject.pipelines.ProductPipeline': 300,
}
