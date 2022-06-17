import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
import string
import random
from random import randint


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
# searchBox.send_keys(Keys.NUMPAD1, Keys.NUMPAD4)

# searchButton = driver.find_element_by_id('ybar-search')
# searchButton.click()
# # searchButton = driver.find_element_by_css_selector('button[class="btn btn-primary"]')
# # searchButton.click()

# os.environ['PATH'] += r"G:/Selenium Driver"
# driver = webdriver.Chrome()
# driver.get('https://youtube.com')
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='search_query']"))).send_keys("youtube test")
# driver.find_element_by_css_selector('button[id="search-icon-legacy"]').click()

os.environ['PATH'] += r"G:/Selenium Driver"
driver = webdriver.Chrome()
url = 'https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp'
driver.get(url)
driver.implicitly_wait(3)

firstName = driver.find_element_by_css_selector('input[name="firstName"]')
first_name = ""
for i in range(0, 8):
    first_name += random.choice(string.ascii_letters)
firstName.send_keys(first_name)
print("First Name: " + first_name)

time.sleep(1)

lastName = driver.find_element_by_css_selector('input[name="lastName"]')
last_name = ""
for i in range(0, 8):
    last_name += random.choice(string.ascii_letters)
lastName.send_keys(last_name)
print("Last Name: " + last_name)

time.sleep(1)

userName = driver.find_element_by_css_selector('input[id="username"]')
user_name = ""
for i in range(0, 10):
    user_name += random.choice(string.ascii_letters)
for i in range(0, 4):
    user_name += str(randint(0, 9))

userName.send_keys(user_name)
print("User Name: " + user_name)

time.sleep(1)

password = driver.find_element_by_css_selector('input[name="Passwd"]')
pass_word = ""
for i in range(0, 10):
    pass_word += random.choice(string.ascii_letters)
for i in range(0, 4):
    pass_word += str(randint(0, 9))
password.send_keys(pass_word)
print("Password: " + pass_word)

time.sleep(1)

confirmPassword = driver.find_element_by_css_selector('input[name="ConfirmPasswd"]')
confirmPassword.send_keys(pass_word)
print("Password: " + pass_word)

time.sleep(1)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[jscontroller='soHxf']"))).click()

time.sleep(2)

telephone = driver.find_element_by_css_selector('input[type="tel"]')
telephone.send_keys('Your own phone number')

time.sleep(2)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[jscontroller='soHxf']"))).click()

time.sleep(25)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[jscontroller='soHxf']"))).click()


# enter you verification code




#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# from bs4 import BeautifulSoup
# import requests
# import time

# with open('home.html', 'r') as html_file:
#     content = html_file.read()

#     soup = BeautifulSoup(content, 'lxml')
#     courses_html_tags = soup.find_all('h5')
#     for course in courses_html_tags:
#         print(course.text)

# with open('home.html', 'r') as html_file:
#     content = html_file.read()

#     soup = BeautifulSoup(content, 'lxml')
#     courses_html_tags = soup.find_all('h5')
#     course_cards = soup.find_all('div', class_='card')
#     for course in course_cards:
#         course_name = course.h5.text
#         course_price = course.a.text.split()[-1]

#         print(f'{course_name} costs {course_price}')

# print('Put some skill that you are not familiar with')
# unfamiliar_skill = input('>')
# print(f'Filtering out {unfamiliar_skill}')

# def find_jobs():
#     url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
#     html_text = requests.get(url).text
#     soup = BeautifulSoup(html_text, 'lxml')
#     jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

#     for index, job in enumerate(jobs):
#         published_date = job.find('span', class_='sim-posted').span.text

#         if "1 day" in published_date:
#             company_name = job.find('h3' , class_='joblist-comp-name').text.replace(' ', '')
#             skills = job.find('span', class_='srp-skills').text.replace(' ', '')
#             more_info = job.header.h2.a['href']

#             if unfamiliar_skill not in skills:
#                 with open(f'posts/{index}.txt', 'w') as f:
#                     f.write(f'Company Name: {company_name.strip()} \n')
#                     f.write(f'Required Skills: {skills.strip()} \n')
#                     f.write(f'More info: {more_info} \n')
#                 print(f'File saved: {index}')

# if __name__ == '__main__':
#     while True:
#         find_jobs()
#         time_wait = 5
#         print(f'Waiting {time_wait} minutes...')
#         time.sleep(time_wait * 60)