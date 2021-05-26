from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
# 拿到文件的绝对路径
file = "file:///"+os.path.abspath("D:\Bit\测试\selenium2html\checkbox.html")
driver.get(file)
driver.maximize_window()  # 浏览器放大
# 定位一组元素的方法
# 1.
# driver.find_element_by_id("c1").click()
# driver.find_element_by_id("c2").click()
# driver.find_element_by_id("c3").click()
# 2.
inputs = driver.find_elements_by_tag_name("input")
# 从一组元素中找出 type=“checkbox”
for input in inputs:
    if input.get_attribute('type')=='checkbox':
        input.click()

time.sleep(3)
driver.quit()

