from selenium import webdriver
import time
driver = webdriver.Chrome()
time.sleep(3)
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("李现\n")  # 在输入数据之后直接回车
# driver.find_element_by_id("su").click()  # 点击百度一下
time.sleep(5)
driver.quit()


