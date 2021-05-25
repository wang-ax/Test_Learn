from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
url = "http://www.baidu.com"
driver.get(url)

# 浏览器的最大化
driver.maximize_window()

driver.find_element_by_id("kw").send_keys("肖战")
driver.find_element_by_id("su").submit()
# 需要等待页面加载出来之后再执行后面的操作
time.sleep(5) # 固定等待
# 智能等待
# driver.implicitly_wait(10) # 如果页面的元素加载出来，就会进行后续的操作
# driver.find_element_by_link_text("肖战(中国内地男演员、歌手) - 百度百科").click()

# 打印title和url
print(driver.title)
print(driver.current_url)

# 设置浏览器的宽和高
# driver.set_window_size(500,800)

# 浏览器的后退
# driver.back()
# time.sleep(3)
# # 浏览器的前进
# driver.forward()

# 浏览器控制条的下拉，将滚动条拉到页面的底部
# 使用JavaScript
js1 = "var q=document.documentElement.scrollTop =10000"
driver.execute_script(js1)
time.sleep(5)
# 将滚动条移动到页面的顶部
js2 = "var q=document.documentElement.scrollTop =0"
driver.execute_script(js2)


# 键盘组合键的使用
kw = driver.find_element_by_id("kw")
kw.send_keys(Keys.CONTROL,'a')
kw.send_keys(Keys.CONTROL,'x')
time.sleep(6)
kw.send_keys("杨紫")
su = driver.find_element_by_id("su")
# 鼠标事件
# 右击元素
ActionChains(driver).context_click(su).perform()
time.sleep(6)
# 双击元素
ActionChains(driver).double_click(su).perform()
time.sleep(6)

driver.quit()
