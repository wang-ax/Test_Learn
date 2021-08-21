import time
import unittest
from selenium import webdriver
import testlearn
from selenium.common.exceptions import NoAlertPresentException
import os,sys
# test1类继承TestCase
class testCase1(unittest.TestCase):
    # 测试固件:setUp() 和tearDown()
    # self代表这个类的实例
    # 在执行测试方法的时候，测试固件每一次都会执行
    def setUp(self):
        # 初始化操作
        self.driver = webdriver.Chrome()
        self.url = "https://www.baidu.com/"
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)
    def tearDown(self):
        # 清理工作
        self.driver.quit()

    # 除了测试固件之外，所以以test_开头的方法是默认运行的
    @unittest.skip("skipping")
    def test_baidu1(self):
        driver = self.driver
        driver.find_element_by_id("kw").send_keys("张")
        driver.find_element_by_id("su").click()
        time.sleep(3)

# 错误截图
    def test_baidu2(self):
        driver = self.driver
        # 判断是不是打开百度页面
        try:
            self.assertEqual(driver.title,"百度，你就知道",msg= "没有打开百度搜索页面")
        except:
            self.save_error_image(driver,"baidu.png")
        #driver.find_element_by_link_text("新闻").click()
        time.sleep(3)

    def save_error_image(self,driver,name):
        if not os.path.exists("./errorImage"):
            os.makedirs("./errorImage")
        now = time.strftime("%Y%m%d-%H%M%S",time.localtime(time.time()))
        self.driver.get_screenshot_as_file('./errorImage/'+now+'-'+name)


    def is_alert_exist(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException as e:
            return False
        return True
# 入口
    if __name__ == '__main__':
        testlearn.main(verbosity=0)




