# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup   

class MediumtopicSpider(scrapy.Spider):
    name = 'mediumtopic'
    topic = ""

    def start_requests(self):
        yield scrapy.Request('https://medium.com/topic/%s' % self.topic)

    def parse(self, response):
        div_articles = response.selector.xpath("/html/body/div/div/div[3]/div/div/div[1]/div[4]/div[1]")
        titles_sel = div_articles.xpath("//h3[contains(@class, 'ap')]")
        # for titles: we should have 12 elements, 1 main, 3 latest, 1 author, 7 other
        titles = titles_sel.getall()[1:4]
        desc_sel = div_articles.xpath("//h3[contains(@class, 'gc')]")                                                                                                                                      
        # for descriptions: we should have 14 elements, 1 main - doubled!, 3 latest, 2 authors, 7 other
        descriptions = desc_sel.getall()[2:5]
        latest = zip(titles, descriptions)

        for title, desc in latest:
            title_soup = BeautifulSoup(title, 'html.parser')
            desc_soup = BeautifulSoup(desc, 'html.parser')
            yield {
                "title": title_soup.h3.text,
                "description": desc_soup.h3.text,
                "link": title_soup.a['href']
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
