from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
file = "file:///"+os.path.abspath("D:/Bit/测试/selenium2html/frame.html")
driver.get(file)
driver.maximize_window()
# 转换层级
driver.switch_to.frame("f1")
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
# 回到默认的页面
driver.switch_to.default_content()

driver.switch_to.frame("f1")
driver.find_element_by_link_text("click").click()
time.sleep(6)
driver.quit()
