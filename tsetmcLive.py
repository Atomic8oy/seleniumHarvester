from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
from json import dumps, loads
from matplotlib import pyplot
import numpy

from utilities import Logger
from config import KEYWORD, OUT

logger = Logger()

logger.log("Initializing")

def save()-> None:
    logger.log("Saving")
    pyplot.clf()

    x = numpy.array([datetime.fromtimestamp(sub['timestamp']) for sub in history])
    y = numpy.array([sub["price"] for sub in history])

    pyplot.plot(x, y)
    pyplot.savefig(f"out/{OUT}-{date}.png")

    file = open(f"out/{OUT}-{date}.json", 'w')
    file.write(dumps(history))
    file.close()
    logger.done()

driver = webdriver.Chrome()

driver.get(f"https://tsetmc.com/instInfo/{KEYWORD}")

pyplot.title(OUT)
pyplot.xlabel("ID")
pyplot.ylabel("Price")
pyplot.grid()
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

_save = 0

massElm = driver.find_element(By.XPATH, '//*[@id="d09"]/div/div')
amountElm = driver.find_element(By.XPATH, '//*[@id="d08"]/div/div')

price = None
lastMass = 0
lastAmount = None

try:
    while True:
        if lastAmount == int(amountElm.text.replace(",", "")):
            continue

        _save += 1
        price = int(driver.title.split(" ")[1].replace(",", ""))
        time = int(datetime.now().timestamp())
        
        mass = float(massElm.text.replace("M", ""))

        amount = int(amountElm.text.replace(",", ""))

        logger.log({
            "timestamp": time,
            "price": price,
            "amount": amount,
            "massChange": mass-lastMass,
            "mass": mass
        }, True)
        history.append({
            "timestamp": time,
            "price": price,
            "amount": amount,
            "massChange": mass-lastMass,
            "mass": mass
        })

        lastAmount = amount
        lastMass = mass

        if _save == 5:
            save()
            
            _save = 0

except KeyboardInterrupt:
    save()