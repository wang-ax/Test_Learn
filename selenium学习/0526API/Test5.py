from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
file = "file:///"+os.path.abspath("D:\Bit\测试\selenium2html\\alert.html")
driver.get(file)
driver.maximize_window()
time.sleep(3)
driver.find_element_by_id("tooltip").click()
time.sleep(5)
# 关闭弹窗
# 得到了操作弹框的句柄
alert = driver.switch_to.alert
alert.accept()

time.sleep(5)
driver.quit()