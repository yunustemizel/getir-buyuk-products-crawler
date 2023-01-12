import scrapy
import json
import time

class GetirSpider(scrapy.Spider):
    name = 'getir'
    allowed_domains = ['getir.com']
    products=[]
    start_urls = [
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=yeni-urunler-OcXAkcBF1S',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=su-icecek-ewknEvzsJc',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=meyve-sebze-VN2A9ap5Fm',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=firindan-q357eEdgBs',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=temel-gida-IQH9bir3bX',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=atistirmalik-BaaxwkyV1y',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=dondurma-Aw6YFhRWBI',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=sut-urunleri-JGtfnNALTJ',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=kahvalti-iat0l1yrkf',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=yiyecek-0VLJmBhnI3',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=fit-form-A9ciT987qU',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=kisisel-bakim-A21PNmddpt',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=ev-bakim-JXy6KcrPKW',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=ev-yasam-jdRnndEpyl',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=teknoloji-X6SRgY6F78',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=evcil-hayvan-T27vt8aM7c',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=bebek-T71m4N3D3K',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=giyim-PGANXG2SYb',
            'https://market-client-api-gateway.getirapi.com/category/products?countryCode=TR&categorySlug=cinsel-saglik-viPc8mv9zd',
            
        ]
        
    def parse(self, response):
        jsonresponse = json.loads(response.body)
        
        for subCategory in jsonresponse["data"]['category']['subCategories']:
           
            for product in subCategory['products']:
                self.products.append({
                    "title": product["name"],
                    "price": product["price"],
                    "id":product['id'],
                    "images":product['picURLs'],
                    "url":"https://getir.com/buyuk/urun/" + product['slug']
                })
        
        jsonString = json.dumps(self.products, ensure_ascii=False)
        jsonFile = open("data.json", "w", encoding='utf8')
        jsonFile.write(jsonString)
        jsonFile.close()


