import time
import unittest
from selenium import webdriver
import testlearn
from selenium.common.exceptions import NoAlertPresentException

class testCase2(unittest.TestCase):

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
    def test_baidu1(self):
        driver = self.driver
        driver.find_element_by_id("kw").send_keys("杨洋")
        driver.find_element_by_id("su").click()
        time.sleep(3)

    def test_baidu2(self):
        driver = self.driver
        driver.find_element_by_link_text("hao123").click()
        time.sleep(3)

    def is_alert_exist(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException as e:
            return False
        return True
# 入口
    if __name__ == '__main__':
        testlearn.main(verbosity=0)




