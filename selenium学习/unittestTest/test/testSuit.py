import unittest
# 导入test001和test002
from test import test001
from test import test002

# 在unittest中用TestSuite类来构建测试套件
# 要同时执行我们已经写好的test001.py和test002.py两个文件，将这两个文件中的测试方法都执行

# 手工添加案例到套件
def createSuite():
    suite = unittest.TestSuite()
# addTest：将测试用例加入到测试容器（套件）中
    # suite.addTest(test001.testCase1("test_baidu1"))
    # suite.addTest(test001.testCase1("test_baidu2"))
    # suite.addTest(test002.testCase2("test_baidu1"))
    # suite.addTest(test002.testCase2("test_baidu2"))

# makeSuite：可以实现把测试用例类内的所有的测试case组成的测试套件TestSuite,只需要把测试类的名称传入即可
    # suite.addTest(unittest.makeSuite(test001.testCase1))
    # suite.addTest(unittest.makeSuite(test002.testCase2))
    # return suite

# TestLoader:用于创建类和模块的测试套件，一般情况下使用TestLoader().loadTestsFromTestCase(TestClass)来加载测试类
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(test001.testCase1)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(test002.testCase2)
    # suite.addTests([suite1,suite2])
    # return suite

# discover:通过递归的方式到其子目录中从指定的目录开始，找到所有测试魔魁啊把那个返回一个包含它们对象的TestSuite
    # 然后进行加载与模式匹配唯一的测试文件
    discover = unittest.defaultTestLoader.discover('../test',pattern='test00*.py',top_level_dir=None)
    print(discover)
    return discover

if __name__ == '__main__':
    suite = createSuite()
    # 执行测试
    runner = unittest.TextTestRunner(verbosity=1)  # 打印出详细信息
    runner.run(suite)
