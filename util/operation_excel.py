import xlrd
from xlutils.copy import copy


class operateExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../data_config/case.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheet内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        table = data.sheets()[self.sheet_id]
        return table

    # 获取单元格行数
    def get_lines(self):
        return self.data.nrows

    # 获取单元格内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # excel写入数据
    def write_value(self, row, col, value):
        workbook = xlrd.open_workbook(self.file_name)
        new_workbook = copy(workbook)
        sheet_data = new_workbook.get_sheet(0)
        sheet_data.write(row, col)
        sheet_data.write(row, col, value)
        new_workbook.save(self.file_name)

    # 根据caseId获取行号
    def get_row_num(self, case_id):
        num = -1
        cols_data = self.get_col_data(0)
        for col_data in cols_data:
            num = num + 1
            if col_data == case_id:
                return num

    # 根据case_Id获取行内容
    def get_row_data_by_caseId(self, case_id):
        row_num = self.get_row_num(case_id)
        return self.get_row_data(row_num)

    # 根据行号获取行内容
    def get_row_data(self, row):
        return self.data.row_values(row)

    # 根据列号获取列内容
    def get_col_data(self, col):
        return self.data.col_values(col)


if __name__ == '__main__':
    oper = operateExcel()
    oper.get_row_data_by_caseId('case2')
