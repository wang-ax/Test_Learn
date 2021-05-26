import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException

class testCase2(unittest.TestCase):
    # 测试固件
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.baidu.com"
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    # 以test_开头,会默认运行
    def test_baidu1(self):
        driver = self.driver
        driver.find_element_by_id("kw").send_keys("李现")
        driver.find_element_by_id("su").click()
        time.sleep(6)

    def test_baidu2(self):
        driver = self.driver
        driver.find_element_by_link_text("hao123").click()
        time.sleep(6)

    def is_alert_exist(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException as e:
            return False
        return True
    if __name__ == "__main__":
        unittest.main(verbosity=0)
