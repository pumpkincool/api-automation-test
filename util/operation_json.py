import json
import jsonpath

key_res = ['init']


class operateJson:

    def __init__(self, filepath=None):
        if filepath:
            self.filename = filepath
        else:
            self.filename = '../datas/request.json'
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.filename) as f:
            data = json.load(f)
            return data

    # 根据关键字获取数据
    def read_keyword(self, key):
        return self.data[key]

    # 反序列化json
    def loads_json(self, data):
        return json.loads(data)

    def __paths(self, data, path='$'):
        if isinstance(data, dict):
            for k, v in data.items():
                tmp = path + '.' + '%s' % k
                yield (tmp, v)
                yield from self.__paths(v, tmp)

        if isinstance(data, list):
            for k, v in enumerate(data):
                tmp = path + '[%d]' % k
                yield (tmp, v)
                yield from self.__paths(v, tmp)

    def find_key_path(self, data, key, v):
        result = []
        for path, value in self.__paths(data):
            if path.endswith('%s' % key) and value is v:
                new_path = path.split('.'+key)[0]
                result.append(new_path)
        return result

    def compare_res(self, expect, actual):
        global key_res
        flag = False
        actual_data = eval(actual)
        for k, v in expect.items():
            if len(key_res) == 1 and key_res[0] == 'init':
                new_key = '$..' + k
                key_word = jsonpath.jsonpath(actual_data, new_key)
                if key_word is not False:
                    for i in key_word:
                        if i == v:
                            key_res = self.find_key_path(actual_data, k, v)
                            flag = True
                        else:
                            return False
                else:
                    return False
            elif len(key_res) != 0:
                for i in key_res:
                    new_key_word = jsonpath.jsonpath(actual_data, i+'.'+k)
                    if new_key_word is False or new_key_word[0] != v:
                        key_res.remove(i)
                        if len(key_res) == 0:
                            return False
                    else:
                        flag = True
        if flag is True:
            return True
        else:
            return False
