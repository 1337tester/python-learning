from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import requests


cookie_banner_css = '#cookieChoiceInfo > div > span.cookie-choices-text'
cookie_dismiss_xpath = '//*[@id="cookieChoiceDismiss"]'
search_button_xpath = '/html/body/div[1]/header/div/div/div[1]/div[2]/button/div[1]'
website_url = 'https://www.1336tester.com/'
accepted_encodings = ('gzip', 'br', 'deflate', 'zstd')

timeout = 10

@pytest.fixture(scope="module")
def website_response():
    return requests.get(website_url)


def test_website_on(website_response):
    assert website_response.status_code == 200

def test_website_encoding(website_response):
    assert website_response.headers['content-encoding'] in accepted_encodings

def test_lambdatest_todo_app():
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        chrome_driver.get('https://www.1337tester.com/')
        chrome_driver.maximize_window()
        # chrome_driver.find_element("name", "li1").click()

        wait = WebDriverWait(chrome_driver, timeout)

        assert chrome_driver.title == 'Testing is my Profession'

        assert chrome_driver.current_url == 'https://www.1337tester.com/'

        cookies = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, cookie_banner_css)))

        assert cookies.is_displayed() == True

        wait.until(EC.element_to_be_clickable((By.XPATH, cookie_dismiss_xpath))).click()
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, cookie_banner_css)))

        wait.until(EC.element_to_be_clickable((By.XPATH, search_button_xpath))).click()

    # except NoSuchElementException:
    #     print('aaa')

    finally:
        chrome_driver.quit()
