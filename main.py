import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"G:/Selenium Driver"
driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")
driver.implicitly_wait(3)
my_element = driver.find_element_by_id('mc-embedded-subscribe')
my_element.click()

# method designed to wait 30s until the text has the expected text
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, ), #Element filtration
        '' # The expected text
    )
)

