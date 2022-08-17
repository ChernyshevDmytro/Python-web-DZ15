import scrapy
from bs4 import BeautifulSoup

class NewsSpider(scrapy.Spider):
    name = 'news'
    a='www.ua.korrespondent.net'
    b= 'https://ua.korrespondent.net/'
    allowed_domains = ['www.pravda.com.ua']
    start_urls = ['http://www.pravda.com.ua/']


    def parse(self, response):
        for quote in response.xpath("/html//div[@class='container_sub_news_wrapper']"):            
            print(quote.xpath("span").get())
            print(quote.xpath("a/@href").get())
            
            yield {
                'title': quote.xpath("span").get(),
                'link': quote.xpath("a/@href").get(),                
                }
            
        #next_link = response.xpath("//li[@class='next']/a/@href").get()
        #if next_link:
           # yield scrapy.Request(url=self.start_urls[0] + next_link)        
        
        
        
        pass
