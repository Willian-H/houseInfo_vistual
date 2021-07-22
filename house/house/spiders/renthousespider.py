import scrapy
from house.items import RentHouseItem
count=1
class RenthousespiderSpider(scrapy.Spider):
    name = 'renthousespider'
    start_urls = ['https://sjz.zu.ke.com/zufang']

    def parse(self, response):
        global count
        count=count+1
        all_msg=response.xpath("//div[@class='content__list--item--main']")
        for i in all_msg:
            house = RentHouseItem()
            house["houseaddress"] = i.xpath("p[@class='content__list--item--des']/a[1]/text()").extract()[0]+i.xpath("p[@class='content__list--item--des']/a[2]/text()").extract()[0]+i.xpath("p[@class='content__list--item--des']/a[3]/text()").extract()[0]
            data_all = i.xpath("p[@class='content__list--item--des']/text()").extract()
            house["housedescription"] = data_all[-2].replace(" ","").replace("\n","")
            data1=data_all[-4].replace(" ","").replace("\n","")
            house["housearea"]=data1[:-2]
            house["houseprice"]=i.xpath("span[@class='content__list--item-price']/em/text()").extract()[0].replace(" ","").replace("\n","")
            house["housetitle"]=i.xpath("p[@class='content__list--item--title']/a/text()").extract()[0].replace(" ","").replace("\n","")
            yield house
        if(count < 31):
            url='https://sjz.zu.ke.com/zufang/pg{}/#contentList/'.format(count)
            yield scrapy.Request(url, self.parse)
        pass
