# 上传文件,直接使用send_keys上传文件
from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
file = "file:///"+os.path.abspath("D:\Bit\测试\selenium2html\\upload.html")
driver.get(file)
driver.maximize_window()
time.sleep(3)

driver.find_element_by_tag_name('input').send_keys("D:\简历\\王奥雪-测试开发实习生-18292940472.pdf")
time.sleep(5)
driver.quit()