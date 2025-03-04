from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()

@given(u'we have navigated to wikipedia')
def step_impl(context):
    browser.get("http://www.wikipedia.org")


@when(u'we search for light bulb')
def step_impl(context):
    search_element = browser.find_element(By.ID, "searchInput")
    search_element.clear()
    search_element.send_keys("light bulb")
    search_element.send_keys(Keys.RETURN)


@then(u'the resulting page will include Edison')
def step_impl(context):
    assert "Edison" in browser.page_source

@then(u'the resulting page will include Davy')
def step_impl(context):
    assert "Davy" in browser.page_source
