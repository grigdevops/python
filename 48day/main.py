from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path="/home/grigor/Development/chromedriver_linux64/chromedriver"

driver_service = Service("/home/grigor/Development/chromedriver_linux64/chromedriver")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options,service=driver_service)



driver.get("https://www.amazon.com/HP-Upgraded-Touch-Screen-Business-Generation/dp/B0BNDSHCCM/ref=sr_1_1_sspa?crid=YPV09IWGXPY8&keywords=hp%2Blaptops&qid=1674549703&sprefix=hp%2B%2Caps%2C240&sr=8-1-spons&smid=A9D6J376CGTLK&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFESVRWMkRYVU1KNEkmZW5jcnlwdGVkSWQ9QTAyMTAxNjJZRVE2TVNMNFdTN1EmZW5jcnlwdGVkQWRJZD1BMDkzMTkxM1RDOFY4RlZHN0VJOCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1")


price = driver.find_element(By.CLASS_NAME, "a-price-whole")

print(price.text)
# time.sleep(4)
# driver.close()
driver.quit()