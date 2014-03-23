import selenium
from selenium.webdriver.common.keys import Keys


driver = selenium.webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_xpath('//*[@id="id-search-field"]')
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
elem1 = driver.find_element_by_xpath('/html/body/div/div[2]/div/section/form/ul/li/h3/a')
assert elem1.is_displayed()
elem1.click()
driver.close()