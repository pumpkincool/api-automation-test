import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from businessHandler.runmethod import runMethod
from businessHandler.dependent_data import dependentData
from businessHandler.get_excel_data import getExcelData
from util import common_util
from util.operation_log import Logger


class RunMainMethod:

    def __init__(self):
        self.run_method = runMethod()
        self.data = getExcelData()
        self.comm_util = common_util.Commonutil()
        self.log = Logger.logger(__name__)

    def go_on_run(self):
        row_count = self.data.get_case_lines()
        pass_count = []
        fail_count = []
        for i in range(1, row_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_url(i)
                method = self.data.get_method(i)
                request_data = self.data.get_json(i)
                header = self.data.get_header(i)
                expect = self.data.get_expect_result(i)
                self.log.debug('预期结果为' + str(expect))
                depend_case = self.data.get_depend_case(i)
                if depend_case is not None:
                    self.depend_data = dependentData(depend_case)
                    depend_res_data = self.depend_data.get_data_for_key(i)
                    depend_key = self.data.get_field_depend(i)
                    request_data[depend_key] = depend_res_data
                res = self.run_method.run_main(method, url, request_data, header)
                self.log.debug('实际结果为' + str(res))
                if self.comm_util.is_contain(expect, res):
                    self.data.write_result(i, 'pass')
                    pass_count.append(i)
                else:

                    self.data.write_result(i, res[0:2000])
                    fail_count.append(i)
            else:
                continue

        self.log.info('通过的case个数为' + str(len(pass_count)))
        self.log.info('失败的case个数为' + str(len(fail_count)))


if __name__ == '__main__':
    run = RunMainMethod()
    run.go_on_run()
