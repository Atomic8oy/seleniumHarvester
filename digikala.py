from selenium.webdriver.common.by import By
from selenium import webdriver
from json import dumps

from utilities import convertDigits, log
from config import KEYWORD, OUT

log("Creating the webdriver")
browser = webdriver.Chrome()
log("[DONE]", True)

log(f"Heading to [https://www.digikala.com/search/?q={KEYWORD}]")
browser.get(f"https://www.digikala.com/search/?q={KEYWORD}")
log("[DONE]", True)

browser.implicitly_wait(30.0)

log("Getting price elements")
pth = "//*[@id='ProductListPagesWrapper']/section[1]/div[2]/div/a/div/article/div[2]/div[2]/div[4]/div[1]/div/span"
elements = browser.find_elements(By.XPATH, pth)
log("[DONE]", True)


log("Harvesting and converting data")
items = {}
special = False
id = 0
for elm in elements:
    if "٪" in elm.text:
        special = True
        continue
    price = convertDigits(elm.text.replace(",", ""))
    items.update({id : {"price": price, "isSpecial": special}})
    special = False
    id += 1
log("[DONE]", True)

log(f"Writing output data in out/{OUT}.json")
with open(f"out/{OUT}.json", 'w') as file:
    file.write(dumps(items))
log("[DONE]", True)

log("Quiting the application...")
browser.quit()