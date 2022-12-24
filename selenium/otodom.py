URL = "https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/wroclaw/psie-pole?distanceRadius=0&page=1&limit=36&market=ALL&locations=%5Bdistricts_6-4%5D&by=DEFAULT&direction=DESC&viewType=listing&lang=pl&searchingCriteria=sprzedaz&searchingCriteria=mieszkanie&searchingCriteria=cala-polska"
WAITING_SECONDS = 5

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get(URL)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
driver.implicitly_wait(WAITING_SECONDS)


def safe_find_by_xpath(element, xpath):
    elems = element.find_elements(By.XPATH, xpath)
    if len(elems) > 0:
        return elems[0].text
    else:
        return None  

offers = driver.find_elements(By.XPATH, "//div[contains(@data-cy, 'search.listing')]//ul/li")

def safe_find_by_class(element, class_name):
    elems = element.find_elements(By.CLASS_NAME, class_name)
    if len(elems) > 0:
        return elems[0].text
    else:
        return None

def gen_offers(offer_divs):
    for offer in offers:
        if offer.is_displayed():
            location = safe_find_by_xpath(offer, "a/article/p/span")
            title = safe_find_by_xpath(offer, "a/article/div[1]/h3")
            price = safe_find_by_xpath(offer, "a/article/div[2]/span")
            if title:
                yield { 
                    "title": title,
                    "location": location,
                    "price": price
                }

offers_parsed = list(gen_offers(offers))

for offer in offers_parsed:
    print(offer)  

driver.close()

