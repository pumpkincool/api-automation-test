import configparser


class global_excel:
    config = configparser.ConfigParser()
    config.read('../configs/excel_config.ini')
    flag = 'excel'


def get_caseId():
    return global_excel.config.getint(global_excel.flag, 'id')


def get_url():
    return global_excel.config.getint(global_excel.flag, 'url')


def get_run():
    return global_excel.config.getint(global_excel.flag, 'run')


def get_request_way():
    return global_excel.config.getint(global_excel.flag, 'request_way')


def get_is_header():
    return global_excel.config.getint(global_excel.flag, 'is_header')


def get_header():
    return global_excel.config.getint(global_excel.flag, 'header')


def get_case_depend():
    return global_excel.config.getint(global_excel.flag, 'case_depend')


def get_data_depend():
    return global_excel.config.getint(global_excel.flag, 'data_depend')


def get_field_depend():
    return global_excel.config.getint(global_excel.flag, 'field_depend')


def get_data():
    return global_excel.config.getint(global_excel.flag, 'data')


def get_expect_result():
    return global_excel.config.getint(global_excel.flag, 'expect_result')


def get_actual_result():
    return global_excel.config.getint(global_excel.flag, 'actual_result')


def get_excel_location():
    return global_excel.config.get(global_excel.flag, 'excel_location')


def get_sheet_id():
    return global_excel.config.get(global_excel.flag, 'sheet_id')


def get_json_location():
    return global_excel.config.get(global_excel.flag, 'json_location')
