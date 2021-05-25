# 键盘事件
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys  # 需要引入Keys包
driver = webdriver.Chrome()
driver.get('http://127.0.0.1:88/zentao/user-login-L3plbnRhby8=.html')

driver.maximize_window()  # 将浏览器最大化
# 登录
driver.find_element_by_id("account").send_keys("admin")
# 模拟Tab键
driver.find_element_by_id("account").send_keys(Keys.TAB)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("wax123456789")  # 让代码更加简洁
# 用Enter键直接登录
password.send_keys(Keys.ENTER)  # 调用的Enter键

# driver.find_element_by_id("submit").click() #点击登录按钮进行登录

time.sleep(6)
driver.quit()
