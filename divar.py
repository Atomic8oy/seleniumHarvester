from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from json import dumps
from time import sleep

from config import KEYWORD, OUT, SCROLL, SCROLL_AMOUNT
from utilities import convertDigits, exists, Logger

logger = Logger()

logger.log("Creating the webdriver")
browser = webdriver.Chrome()
logger.done()

browser.implicitly_wait(5.0)

logger.log(f"Heading to [https://divar.ir/s/{KEYWORD}/real-estate]")
browser.get(f"https://divar.ir/s/{KEYWORD}/real-estate")
logger.done()

id = 0
items = []
for x in range(SCROLL):
    logger.log("Getting the main element")
    pth = '//*[@id="post-list-container-id"]/div[1]/div/div/div/div/div/div'
    elements = browser.find_elements(By.XPATH, pth)
    logger.done()

    for elm in elements:
        logger.log("Parsing the gray descriptions")
        title = None
        promis = None
        rent = None
        price = None
        inHurry = False
        isLaddered = False
        fullRent = False

        isPrice = False

        title = elm.find_element(By.CLASS_NAME, "kt-post-card__title").text
        for x in elm.find_elements(By.CLASS_NAME, "kt-post-card__description"):
            row = x.text.replace(" ", "")
            if "تومان" in row: 
                isPrice = True
                row = row.replace("تومان", "")
            row = row.replace(",", "")
            if isPrice and ":" in row:
                row = row.split(':')
                if row[0] == "ودیعه":
                    promis = convertDigits(row[1])
                elif row[0] == "اجاره":
                    rent = convertDigits(row[1])
                continue
            elif isPrice:
                price = convertDigits(row)
                continue

            if "رهن کامل" in row:
                fullRent = True
                continue
        logger.done()

        logger.log("Parsing the red descriptions")
        try:
            x = elm.find_element(By.CLASS_NAME, "kt-post-card__red-text")
            row = x.text
            if "نردبان شده" in row:
                isLaddered = True
            if "فوری" in row:
                inHurry = True
            logger.done()
        except NoSuchElementException:
            logger.log("[NOT FOUND]", True)

        item = {
            "title": title.replace("/", " ").split(" "),
            "promis": promis,
            "rent": rent, 
            "price": price, 
            "inHurry": inHurry, 
            "isLaddered": isLaddered,
            "fullRent": fullRent
        }

        if not exists(item, items):
            item.update({"id": id})
            items.append(item)
            id += 1

    logger.log("Scrolling down")
    browser.execute_script(f"window.scrollBy(0,{SCROLL_AMOUNT})")
    logger.done()

with open(f"out/{OUT}.json", 'w') as file:
    logger.log(f"Writing the data in [out/{OUT}.json]")
    file.write(dumps(items)+"\n")
    logger.done()

browser.quit()