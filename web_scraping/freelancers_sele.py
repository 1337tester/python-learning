from selenium import webdriver
# from selenium.webdriver import Keys #ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from time import sleep

separator = 40*"*"

def jobs_info(job):
    job_details = [text for text in job.stripped_strings]
    
    # deleting premium content
    del job_details[1]
    del job_details[1]
    del job_details[-1]
    del job_details[-1]

    print(*job_details, sep = "\n")
    print(separator)
    
def check_pagination(pagination):
    pages = pagination.text.split(' ')
    print(pages[1], pages[2], pages[3])
    # print(pages)



# cookie_banner_css = '#cookieChoiceInfo > div > span.cookie-choices-text'
# cookie_dismiss_xpath = '//*[@id="cookieChoiceDismiss"]'
# search_button_xpath = '/html/body/div[1]/header/div/div/div[1]/div[2]/button/div[1]'
freetext_css = '#__search_freetext'
city_css = '#__search_city'
city_selectfirst_css = '.place-autocompleter > a:nth-child(1)'
city_distance_css = 'div.col-sm-2:nth-child(3) > div:nth-child(2) > button:nth-child(1)'
city_distance_100km_css = 'div.col-sm-2:nth-child(3) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(5) > a:nth-child(1)'
search_css = '#search_simple'
job_info_css = '.project-list > div'
pagination_css = '[id=pagination] > p'
next_css = '[aria-label=Next]'

chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    chrome_driver.get('https://www.freelance.de/Projekte/K/IT-Entwicklung-Projekte/')
    chrome_driver.maximize_window()
            
    input_freetext = chrome_driver.find_element(By.CSS_SELECTOR, freetext_css)
    input_freetext.send_keys("test")
    
    input_city = chrome_driver.find_element(By.CSS_SELECTOR, city_css)
    input_city.click()
    sleep(1)
    input_city.send_keys("Zürich")

    # select first choice
    WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, city_selectfirst_css)))
    city_dropdown = chrome_driver.find_element(By.CSS_SELECTOR, city_selectfirst_css)
    city_dropdown.click()
    
    # select radius from city
    chrome_driver.find_element(By.CSS_SELECTOR, city_distance_css).click()
    chrome_driver.find_element(By.CSS_SELECTOR, city_distance_100km_css).click() 
    sleep(1)
    
    # submit search
    chrome_driver.find_element(By.CSS_SELECTOR, search_css).click()    
    
    WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, job_info_css)))
    jobs = chrome_driver.find_elements(By.CSS_SELECTOR, job_info_css)
    for job in jobs:
        soup_job = BeautifulSoup(job.get_attribute('innerHTML'), 'html.parser')
        jobs_info(soup_job)

    pagination = chrome_driver.find_element(By.CSS_SELECTOR, pagination_css)
    check_pagination(pagination)
    
    
    
except NoSuchElementException:
    print('Element not found')
    
finally:
    chrome_driver.close()
