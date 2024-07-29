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

pth = "/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/span/span[3]"
slider = driver.find_element(By.XPATH, pth)
slider.click()

driver.implicitly_wait(0.0)

items = []
time = 0
while (time != 540):
    time = int(slider.get_attribute("aria-valuenow"))
    logger.log(f"Reading {int(time/60)}:{time%60}")

    pth = '/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/table/tr[1]'
    elm = driver.find_element(By.XPATH, pth)
    price = elm.text
    price = price.replace("آخرین معامله ", "")
    try:
        change = elm.find_element(By.XPATH, '//*[@id="d02"]/span').text
        price = price.replace(change, "")
        change = float(change[change.index("(")+1:change.index("%")])

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

    items.insert(0, {
        "time": time ,
        "price": int(price.replace(",", "")), 
        "change": change, 
        "transactionCount": int(transactionsCount.replace(",", "")),
        "transactionsMass": int(transactionsMass.replace(",", "")),
        "transactionsWorth": int(transactionsWorth.replace(",", ""))
    })

    slider.send_keys(Keys.RIGHT)
    logger.log("[DONE]", True)

logger.log(f"Writing the result in [out/{OUT}.json]")
with open(f"out/{OUT}.json", 'w') as file:
    file.write(dumps(items))
logger.log("[DONE]", True)

driver.quit()