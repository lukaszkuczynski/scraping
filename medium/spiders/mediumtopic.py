# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup   

MAX_HEADERS = 8

class MediumtopicSpider(scrapy.Spider):
    name = 'mediumtopic'

    def start_requests(self):
        yield scrapy.Request('https://medium.com/topic/%s' % self.topic)

    def parse(self, response):
        div_articles = response.selector.xpath("/html/body/div/div/div[3]/div/div/div[1]/div[4]/div[1]")
        h3_sel = div_articles.xpath("//h3")
        for h3_html in h3_sel.getall()[:MAX_HEADERS]:
            soup = BeautifulSoup(h3_html, 'html.parser')
            yield {
                "text": soup.h3.text,
                "link": soup.a['href']
            }


if __name__ == "__main__":

    def fetch(a):
        pass
    response = None

    from bs4 import BeautifulSoup   
    MAX_HEADERS = 6
    fetch("https://medium.com/topic/data-science/")
    div_articles = response.selector.xpath("/html/body/div/div/div[3]/div/div/div[1]/div[4]/div[1]")
    h3_sel = div_articles.xpath("//h3")
    h3_html = h3_sel.get()
    soup = BeautifulSoup(h3_html, 'html.parser')

