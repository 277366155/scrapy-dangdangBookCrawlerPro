import scrapy
from dangdang.items import DangdangItem

class DangdangbookSpider(scrapy.Spider):
    name = 'dangdangbook'
    allowed_domains = ['dangdang.com']
    key='python'
    pageIndex=1
    host='http://search.dangdang.com'
    start_urls = ['http://search.dangdang.com/?key=%s&page_index=%d'%(key,pageIndex)]

    def parse(self, response):
        liList = response.xpath("//ul[@id='component_59']/li")
        #print(response.xpath("//ul[@name='Fy']/li[@class='next']/a/@href").extract_first())

        for li in liList:
            item=DangdangItem()
            item['title']= li.xpath("./p[@class='name']/a[@name='itemlist-title']/@title").extract_first()
            item['url'] = li.xpath("./p[@class='name']/a[@name='itemlist-title']/@href").extract_first()
            item['price']=li.xpath("./p[@class='price']/span[@class='search_pre_price']/text()").extract_first()
            item['realPrice']=li.xpath("./p[@class='price']/span[@class='search_now_price']/text()").extract_first()
            item['author']=li.xpath("./p[@class='search_book_author']/span[1]").xpath("string(.)").extract_first()
            item['press']=li.xpath("./p[@class='search_book_author']/span[3]").xpath("string(.)").extract_first().strip().replace("/","")
            item['detail']= li.xpath("./p[@class='detail']/text()").extract_first()

            yield item

        nextPageUrl = response.xpath("//ul[@name='Fy']/li[@class='next']/a/@href").extract_first()
        if nextPageUrl is not None:
            print("nextPageUrl=",nextPageUrl)
            yield scrapy.Request(self.host +nextPageUrl,callback=self.parse)




