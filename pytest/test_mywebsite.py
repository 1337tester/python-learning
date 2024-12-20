from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from time import sleep

cookie_banner_css = '#cookieChoiceInfo > div > span.cookie-choices-text'
cookie_dismiss_xpath = '//*[@id="cookieChoiceDismiss"]'
search_button_xpath = '/html/body/div[1]/header/div/div/div[1]/div[2]/button/div[1]'


def test_lambdatest_todo_app():
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    
    try:
        chrome_driver.get('https://www.1337tester.com/')
        chrome_driver.maximize_window()
        # chrome_driver.find_element("name", "li1").click()
    
        assert chrome_driver.title == 'Testing is my Profession'
        
        assert chrome_driver.current_url == 'https://www.1337tester.com/'
        
        cookies = chrome_driver.find_element(By.CSS_SELECTOR, cookie_banner_css)
        
        assert cookies.is_displayed() == True
        
        sleep(1)
        chrome_driver.find_element(By.XPATH, cookie_dismiss_xpath).click()
        sleep(1)
        
        chrome_driver.find_element(By.XPATH, search_button_xpath).click()
        sleep(2)
        
    # except NoSuchElementException:
    #     print('aaa')
        
    finally:
        chrome_driver.close()
    

    # sample_text = "Happy Testing at LambdaTest"
    # email_text_field = chrome_driver.find_element("id", "sampletodotext")
    # email_text_field.send_keys(sample_text)
    # sleep(2) 
    # chrome_driver.find_element("id", "addbutton").click()
    # sleep(2) 
    # output_str = chrome_driver.find_element("xpath", "/html/body/div/div/div/ul/li[6]/span").text
    # assert output_str == "Happy Testing at LambdaTest"
    # sys.stderr.write(output_str)    
    # sleep(1)
