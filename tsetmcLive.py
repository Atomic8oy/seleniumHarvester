from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
from json import dumps, loads

from utilities import Logger
from config import KEYWORD, OUT

logger = Logger()

logger.log("Initializing")
driver = webdriver.Chrome()

driver.get(f"https://tsetmc.com/instInfo/{KEYWORD}")
logger.done()

while "TSETMC" in driver.title:
    pass

date = datetime.now().strftime("%Y%m%d")

try:
    file = open(f"out/{OUT}-{date}.json")
    history = loads(file.read())
    file.close()
except:
    history = []

price = None
try:
    while True:
        if price == int(driver.title.replace("خودرو ", "").replace(",", "")):
            continue

        price = int(driver.title.replace("خودرو ", "").replace(",", ""))
        time = datetime.now().timestamp()
        
        logger.log(price, True)

        history.append({
            "timestamp": time,
            "price": price 
        })

except KeyboardInterrupt:
    logger.log(f"Saving the output in [out/{OUT}-{date}.json]")
    file = open(f"out/{OUT}-{date}.json", 'w')
    file.write(dumps(history))
    file.close()
    logger.done()

driver.close()