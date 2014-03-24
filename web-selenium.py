import selenium
from selenium.webdriver.common.keys import Keys


driver = selenium.webdriver.Firefox()
driver.get("http://www.python.org")
driver.maximize_window()
assert "Python" in driver.title
elem = driver.find_element_by_id('id-search-field')
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
elem1 = driver.find_element_by_name('q')
assert elem1.is_displayed()
elem1.click()
driver.close()