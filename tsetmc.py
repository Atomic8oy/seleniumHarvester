from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium import webdriver
from json import dumps

from config import KEYWORD, OUT
from utilities import log

driver = webdriver.Chrome()

driver.implicitly_wait(20.0)

log(f"Heading to [https://www.tsetmc.com/History/65883838195688438/20240709]")
driver.get(f"https://www.tsetmc.com/History/65883838195688438/20240709")
log("[DONE]", True)

log("Doing the range bar thing")
pth = "/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/span/span[3]"
slider = driver.find_element(By.XPATH, pth)
slider.click()
for x in range(540, 862):
    slider.send_keys(Keys.ARROW_RIGHT)
log("[DONE]", True)

items = []
for x in range(540, 862):
    log(f"Reading {int(x/60)}:{x%60}")
    pth = "/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/table/tr[1]"
    elm = driver.find_element(By.XPATH, pth)
    price = elm.text.replace("آخرین معامله ", "")
    price = price.replace("(", "")
    price = price.replace(")", "")
    price = price.replace(",", "")
    price = price.split(" ")
    items.append({"time": x ,"price": price[0]})
    log("[DONE]", True)
    slider.send_keys(Keys.ARROW_LEFT)

with open(f"out/{OUT}.json", 'w') as file:
    file.write(dumps(items))