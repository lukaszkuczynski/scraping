URL = "https://www.morizon.pl/mieszkania/wroclaw/psie-pole/?ps%5Bprice_from%5D=400000&ps%5Bprice_to%5D=550000&ps%5Bmarket_type%5D%5B0%5D=2"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
# options.add_argument('headless')
# options.add_argument('window-size=0x0')
# driver = webdriver.Chrome(options=options)

from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

driver.get(URL)
print("wait started")
# driver.find_element(By.CSS_SELECTOR, "div.cmp-app_gdpr button.cmp-intro_acceptAll").click()

offers = driver.find_elements(By.CLASS_NAME, "row-content")

def safe_find_by_class(element, class_name):
    elems = element.find_elements(By.CLASS_NAME, class_name)
    if len(elems) > 0:
        return elems[0].text
    else:
        return None

def offers_generator():
    for offer in offers:
        title = offer.find_element(By.CLASS_NAME, "single-result__title").text
        date_added = safe_find_by_class(offer, "single-result__category--date")
        price = safe_find_by_class(offer, "single-result__price")
        description = safe_find_by_class(offer, "single-result__description")
        yield {
            "title": title,
            "date_added": date_added,
            "price": price,
            "description": description
        }

offers = list(offers_generator())
for offer in offers:
    print(offer)  

driver.close()

