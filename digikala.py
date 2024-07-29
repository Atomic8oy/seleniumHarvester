from selenium.webdriver.common.by import By
from selenium import webdriver
from json import dumps

from utilities import convertDigits, exists, Logger
from config import KEYWORD, OUT, SCROLL, SCROLL_AMOUNT

logger = Logger()

logger.log("Creating the webdriver")
browser = webdriver.Chrome()
logger.done()

logger.log(f"Heading to [https://www.digikala.com/search/?q={KEYWORD}]")
browser.get(f"https://www.digikala.com/search/?q={KEYWORD}")
logger.done()

browser.implicitly_wait(10.0)

for x in range(SCROLL):
    logger.log("Getting price elements")
    pth = "//*[@id='ProductListPagesWrapper']/section[1]/div[2]/div/a/div/article/div[2]/div[2]/div[4]/div[1]/div/span"
    elements = browser.find_elements(By.XPATH, pth)
    logger.done()


    logger.log("Harvesting and converting data")
    items = []
    special = False
    id = 0
    for elm in elements:
        if "٪" in elm.text:
            special = True
            continue
        price = convertDigits(elm.text.replace(",", ""))

        item = {"price": price, "isSpecial": special}
        if not exists(item, items):
            item.update({"id": id})
            items.append(item)
            id += 1
        special = False
        
    logger.done()

    browser.execute_script(f"window.scrollBy(0,{SCROLL_AMOUNT})")

logger.log(f"Writing output data in out/{OUT}.json")
with open(f"out/{OUT}.json", 'w') as file:
    file.write(dumps(items))
logger.done()

browser.quit()