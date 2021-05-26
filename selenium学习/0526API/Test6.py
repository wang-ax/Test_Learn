from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
file = "file:///"+os.path.abspath("D:\Bit\测试\selenium2html\\send.html")
driver.get(file)
driver.maximize_window()
time.sleep(3)
driver.find_element_by_tag_name("input").click()
time.sleep(3)
alert = driver.switch_to.alert
alert.send_keys("java40")
alert.accept()
# alert.dismiss()
time.sleep(6)
driver.quit()