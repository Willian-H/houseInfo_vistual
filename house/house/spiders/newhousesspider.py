import scrapy


from house.items import NewHouseItem
count=1
class HousespiderSpider(scrapy.Spider):
    name = 'newhousesspider'
    # allowed_domains = ['beike.com']
    start_urls = ['https://sjz.fang.ke.com/loupan']

    def parse(self, response):
        global count
        count=count+1
        all_msg=response.xpath("//div[@class='resblock-desc-wrapper']")
        for i in all_msg:
            house = NewHouseItem()
            house["houseaddress"] = i.xpath("a[1]/@title").extract()[0]
            if (i.xpath("a[@class='resblock-room']/span[1]/text()").extract()):
                temp0 = i.xpath("a[@class='resblock-room']/span/text()").extract()
                temp1 = i.xpath("a[@class='resblock-room']/span[@class='area']/text()").extract()
                temp2= ''.join(temp0)
                temp3=''.join(temp1)
                house["housedescription"]=temp2.replace(temp3,'')
            else:
                house["housedescription"] = "暂无描述!"
            house["houseprice"] = i.xpath("div[@class='resblock-price']/div[@class='main-price']/span[1]/text()").extract()[0]
            if (i.xpath("a[@class='resblock-room']/span[last()]/text()").extract()):
                # list=i.xpath("a[@class='resblock-room']/span[4]/text()").extract()
                # for data in list:
                #     data1=data
                # data2=data1[3:]
                house["housearea"]=i.xpath("a[@class='resblock-room']/span[last()]/text()").extract()[0][3:-1]
            else:
                house["housearea"]="暂无描述"
            house["housetitle"] = i.xpath("div[@class='resblock-name']/a/text()").extract()[0]
            yield house

        if(count < 55):
            url='https://sjz.fang.ke.com/loupan/pg{}'.format(count)
            yield scrapy.Request(url, self.parse)
        pass
