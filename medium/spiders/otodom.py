# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup   

ARTICLE_PATH = "//article//div"
START_PATH = "https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/cala-polska"
START_PATH = "https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/wroclaw/psie-pole"
PATH_ARGUMENTS = "?market=ALL&viewType=listing&lang=pl&searchingCriteria=sprzedaz&searchingCriteria=mieszkanie"
PATH_ARGUMENTS = "?distanceRadius=0&page=1&limit=36&market=ALL&locations=%5Bdistricts_6-4%5D&by=DEFAULT&direction=DESC&viewType=listing&lang=pl&searchingCriteria=sprzedaz&searchingCriteria=mieszkanie&searchingCriteria=cala-polska"

class OtotdomSpider(scrapy.Spider):
    name = 'otodom'

    def start_requests(self):
        yield scrapy.Request(START_PATH + PATH_ARGUMENTS)

    def parse(self, response):
        div_offers = response.xpath("//div[contains(@data-cy, 'search.listing')]//ul/li")
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