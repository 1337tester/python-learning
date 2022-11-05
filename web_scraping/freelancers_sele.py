from selenium import webdriver
from selenium.webdriver import Keys #ActionChains
# from  selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from time import sleep

# cookie_banner_css = '#cookieChoiceInfo > div > span.cookie-choices-text'
# cookie_dismiss_xpath = '//*[@id="cookieChoiceDismiss"]'
# search_button_xpath = '/html/body/div[1]/header/div/div/div[1]/div[2]/button/div[1]'
freetext_css = '#__search_freetext'
city_css = '#__search_city'
city_selectfirst_css = '.place-autocompleter > a:nth-child(1)'
city_distance_css = 'div.col-sm-2:nth-child(3) > div:nth-child(2) > button:nth-child(1)'
city_distance_100km_css = 'div.col-sm-2:nth-child(3) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(5) > a:nth-child(1)'
search_css = '#search_simple'


chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    chrome_driver.get('https://www.freelance.de/Projekte/K/IT-Entwicklung-Projekte/')
    chrome_driver.maximize_window()
    
    
    # chrome_driver.find_element("name", "li1").click()
    # assert chrome_driver.title == 'Testing is my Profession'
        
    input_freetext = chrome_driver.find_element(By.CSS_SELECTOR, freetext_css)
    input_freetext.send_keys("test")
    
    input_city = chrome_driver.find_element(By.CSS_SELECTOR, city_css)
    input_city.click()
    sleep(1)
    input_city.send_keys("Zürich")
    sleep(1)

    # select first choice
    city_dropdown = chrome_driver.find_element(By.CSS_SELECTOR, city_selectfirst_css)
    city_dropdown.click()
    
    # select radius from city
    chrome_driver.find_element(By.CSS_SELECTOR, city_distance_css).click()
    chrome_driver.find_element(By.CSS_SELECTOR, city_distance_100km_css).click() 
        
    sleep(1)
    
    chrome_driver.find_element(By.CSS_SELECTOR, search_css).click()    
    
    # chrome_driver.find_element(By.XPATH, search_button_xpath).click()
    sleep(10)
    
except NoSuchElementException:
    print('aaa')
    
finally:
    chrome_driver.close()
