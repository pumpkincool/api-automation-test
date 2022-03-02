from util.operation_excel import operateExcel
from util.operation_json import operateJson
from businessHandler.runmethod import runMethod
from businessHandler.get_excel_data import getExcelData


class dependentData:

    def __init__(self, case_id):
        self.oper_excel = operateExcel()
        self.oper_json = operateJson()
        self.data = getExcelData()
        self.case_id = case_id

    def get_case_line_data(self):
        row_data = self.oper_excel.get_row_data_by_caseId(self.case_id)
        return row_data

    # 执行依赖的case
    def run_dependent(self):
        run_method = runMethod()
        row_num = self.oper_excel.get_row_num(self.case_id)
        request_data = self.data.get_json(row_num)
        header = self.data.get_header(row_num)
        method = self.data.get_method(row_num)
        url = self.data.get_url(row_num)
        res = run_method.run_main(method, url, request_data, header)
        return res

    def get_data_for_key(self, row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        d = self.oper_json.loads_json(response_data)
        return d[depend_data]
