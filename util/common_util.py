from util.operation_json import operateJson


class Commonutil:

    def __init__(self):
        self.opera_json = operateJson()

    def is_contain(self, expect, actual):
        flag = False
        if expect is True:
            return True
        if expect is None or expect is False:
            return False
        if type(expect) is str:
            str_res = expect.split(';')
            for i in str_res:
                if i in actual:
                    flag = True
                else:
                    flag = False
            return flag
        if type(expect) is list or type(expect) is tuple:
            if len(expect) == 0:
                return False
            for i in expect:
                if self.opera_json.compare_res(i, actual):
                    flag = True
                    continue
                else:
                    return False
            return flag
