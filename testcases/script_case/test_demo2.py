from testcases.script_case.base_demo import BaseDemo
from parameterized import parameterized


class TestDemo2(BaseDemo):
    
    @parameterized.expand(['pet2', 'pet3'])
    def test02(self, key):
        # 获取环境信息
        host = BaseDemo.env.get_host()
        BaseDemo.log.info_log(host)
        
        # 发送接口请求
        url = 'https://petstore.swagger.io/v2/pet'
        header = {'accept': 'application/json', 'Content-Type': 'application/json'}
        body = BaseDemo.operateJson.read_keyword(key)
        rst = BaseDemo.runMethod.post_main(url, body, header)
        BaseDemo.log.info_log('rst: ' + str(rst))

