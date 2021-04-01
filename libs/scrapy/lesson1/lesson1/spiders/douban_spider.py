import scrapy

from lesson1.items import Lesson1Item

class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    # 允许访问域名
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    # 解析
    def parse(self, response):

        movie_list = response.xpath("//ol[@class='grid_view']//li")

        for item in movie_list:
            mItem = Lesson1Item()
            mItem['serial_number'] = item.xpath(".//div[@class='item']//em/text()").extract_first()
            mItem['movie_name'] = item.xpath(".//div[@class='item']//div[@class='info']//span[@class='title'][1]/text()").extract_first()
            content = item.xpath(".//div[@class='item']//div[@class='bd']/p[1]/text()").extract()
            for i_content in content:
                content_s = ''.join(i_content.split())
                mItem['introduce'] = content_s
            mItem['star'] = item.xpath(".//div[@class='item']//div[@class='bd']//span[@class='rating_num'][1]/text()").extract_first()
            mItem['evaluate'] = item.xpath(".//div[@class='item']//div[@class='bd']//div[@class='star']//span[4]/text()").extract_first()
            mItem['desc'] = item.xpath(".//div[@class='item']//div[@class='bd']//p[@class='quote']//span[1]/text()").extract_first()

            yield mItem

        # 下一页
        next_link = response.xpath("//div[@class='paginator']/span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link, callback=self.parse)
