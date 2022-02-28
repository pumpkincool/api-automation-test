from util.operation_excel import operateExcel
from util.operation_json import operateJson
from util.operation_mysql import operationMysql
from data import data_config_excel
from base.env_info import EnvInfo


class getData:

    def __init__(self):
        self.opera_excel = operateExcel()
        self.get_env = EnvInfo()
        self.opera_mysql = operationMysql(self.get_env.get_username(), self.get_env.get_password(), self.get_env.get_host(), self.get_env.get_db())

    # 获取case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 判断是否执行
    def get_is_run(self, row):
        col = data_config_excel.get_run()
        is_run = self.opera_excel.get_cell_value(row, col)
        if is_run.lower() == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 获取header
    def get_header(self, row):
        is_herder_col = data_config_excel.get_is_header()
        is_header = self.opera_excel.get_cell_value(row, is_herder_col)
        header_col = data_config_excel.get_header()
        header = self.opera_excel.get_cell_value(row, header_col)
        if is_header.lower() == 'yes' and header != '':
            return eval(header)
        else:
            return None

    # 获取请求方式
    def get_method(self, row):
        col = data_config_excel.get_request_way()
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    # 获取url
    def get_url(self, row):
        col = data_config_excel.get_url()
        url = self.opera_excel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = data_config_excel.get_data()
        request_data = self.opera_excel.get_cell_value(row, col)
        return request_data

    # 通过获取关键字拿到json数据
    def get_json(self, row):
        oper_json = operateJson()
        key_word = self.get_request_data(row)
        if key_word == '':
            return None
        else:
            request_data = oper_json.read_keyword(self.get_request_data(row))
            return request_data

    # 获取预期结果
    def get_expect_result(self, row):
        col = data_config_excel.get_expect_result()
        expect_result = str(self.opera_excel.get_cell_value(row, col))
        if expect_result == '':
            return False
        elif expect_result.lower().startswith("sql"):
            expect_result_ori = self.operate_sql_data(expect_result)
            return self.opera_mysql.querydball(expect_result_ori)
        else:
            return expect_result

    def operate_sql_data(self, sql_data):
        expect_data_sql = sql_data.split(':', maxsplit=1)[1]
        return expect_data_sql

    def write_result(self, row, value):
        col = data_config_excel.get_actual_result()
        self.opera_excel.write_value(row, col, value)

    def get_depend_case(self, row):
        col = data_config_excel.get_case_depend()
        depend_case = self.opera_excel.get_cell_value(row, col)
        if depend_case == '':
            return None
        else:
            return depend_case

    def get_depend_key(self, row):
        col = data_config_excel.get_data_depend()
        depend_key = self.opera_excel.get_cell_value(row, col)
        if depend_key == '':
            return None
        else:
            return depend_key

    def get_field_depend(self, row):
        col = data_config_excel.get_field_depend()
        filed_depend = self.opera_excel.get_cell_value(row, col)
        if filed_depend == '':
            return None
        else:
            return filed_depend

