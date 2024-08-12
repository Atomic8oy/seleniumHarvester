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

driver.implicitly_wait(10.0)

while "TSETMC" in driver.title:
    pass

date = datetime.now().strftime("%Y%m%d")

try:
    logger.log("File already exists. appending...", True)
    file = open(f"out/{OUT}-{date}.json")
    history = loads(file.read())
    file.close()
except:
    history = []

save = 0

massElm = driver.find_element(By.XPATH, '//*[@id="d09"]/div/div')
amountElm = driver.find_element(By.XPATH, '//*[@id="d08"]/div/div')

price = None
last = {
    "timestamp": None,
    "price": None,
    "mass": 0,
    "massChange": None,
    "amount": None
}

try:
    while True:
        if last["amount"] == int(amountElm.text.replace(",", "")):
            continue

        save += 1
        price = int(driver.title.split(" ")[1].replace(",", ""))
        time = int(datetime.now().timestamp())

        mass = float(massElm.text.replace("M", ""))

        amount = int(amountElm.text.replace(",", ""))


        last["timestamp"] = time
        last["price"] = price
        last["amount"] = amount
        last["massChange"] = mass-last["mass"]
        last["mass"] = mass

        logger.log(last, True)

        history.append(last)
        
        if save == 10:
            file = open(f"out/{OUT}-{date}.json", 'w')
            file.write(dumps(history))
            file.close()
            save = 0

except KeyboardInterrupt:
    logger.log(f"Saving the output in [out/{OUT}-{date}.json]")
    with open(f"out/{OUT}-{date}.json", 'w') as file:
        file.write(dumps(history))
    logger.done()