from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from json import dumps
from time import sleep

from utilities import Logger, convertDigits

logger = Logger()

logger.log("Initializing")
driver = webdriver.Chrome()

driver.implicitly_wait(20.0)

driver.get("http://search-hamivakil.ir")
logger.done()

logger.log(f"Selecting the select bar")
provSelect = Select(driver.find_element(value="seBar"))
provSelect.select_by_value("163163ca2cc94a229989ceea75e762f4")
logger.done()

logger.log("Clicking on the search button")
driver.find_element(value="btnSearchLawyer").click()
logger.done()

logger.log("Getting the code elements")
codeElms = driver.find_elements(By.XPATH, '//*[@id="personNumberResultsGriddatacontainer"]/div/span')
logger.done()

codes = []
for elm in codeElms:
    logger.log(elm.text, True)
    codes.append(elm.text)

lawyers = []
for code in codes:
    while True:
        try:
            sleep(20.0)
            logger.log(f"Getting {code}", True)
            driver.get(f"http://search-hamivakil.ir/Lawyer/{code}/")

            prov = driver.find_element(value="lastClub").text
            name = driver.find_element(value="name").text
            surName = driver.find_element(value="family").text
            phone = convertDigits(driver.find_element(value="mobileNumber").text)
            office = convertDigits(driver.find_element(value="officeTelNumber").text)
            state = driver.find_element(value="workstate").text
            degree = driver.find_element(value="lawyerDegree").text
            address = driver.find_element(value="lawyerDegree").text

            lawyers.append({
                "name": name,
                "surName": surName,
                "province": prov,
                "degree": degree,
                "state": state,
                "phoneNumber": phone,
                "officeNumber": office,
                "address": address
            })

            break
        except:
            continue

logger.log(f"Writing the data")
with open(f"out/vakilGolestan.json", 'w') as outFile:
    outFile.write(dumps(lawyers))
logger.done()

logger.log("Quiting the application", True)
driver.quit()