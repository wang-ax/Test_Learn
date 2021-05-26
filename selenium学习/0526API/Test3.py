from selenium import  webdriver
import  time
import os
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
file = "file:///"+os.path.abspath("D:\Bit\测试\selenium2html\\level_locate.html")
driver.get(file)
driver.maximize_window()
driver.find_element_by_link_text("Link1").click()
# 定位下拉列表特性的元素
element = driver.find_element_by_id("dropdown1").find_element_by_link_text("Another action")
# 把鼠标放到这个元素上，让这个元素高亮显示
ActionChains(driver).move_to_element(element).perform()

time.sleep(6)
driver.quit()