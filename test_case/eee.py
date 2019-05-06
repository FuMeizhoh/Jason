from selenium import webdriver
from common.base import Base


driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
baidu = Base(driver)

loc = ('link text','设置')
baidu.move_to_element(loc)



