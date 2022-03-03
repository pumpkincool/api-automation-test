from testcases.script_case.base_demo import BaseDemo


class TestDemo(BaseDemo):
    
    def test01(self):
        # 获取环境信息
        host = BaseDemo.env.get_host()
        BaseDemo.logger.info(host)
        
        # 发送接口请求
        url = 'https://petstore.swagger.io/v2/pet'
        header = {'accept': 'application/json', 'Content-Type': 'application/json'}
        data = BaseDemo.operateJson.read_keyword('pet3')
        rst = BaseDemo.runMethod.post_main(url, data, header)
        BaseDemo.logger.info('rst: ' + str(rst))
        
        # 断言
        self.assertEqual(rst['id'], 60, "the response data is error")
        
        # 如果用例间有数据依赖关系，可通过类变量传递
        TestDemo.depend = rst['id']