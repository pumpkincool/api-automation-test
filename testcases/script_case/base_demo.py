import unittest
from businessHandler.runmethod import *
from util.operation_json import *
from businessHandler.get_env_info import getEnvInfo
from util.log_util import LogUtil


class BaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 基础类实例化
        BaseDemo.log = LogUtil()
        BaseDemo.log.error_log("this is setUpClass...")
        BaseDemo.runMethod = runMethod()
        BaseDemo.env = getEnvInfo()
        BaseDemo.operateJson = operateJson()
    
    def setUp(self):
        BaseDemo.log.warning_log("this is setUp...")
        # 用例执行前的业务相关且通用操作, 如：登录
        BaseDemo.log.warning_log("this is login...")
        
    def tearDown(self):
        BaseDemo.log.warning_log("this is tearDown...")
        # 用例执行后的相关且通用操作, 如：登出
        BaseDemo.log.warning_log("this is logout...")
    
    @classmethod
    def tearDownClass(cls) -> None:
        BaseDemo.log.error_log("this is tearDownClass...\n")
