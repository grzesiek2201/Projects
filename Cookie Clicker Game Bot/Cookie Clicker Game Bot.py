from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from time import time

chrome_driver_path = "D:\\chromedriver_win32\\chromedriver.exe"
URL = "http://orteil.dashnet.org/experiments/cookie/"
TIMEOUT = 600
ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)
driver.get(url=URL)

upgrades_id = ["buyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment", "buyMine", "buyFactory", "buyGrandma", "buyCursor"]

cookie_button = driver.find_element(By.ID, "cookie")

iterations = 1
time_ref = time()
while time() - time_ref < TIMEOUT:
    for _ in range(iterations):
        cookie_button.click()

    for upgrade_id in upgrades_id:
        try:
            driver.find_element(By.ID, upgrade_id).click()
        except NoSuchElementException:
            continue
        except StaleElementReferenceException:
            continue

    iterations += 100


