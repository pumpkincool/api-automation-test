class global_var:
    # case_id
    Id = 0
    url = 1
    run = 2
    request_way = 3
    is_header = 4
    header = 5
    case_depend = 6
    data_depend = 7
    field_depend = 8
    data = 9
    expect_result = 10
    actual_result = 11
    env_flag = 'test'


# 获取case_id
def get_caseId():
    return global_var.Id


def get_url():
    return global_var.url


def get_run():
    return global_var.run


def get_request_way():
    return global_var.request_way


def get_is_header():
    return global_var.is_header


def get_header():
    return global_var.header


def get_case_depend():
    return global_var.case_depend


def get_data_depend():
    return global_var.data_depend


def get_field_depend():
    return global_var.field_depend


def get_data():
    return global_var.data


def get_expect_result():
    return global_var.expect_result


def get_actual_result():
    return global_var.actual_result


def get_env_flag():
    return global_var.env_flag


def set_env_flag(env_flag):
    global_var.env_flag = env_flag
