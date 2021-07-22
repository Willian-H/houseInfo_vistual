import scrapy


from house.items import HouseItem
count=1
class HousespiderSpider(scrapy.Spider):
    name = 'housespider'
    # allowed_domains = ['beike.com']
    start_urls = ['https://sjz.ke.com/ershoufang/tt9/']

    def parse(self, response):
        global count
        count=count+1
        all_msg=response.xpath("//div[@class='info clear']")
        for i in all_msg:
            house = HouseItem()
            house["houseaddress"]=i.xpath("div[@class='address']/div[@class='flood']/div[@class='positionInfo']/a/text()").extract()[0]
            data=i.xpath("div[@class='address']/div[@class='houseInfo']/text()").extract()[1].replace(" ","").replace("\n","")
            data1="|"
            house["housearea"]=str.split(data,data1)[-2][:-2]
            data2=str.split(data,data1)[:-2]
            house["housedescription"]=''.join(data2)
            # house["housedescription"]=str.split(data,data1)[0]+" "+str.split(data,data1)[1]+" "+str.split(data,data1)[2]
            house["houseprice"]=i.xpath("div[@class='address']/div[@class='priceInfo']/div[@class='totalPrice']/span/text()").extract()[0].replace(" ","").replace("\n","")
            house["housetitle"]=i.xpath("div[@class='title']/a/text()").extract()[0]
            yield house
        # next_page = response.xpath("//div[@class='page-box house-lst-page-box']/a[5]/@href").extract()
        # if next_page:
        #     url=response.urljoin(next_page.extract())
        #     yield scrapy.Request(url,self.parse)
        if(count < 67):
            url='https://sjz.ke.com/ershoufang/pg{}tt9/'.format(count)
            yield scrapy.Request(url, self.parse)
        pass
