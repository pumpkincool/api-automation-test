import unittest
from  businessHandler.runmethod import *
from util.operation_json import *


class TestDemo2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("this is setUpClass...")
        TestDemo2.runMethod = runMethod()
    
    def setUp(self):
        print("this is setUp...")
    
    def test_03(self):
        url = 'https://petstore.swagger.io/v2/pet'
        header = {'accept': 'application/json', 'Content-Type': 'application/json'}
        data = operateJson().read_keyword('pet3')
        rst = TestDemo2.runMethod.post_main(url, data, header)
        print('rst: ' + str(rst))
        self.assertEqual(rst['id'], 60, "the response data is error")
    
    def test_04(self):
        url = 'https://www.baidu.com/'
        # rst = TestDemo.runMethod.get_main(url)
        # print(rst)
    
    def tearDown(self):
        print("this is tearDown...")
    
    @classmethod
    def tearDownClass(cls) -> None:
        print("this is tearDownClass...")
