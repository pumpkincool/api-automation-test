import unittest
import sys
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    # env_flag = sys.argv[1]
    # globals(env_flag)
    test_suite = unittest.defaultTestLoader.discover('../y-test', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='BeautifulReport', description='api测试报告', report_dir='../report', theme='theme_default')