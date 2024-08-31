import scrapy


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    allowed_domains = ["www.imdb.com"]
    start_urls = [
      "https://rajanigroup.in/product"
   ]
    def parse(self, response):
        colunms = response.css('div.tab-pane div.row')
        for coulunm in colunms:
            yield{
                "Title": coulunm.css('h3::text').get(),
                "Image": coulunm.css('img[class="img-fluid product-img"]::attr(src)').get(),
                "Price & quantity": coulunm.css('h4[class="col-12 text-center"]::text').get()
            }
        pass
