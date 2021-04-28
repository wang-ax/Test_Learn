from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium\n")
# 在输入框中填入selenium,如果输入\n表示在输入之后按回车直接进行搜索，不需要再点击百度一下
# driver.find_element_by_id('su').click()# 点击百度一下


# driver.find_element_by_name("wd").send_keys("selenium")
time.sleep(5)
driver.close()