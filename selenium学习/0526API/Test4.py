# 下拉框
from selenium import  webdriver
import os
import time

driver = webdriver.Chrome()
file = "file:///"+os.path.abspath("D:\Bit\测试\selenium2html\\drop_down.html")
driver.get(file)
driver.maximize_window()
time.sleep(3)
# driver.find_element_by_xpath('//*[@id="ShippingMethod"]/option[3]').click()
# driver.find_element_by_css_selector('#ShippingMethod > option:nth-child(3)').click()
options = driver.find_element_by_id("ShippingMethod").find_elements_by_tag_name("option")
# 遍历options找value是10.69的
# for option in options:
#     if option.get_attribute('value') == '10.69':
#         option.click()
options[2].click()  # options数组中的第2个元素
time.sleep(6)
driver.quit()