import json
import requests


class runMethod:

    def post_main(self, url, data, header=None):
        if header != '':
            res = requests.post(url, json=data, headers=header)
        else:
            res = requests.post(url, json=data)
        return res.json()

    def get_main(self, url, data=None, header=None):
        if header == '' or header is None:
            res = requests.get(url, params=data)
        else:
            res = requests.get(url=url, params=data, headers=header)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        if method.lower() == 'get':
            res = self.get_main(url, data, header)
        elif method.lower() == 'post':
            res = self.post_main(url, data, header)
        else:
            return "method错误"
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
