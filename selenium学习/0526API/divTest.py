from selenium import webdriver
import os
import time
# 层级关系
driver = webdriver.Chrome()
file = "file:///"+os.path.abspath("D:\Bit\测试\selenium2html\\modal.html")
driver.get(file)
driver.maximize_window()
time.sleep(3)

driver.find_element_by_link_text("Click").click()
time.sleep(3)
div0 = driver.find_element_by_class_name("modal-body")
div0.find_element_by_id("click").click()

div1 = driver.find_element_by_class_name("modal-footer")
# div1.find_element_by_name("btn").click()
buttons = div1.find_elements_by_tag_name("button")  # 在div1中找到button一组元素
buttons[0].click  # 点击close

time.sleep(5)
driver.quit()