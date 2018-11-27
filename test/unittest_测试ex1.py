import unittest

class mytestcase(unittest.TestCase):#TestCase 也就是测试用例
    def setUp(self):
        # 每个测试用例执行之前做操作
        self.initdata="hello mooc"

    def test_something(self):
        #测试用例，必须以test开头
        self.assertEqual("hello mooc",self.initdata)

    def tearDown(self):
        # 每个测试用例执行之后释放资源
        pass
if __name__ == '__main__':
    #TestSuite 多个测试用例集合在一起，就是TestSuite
    test_suite = unittest.TestSuite()#创建一个测试集合
    #从类加载到用例集
    cases=unittest.TestLoader().loadTestsFromModule(mytestcase)
    #添加用例到suite
    test_suite.addTests(cases)
    #声明testrunner
    mytestrunner=unittest.TextTestRunner(verbosity=2)
    #执行runner
    mytestrunner.run(test_suite)

