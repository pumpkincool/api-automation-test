import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from BeautifulReport import BeautifulReport
from businessHandler.env_flag import *
import unittest


class RunPy:
    def __init__(self):
        if len(sys.argv) > 1:
            set_env_flag(sys.argv[1])
        else:
            set_env_flag('test')
            
    def run_py(self):
        test_suite = unittest.defaultTestLoader.discover('../testcases', pattern='test*.py')
        result = BeautifulReport(test_suite)
        result.report(filename='BeautifulReport', description='api测试报告', report_dir='../reports', theme='theme_default')


if __name__ == '__main__':
    RunPy().run_py()
