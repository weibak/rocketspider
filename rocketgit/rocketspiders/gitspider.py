import logging
import scrapy

logger = logging.getLogger(__name__)


class GitSpider(scrapy.Spider):
    name = "github.com"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/bobuk/ujokesrv/"]

    def __init__(self, *args, **kwargs):
        logger = logging.getLogger("scrapy")
        logger.setLevel(logging.ERROR)
        super().__init__(*args, **kwargs)

    def parse(self, response, **kwargs):
        data = {
           "author": response.css(".fle-d:first-child .flex-auto .span author .a url fn::text").get(),
           "name": response.css(".flex-auto .strong name .a::text").get(),
           # "about": int(
            #    response.css(".anons-sku::text").get().replace("Арт. ", "")
            #),
           "url": f"url: {self.start_urls}",
           # "stars": int(price),
           # "forks": f'https://{self.allowed_domains[0]}{product.css(".anons-name a::attr(href)").get()}',
           # "watching": response.css(".anons-price-wrap .price span::text").get(),
           # "commit": response.css(".anons-price-wrap .price span::text").get(),
           # "last_commit": response.css(".anons-price-wrap .price span::text").get(),
           # "release": response.css(".anons-price-wrap .price span::text").get(),
           # "last_release": response.css(".anons-price-wrap .price span::text").get(),
        }
        logger.info(data)
        return data


