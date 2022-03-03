import unittest
from businessHandler.runmethod import *
from util.operation_json import *
from businessHandler.get_env_info import getEnvInfo
from util.operation_log import Logger


class BaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 基础类实例化
        BaseDemo.logger = Logger()
        BaseDemo.logger.info("this is setUpClass...")
        BaseDemo.runMethod = runMethod()
        BaseDemo.env = getEnvInfo()
        BaseDemo.operateJson = operateJson()
        
    def setUp(self):
        BaseDemo.logger.info("this is setUp...")
        # 登录等业务相关且通用操作, 如：登录
        BaseDemo.logger.info("this is login...")
        
    def tearDown(self):
        BaseDemo.logger.info("this is tearDown...")
        # 登录等业务相关且通用操作, 如：登出
        BaseDemo.logger.info("this is logout...")
        BaseDemo.logger.warning("this testcase done...")
    
    @classmethod
    def tearDownClass(cls) -> None:
        BaseDemo.logger.info("this is tearDownClass...")
        BaseDemo.logger.info("this class done...\n")
