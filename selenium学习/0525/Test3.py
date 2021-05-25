from  selenium import  webdriver
import  time

driver = webdriver.Chrome()
url = "http://127.0.0.1:88/zentao/user-login-L3plbnRhby8=.html"
driver.get(url)
# 用name来定位
# driver.find_element_by_name("account").send_keys("admin")
# driver.find_element_by_name("password").send_keys("wax123456789")
# driver.find_element_by_id("submit").click()

time.sleep(5)
driver.quit()
