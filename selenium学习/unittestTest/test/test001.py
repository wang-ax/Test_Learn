import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException

class testCase1(unittest.TestCase):
    # 测试固件
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.baidu.com"
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    # 测试用例，必须要以test开头，以test_开头,会默认运行
    def test_baidu1(self):
        driver = self.driver
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(6)

    def test_baidu2(self):
        driver = self.driver
        driver.find_element_by_link_text("新闻").click()
        time.sleep(6)
    # 判断alert是否存在，可删除
    def is_alert_exist(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException as e:
            return False
        return True
    if __name__ == "__main__":
        # 执行测试用例
        unittest.main(verbosity=0)
