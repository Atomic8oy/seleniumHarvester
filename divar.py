from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from json import dumps

from config import KEYWORD, OUT
from utilities import log, convertDigits

log("Creating the webdriver")
browser = webdriver.Chrome()
log("[DONE]", True)

browser.implicitly_wait(10.0)

log(f"Heading to [https://divar.ir/s/{KEYWORD}/real-estate]")
browser.get(f"https://divar.ir/s/{KEYWORD}/real-estate")
log("[DONE]", True)

log("Getting the main element")
pth = '//*[@id="post-list-container-id"]/div[1]/div/div/div/div/div/div'
elements = browser.find_elements(By.XPATH, pth)
log("[DONE]", True)

id = 0
items = {}
with open(f"out/{OUT}.json", 'w', encoding='utf-8') as file:
    for elm in elements:
        log("Parsing the gray descriptions")
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
        log("[DONE]", True)

        log("Paring the red descriptions")
        try:
            x = elm.find_element(By.CLASS_NAME, "kt-post-card__red-text")
            row = x.text
            if "نردبان شده" in row:
                isLaddered = True
            if "فوری" in row:
                inHurry = True
            log("[DONE]", True)
        except NoSuchElementException:
            log("[NOT FOUND]", True)

        items.update({id: {
            "title": title,
            "promis": promis,
            "rent": rent, 
            "price": price, 
            "inHurry": inHurry, 
            "isLaddered": isLaddered,
            "fullRent": fullRent
        }})

        id += 1
        
    log(f"Writing the data in [out/{OUT}.json]")
    file.write(dumps(items)+"\n")
    log("[DONE]", True)


log("Quiting the application...")
browser.quit()