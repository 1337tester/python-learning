import selenium
from selenium.webdriver.common.keys import Keys


driver = selenium.webdriver.Firefox()
driver.get("http://www.python.org")
driver.maximize_window()
assert "Python" in driver.title
elem = driver.find_element_by_id('id-search-field')
print("Passed - elem found")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
elem1 = driver.find_element_by_name('q')
elem2 = driver.find_element_by_css_selector('html.js body div#touchnav-wrapper footer#site-map.main-footer div.main-footer-links div.container ul.sitemap li.tier-1 ul.subnav li.tier-2 a')
assert elem1.is_displayed()
print("Passed - elem1 found")
assert elem2.is_displayed()
print("Passed - elem2 found")
elem1.click()
driver.close()