from testlearn import test001
import test002
import unittest
def createSuite():
    # 组织测试套件
    suite = unittest.TestSuite()

    # 1.addTest() 将每个测试方法依次添加到测试套件中
    # suite.addTest(test001.testCase1("test_baidu1"))
    # suite.addTest(test001.testCase1("test_baidu2"))
    # suite.addTest(test002.testCase2("test_baidu1"))
    # suite.addTest(test002.testCase2("test_baidu2"))
    # return suite

    # 2.makeSuite
    # suite.addTest(unittest.makeSuite(test001.testCase1))
    # suite.addTest(unittest.makeSuite(test002.testCase2))
    # return suite

    # TestLoader
    suite1 = unittest.TestLoader().loadTestsFromTestCase(test001.testCase1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(test002.testCase2)
    suite.addTests([suite1,suite2]) # 将两个小的测试套件添加到测试套件suite中
    return suite

    # 直接添加文件
    # discover = unittest.defaultTestLoader.discover('../testlearn',pattern='test00*.py',top_level_dir=None)
    # print(discover)
    # return discover


# 入口
if __name__ == '__main__':
    suite = createSuite()
    # 执行
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)# 执行这个测试套件


