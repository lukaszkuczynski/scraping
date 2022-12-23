# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup   
from scrapy_playwright.page import PageMethod

ARTICLE_PATH = "//article//div"
START_PATH = "https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/cala-polska"
START_PATH = "https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/wroclaw/psie-pole"
PATH_ARGUMENTS = "?market=ALL&viewType=listing&lang=pl&searchingCriteria=sprzedaz&searchingCriteria=mieszkanie"
PATH_ARGUMENTS = "?distanceRadius=0&page=1&limit=36&market=ALL&locations=%5Bdistricts_6-4%5D&by=DEFAULT&direction=DESC&viewType=listing&lang=pl&searchingCriteria=sprzedaz&searchingCriteria=mieszkanie&searchingCriteria=cala-polska"

class OtotdomSpider(scrapy.Spider):
    name = 'otodom'

    def start_requests(self):
        url = START_PATH + PATH_ARGUMENTS
        yield scrapy.Request(url, meta=dict(
                playwright = True,
                playwright_include_page = True, 
                playwright_page_methods =[
        #   PageMethod("wait_for_selector", "div."),
          PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)"),
        #   PageMethod("wait_for_selector", 'h3[data-cy="listing-item-title":nth-child(20)'),  # 10 per page
          ],
        errback=self.errback,
            ))

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()

    async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.close()
        div_offers = response.xpath("//div[contains(@data-cy, 'search.listing')]//ul/li")
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        for offer in div_offers:
            location = offer.xpath("a/article/p/span/text()")
            title = offer.xpath("a/article/div[1]/h3/text()")
            price = offer.xpath("a/article/div[2]/span/text()")
            if title:
                yield { 
                    "title": title.get(),
                    "location": location.get(),
                    "price": price.get()
                }