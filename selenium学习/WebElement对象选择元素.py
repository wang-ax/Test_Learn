from selenium import webdriver
import time
wd = webdriver.Chrome()
wd.implicitly_wait(10) # 每隔半秒钟找一次
wd.get("https://www.baidu.com")
element = wd.find_element_by_id("kw")
element.send_keys("百越黑羽\n")
# 必须等待几秒钟，再进行搜索
# time.sleep(5)
element = wd.find_element_by_id('2')
print(element.text)