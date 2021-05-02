from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from selenium.webdriver.support import select
from selenium.common import exceptions
import unittest,time,re
class Baidu(unittest.TestCase):
    def SetUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors=[]
        self.accept_next_alert = True

    #百度搜索用例
    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.quit()
    # 百度设置用例
    def test_baidu_set(self):
        driver = self.driver
        # 进入搜索设置页
        driver.get(self.base_url+'gaoji/preferences.html')
        m=driver.find_element_by_name('NR')
        #设置每页搜索结果为100条，先找到ID=NR的标签，再找到ID=NR标签下的option标签value值等于100的选择按钮
        m.find_element_by_xpath("//option[@value='100']").click()
        time.sleep(2)
        #保存设置的信息
        driver.find_element_by_xpath("//input[@value='保存设置']").click()
        time.sleep(2)
        n=driver.switch_to_alert()
        n.accept()
    def tearDown(self):
        self.driver.quit()
        self.assertEquals([],self.verificationErrors)

if __name__ == '__main__':
    unittest.main() #执行测试用例

