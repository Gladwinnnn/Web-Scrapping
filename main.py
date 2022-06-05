# import os
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys

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

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from bs4 import BeautifulSoup
import requests
import time

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

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text

        if "1 day" in published_date:
            company_name = job.find('h3' , class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Required Skills: {skills.strip()} \n')
                    f.write(f'More info: {more_info} \n')
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 5
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)