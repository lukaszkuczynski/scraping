# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup   

ARTICLE_PATH = "//article//div"

class MediumtopicSpider(scrapy.Spider):
    name = 'mediumtopic'
    topic = "data-science"

    def start_requests(self):
        yield scrapy.Request('https://medium.com/tag/%s' % self.topic)

    def parse(self, response):
        from scrapy.shell import inspect_response
        inspect_response(response, self)

        div_articles = div_articles.xpath("//div[contains(@class, 'kh')]")
        title_html = article_sel.get("//a/div/h2/text()")


        # div_articles = response.selector.xpath(ARTICLE_PATH)
        # titles_sel = div_articles.xpath("//div[contains(@class, 'kh')]")
        # # for titles: we should have 12 elements, 1 main, 3 latest, 1 author, 7 other
        # titles = titles_sel.getall()[1:4]
        # desc_sel = div_articles.xpath("//h3[contains(@class, 'gc')]")                                                                                                                                      
        # # for descriptions: we should have 14 elements, 1 main - doubled!, 3 latest, 2 authors, 7 other
        # descriptions = desc_sel.getall()[2:5]
        # latest = zip(titles, descriptions)

        # for title, desc in latest:
        #     title_soup = BeautifulSoup(title, 'html.parser')
        #     desc_soup = BeautifulSoup(desc, 'html.parser')
        #     yield {
        #         "title": title_soup.h3.text,
        #         "description": desc_soup.h3.text,
        #         "link": title_soup.a['href']
        #     }


if __name__ == "__main__":
    import requests    
    request_object = requests.get("https://medium.com/tag/data-science/")
    response_object = scrapy.Selector(request_object )
    div_articles = response_object.xpath(ARTICLE_PATH)
    # print(div_articles)
    article_sel = div_articles.xpath("//div[contains(@class, 'kh')]")
    title_html = article_sel.get("//a/div/h2/text()")
    print(title_html)
    # soup = BeautifulSoup(title_html, 'html.parser')
    # print(soup)
