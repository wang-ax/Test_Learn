# 要使用selenium中的webdriver里的函数，首先要将包导进来
from selenium import webdriver
import time
# 选择需要操控哪个浏览器
browser = webdriver.Chrome("D:\chromedriver.exe")
time.sleep(3)
browser.get("https://www.baidu.com")
time.sleep(3)
# 一个控件有若干个属性id，name等等，百度输入框的id叫kw，我们要搜索的是selenium
browser.find_element_by_id("kw").send_keys("selenium")
time.sleep(3)
# 搜索的按钮的id叫su，我需要点击一个按钮
browser.find_element_by_id("su").click()
# 退出并关闭每一个相关的驱动程序
browser.quit()
# quit方法不仅会关闭窗口，还会彻底的退出webdriver，会更好的释放资源
# 关闭当前的浏览器窗口，
# browser.close()

