from selenium.webdriver.common.by import By
from selenium import webdriver
from json import dumps

from config import KEYWORD, OUT
from utilities import log

log("Creating the webdriver")
browser = webdriver.Chrome()
log("[DONE]", True)

browser.implicitly_wait(30.0)

log(f"Heading to [https://divar.ir/s/{KEYWORD}/real-estate]")
browser.get(f"https://divar.ir/s/{KEYWORD}/real-estate")
log("[DONE]", True)

log("Getting title elements and parsing the data")
pth = '//*[@id="post-list-container-id"]/div[1]/div/div/div/div/div/div'
elements = browser.find_elements(By.XPATH, pth)

id = 0
item = {}
try:
    for elm in elements:
        with open(f"out/{OUT}.txt", 'a', encoding='utf-8') as file:
            file.write(elm.find_element(By.CLASS_NAME, "kt-post-card__title"))

    log("[DONE]", True)
except:
    log("[FAILED]", True)

log("Quiting the application...")
browser.quit()