import HTMLTestRunner
import unittest
import run_main


class run_unittest(unittest.TestCase):
    def setUp(self):
        self.run = run_main.RunMainMethod()

    def test_case_unittest(self):
        row_count = self.run.data.get_case_lines()
        for i in range(1, row_count):
            url = self.run.data.get_url(i)
            method = self.run.data.get_method(i)
            is_run = self.run.data.get_is_run(i)
            data = self.run.data.get_json(i)
            header = self.run.data.get_header(i)
            expect = self.run.data.get_expect_result(i)
            if is_run:
                res = self.run.run_method.run_main(method, url, data, header)
                try:
                    self.assertIn(expect, res, '测试失败')
                except AssertionError:
                    self.run.data.write_result(i, 'failure')
                else:
                    self.run.data.write_result(i, 'pass')
            else:
                continue


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(run_unittest('test_case_unittest'))
    # unittest.TextTestRunner().run(suite)
    # 以下方法使用HTMLTestRunner进行执行
    fp = open('../report/htmlReport.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='api测试报告', description='测试情况')
    runner.run(suite)
