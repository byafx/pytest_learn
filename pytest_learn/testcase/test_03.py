class Test03:

    def setup_class(self):
        print('在每个类执行前的初始化工作')

    def setup(self):
        print('\n在执行测试用例前初始化的代码')

    def test_03_01(self):
        print('test03_01')

    def test_03_02(self):
        print('test03_02')

    def teardown(self):
        print('\n在执行测试用例之后的扫尾代码')

    def teardown_class(self):
        print('在每个类执行后的扫尾工作')
