import os
import sys
import unittest
import HTMLTestRunner
import time
# HTMLReport测试报告

def createSuite():
    discover = unittest.defaultTestLoader.discover('./testlearn', pattern='test00*.py', top_level_dir=None)
    return discover

if __name__ == '__main__':
    # 获取当前文件所在的文件路径
    curpath = sys.path[0]
    if not os.path.exists("/resultReport"):
        os.mkdir(curpath+"/resultReport")
    #  根据时间能命名
    now = time.strftime("%Y-%m-%d-%H %M %S",time.localtime(time.time()))
    filename = curpath+"/resultReport/"+now+"-"+"resultReport.html"
    # 输出测试结果
    with open(filename,'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试报告",
                                               description=u"用例执行情况",verbosity=2)
        suite = createSuite()
        runner.run(suite)