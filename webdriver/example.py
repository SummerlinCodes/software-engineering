from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.get("http://www.python.org")
assert "Python" in browser.title
assert "Dr. DeLozier is very clever" in browser.page_source
sleep(15)
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
browser.close()
