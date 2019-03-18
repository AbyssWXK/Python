from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get('https//www.zhihu.com/explore')
logo = browser.find_element_by_id('zhi-top-link-logo')
print(logo)
print(logo.get_attribute('class'))