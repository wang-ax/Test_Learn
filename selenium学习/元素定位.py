# 元素的定位是自动化测试的核心，要想操作一个对象，首先应该识别这个对象。
# webdriver提供了一系列的对象定位的方法，常用的有
# id，name，class name，link text，partial link text ，tag name，xpath，css selector
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("http:www.baidu.com")
# <input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
# ####### 百度输入框的定位方式 #############
# 通过id方式进行定位
browser.find_element_by_id("kw").send_keys("selenium")
# 通过name进行定位
browser.find_element_by_name("wd").send_keys("selenium")
# 通过tag name进行定位
browser.find_element_by_tag_name("input").send_keys("selenium") # 定位不成功，不唯一，有多个input
# 通过class name进行定位
browser.find_element_by_class_name("s_ipt").send_keys("selenium")
# 通过css方式定位
browser.find_element_by_css_selector("#kw").send_keys("selenium")
# 通过xpath方式定位
browser.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")
##########################################
browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()



