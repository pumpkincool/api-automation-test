import unittest
from pythonRequest.base.runmethod import *
from pythonRequest.util.operation_json import *
from pythonRequest.base.env_info import EnvInfo


class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("this is setUpClass...")
        TestDemo.runMethod = runMethod()
        
    def setUp(self):
        print("this is setUp...")

    def test_01(self):
        host = EnvInfo().get_host()
        print(host)
        url = 'https://petstore.swagger.io/v2/pet'
        header = {'accept': 'application/json', 'Content-Type': 'application/json'}
        data = operateJson().read_keyword('pet3')
        rst = TestDemo.runMethod.post_main(url, data, header)
        print('rst: '+str(rst))
        self.assertEqual(rst['id'], 60, "the response data is error")
        
    def test_02(self):
        url = 'https://www.baidu.com/'
        # rst = TestDemo.runMethod.get_main(url)
        # print(rst)
        
    def tearDown(self):
        print("this is tearDown...")
    
    @classmethod
    def tearDownClass(cls) -> None:
        print("this is tearDownClass...")
