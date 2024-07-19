from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from json import dumps

from config import KEYWORD, OUT
from utilities import Logger

logger = Logger()

driver = webdriver.Chrome()

driver.implicitly_wait(5.0)

logger.log(f"Heading to [https://www.tsetmc.com/History/{KEYWORD}]")
driver.get(f"https://www.tsetmc.com/History/{KEYWORD}")
logger.log("[DONE]", True)

logger.log("Doing the range bar thing")
pth = "/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/span/span[3]"
slider = driver.find_element(By.XPATH, pth)
slider.click()
for x in range(540, 862):
    slider.send_keys(Keys.ARROW_RIGHT)
logger.log("[DONE]", True)

driver.implicitly_wait(0.0)

items = []
for x in range(540, 862):
    logger.log(f"Reading {int(x/60)}:{x%60}")

    pth = '/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/table/tr[1]'
    elm = driver.find_element(By.XPATH, pth)
    price = elm.text
    price = price.replace("آخرین معامله ", "")
    try:
        change = elm.find_element(By.XPATH, '//*[@id="d02"]/span').text
        price = price.replace(change, "")
    except NoSuchElementException:
        change = None
    
    transactionsCount = driver.find_element(
        By.XPATH,
        '//*[@id="MainContent"]/div[1]/div[4]/div[3]/table/tr[1]'
    ).text.replace("تعداد معاملات ", "")

    transactionsMass = driver.find_element(
        By.XPATH,
        '//*[@id="MainContent"]/div[1]/div[4]/div[3]/table/tr[2]'
    ).text.replace("حجم معاملات ", "")

    transactionsWorth = driver.find_element(
        By.XPATH,
        '//*[@id="MainContent"]/div[1]/div[4]/div[3]/table/tr[3]'
    ).text.replace("ارزش معاملات ", "")

    items.append({
        "time": x ,
        "price": price, 
        "change": change, 
        "transactionCount": transactionsCount,
        "transactionsMass": transactionsMass,
        "transactionsWorth": transactionsWorth
    })

    slider.send_keys(Keys.ARROW_LEFT)
    logger.log("[DONE]", True)

logger.log(f"Writing the result in [out/{OUT}.json]")
with open(f"out/{OUT}.json", 'w') as file:
    file.write(dumps(items))
logger.log("[DONE]", True)

driver.quit()