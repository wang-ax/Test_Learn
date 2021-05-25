from selenium import webdriver
import time

driver = webdriver.Chrome() # 获得浏览器的驱动
url = "https://www.baidu.com"
driver.get(url)
# 用id来定位百度搜索框,如果元素有id属性就用id来定位
# id是全局唯一的
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()

# 用link text来定位
# driver.find_element_by_link_text("新闻").click()

# 用partial link text 来定位
# driver.find_element_by_partial_link_text("123").click()

# 用tag name 来进行定位
# 需要全局唯一才能够进行定位

# 用Xpath来进行定位
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys("selenium")
# driver.find_element_by_xpath('//*[@id="su"]').click()

# 用css selector来进行定位
# driver.find_element_by_css_selector('#kw').send_keys("李现")
# driver.find_element_by_css_selector('#su').click()
# time.sleep(3)
# 将原本输入框中的内容进行清除
# driver.find_element_by_css_selector("#kw").clear()
# time.sleep(3)
# 重新进行搜索
# driver.find_element_by_css_selector('#kw').send_keys("人生若只如初见")
# 提交表单
# driver.find_element_by_id('su').submit()
# driver.find_element_by_id('su').click()

# text 获取文本内容
text = driver.find_element_by_id("s-top-left").text
print(text)
time.sleep(5) # 固定等待
driver.quit()
