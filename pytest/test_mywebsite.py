from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import sys
from time import sleep
 
def test_lambdatest_todo_app():
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    chrome_driver.get('https://www.1337tester.com/')
    # chrome_driver.maximize_window()
    
    # chrome_driver.find_element("name", "li1").click()
    # chrome_driver.find_element("name", "li2").click()
 
    assert chrome_driver.title == 'Testing is my Profession'
    
    assert chrome_driver.current_url == 'https://www.1337tester.com/'
    
    
    chrome_driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div/div[2]/button").click()
    
    #ic_menu_black_24dp
 
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
    chrome_driver.close()