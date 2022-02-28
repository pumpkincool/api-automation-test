import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from base.runmethod import runMethod
from data import dependent_data
from data import get_data
from util import common_util
from util.log import Logger


class RunMainMethod:

    def __init__(self):
        self.run_method = runMethod()
        self.data = get_data.getData()
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
                self.log.debug(expect)
                depend_case = self.data.get_depend_case(i)
                if depend_case is not None:
                    self.depend_data = dependent_data.dependentData(depend_case)
                    depend_res_data = self.depend_data.get_data_for_key(i)
                    depend_key = self.data.get_field_depend(i)
                    request_data[depend_key] = depend_res_data
                res = self.run_method.run_main(method, url, request_data, header)
                self.log.debug(res)
                if self.comm_util.is_contain(expect, res):
                    self.data.write_result(i, 'pass')
                    pass_count.append(i)
                else:

                    self.data.write_result(i, res[0:2000])
                    fail_count.append(i)
            else:
                continue

        print('通过的case个数为' + str(len(pass_count)))
        print('失败的case个数为' + str(len(fail_count)))


if __name__ == '__main__':
    run = RunMainMethod()
    run.go_on_run()
