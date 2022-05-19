import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# os.environ['PATH'] += r"G:/Selenium Driver"
# driver = webdriver.Chrome()
# driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")
# driver.implicitly_wait(3)
# my_element = driver.find_element_by_id('mc-embedded-subscribe')
# my_element.click()

# method designed to wait 30s until the text has the expected text
# WebDriverWait(driver, 30).until(
#     EC.text_to_be_present_in_element(
#         (By.CLASS_NAME, ), #Element filtration
#         '' # The expected text
#     )
# )

# os.environ['PATH'] += r"G:/Selenium Driver"
# driver = webdriver.Chrome()
# driver.get("https://sg.yahoo.com/?p=us")
# driver.implicitly_wait(3)
# searchBox = driver.find_element_by_id('ybar-sbq')
# searchBox.send_keys('aws')
# # searchBox.send_keys(Keys.NUMPAD1, Keys.NUMPAD4)

# searchButton = driver.find_element_by_id('ybar-search')
# searchButton.click()
# # searchButton = driver.find_element_by_css_selector('button[class="btn btn-primary"]')
# # searchButton.click()

# os.environ['PATH'] += r"G:/Selenium Driver"
# driver = webdriver.Chrome()
# driver.get('https://youtube.com')
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='search_query']"))).send_keys("youtube test")
# driver.find_element_by_css_selector('button[id="search-icon-legacy"]').click()

