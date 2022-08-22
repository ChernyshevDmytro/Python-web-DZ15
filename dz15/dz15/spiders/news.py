import scrapy
from bs4 import BeautifulSoup

class NewsSpider(scrapy.Spider):
    name = 'news'
    a='www.ua.korrespondent.net'
    b= 'https://ua.korrespondent.net/'
    allowed_domains = ['www.pravda.com.ua', 'www.ua.korrespondent.net',]
    start_urls = ['http://www.pravda.com.ua/', 'https://ua.korrespondent.net/',]


    def parse(self, response):
        if str(response.request) == str("<GET https://www.pravda.com.ua/>"):            
            for quote in response.xpath("/html//div[@class='container_sub_news_wrapper']/div[@class='article_news']"):
                link = quote.xpath('div[@class="article_header"]/a/@href').get()
                if "vda.com.ua/" not in link:
                    full_link= f"http://www.pravda.com.ua{link}"
                else:
                   full_link = link     

                yield {
                    'title': quote.xpath('div[@class="article_header"]/a/span/text()').get(),
                    'link': full_link,
                    'source' : "pravda.com.ua"           
                    }

        if str(response.request) == str("<GET https://ua.korrespondent.net/>"):            
            print(response.request)
            for quote in response.xpath("/html//div[@class='article__title']"):        
                link = quote.xpath('a/@href').get()
                yield {
                    'title': quote.xpath('a/text()').get(),
                    'link': link,
                    'source' : "ua.korrespondent.net"           
                    }                

            
        #next_link = response.xpath("//li[@class='next']/a/@href").get()
        #if next_link:
           # yield scrapy.Request(url=self.start_urls[0] + next_link)   
