"""
THIS PROGRAM IS SEPARATED FROM THE APP.
YOU SHOULD RUN IT MANUALLY
"""
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import base64

from utilities import Logger

NUMBER_OF_PICTURES = 2000

logger = Logger()

logger.log("Initializing")
opt = Options()
opt.add_argument("--log-level=1000")

driver = webdriver.Chrome(options=opt)

driver.implicitly_wait(10.0)

driver.get("https://kala.ntsw.ir")
logger.done()

driver.find_element(By.XPATH, '//*[@id="multi-step-form"]/div[1]/div/div[2]/div/div[1]').click()

sleep(2)

driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/button').click()

images = []

for n in range(NUMBER_OF_PICTURES):
    while True:
        try:
            captchaElm = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/main/div[1]/form/div[2]/div/div/div/div[2]/div[3]/div/img')
            img = base64.b64decode(captchaElm.get_attribute("src").split(",")[1])
            if img in images:
                continue
            images.append(img)
            driver.execute_script("RefreshCaptcha()")
            break
        except StaleElementReferenceException:
            continue

for x in range(len(images)):
    file = open(f"captcha/{x}.gif", 'wb')
    file.write(images[x])
    file.close()