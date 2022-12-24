# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup   
from scrapy_playwright.page import PageMethod

URL = "https://www.morizon.pl/mieszkania/wroclaw/psie-pole/?ps%5Bprice_from%5D=400000&ps%5Bprice_to%5D=550000&ps%5Bmarket_type%5D%5B0%5D=2"
class MorizonSpider(scrapy.Spider):
    name = 'morizon'

    def start_requests(self):
        url = URL
        # yield scrapy.Request(url)
        yield scrapy.Request(url, meta=dict(
                playwright = True,
                playwright_include_page = True, 
                playwright_page_methods =[
            # PageMethod("wait_for_selector", "div.row-content"),
        #   PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)"),
        #   PageMethod("wait_for_selector", "footer"), 
          ],
        errback=self.errback,
            ))

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()

async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.close()
        from scrapy.shell import inspect_response
        inspect_response(response, self)

        # div_offers = response.xpath("//div[contains(@data-cy, 'search.listing')]//ul/li")
        # for offer in div_offers:
        #     location = offer.xpath("a/article/p/span/text()")
        #     title = offer.xpath("a/article/div[1]/h3/text()")
        #     price = offer.xpath("a/article/div[2]/span/text()")
        #     if title:
        #         yield { 
        #             "title": title.get(),
        #             "location": location.get(),
        #             "price": price.get()
        #         }