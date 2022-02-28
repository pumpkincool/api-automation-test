# api-automation-test
本工具用于自动执行excel人工管理的接口测试用例，并将执行结果回写至excel中。开发语言为python,主要依赖库为requests。

各模块介绍：
<br>base：存放接口发送功能相关代码，根据接口类型进行数据组装并发送请求
<br>data：解析data_config中的模型，进行数据读取及依赖处理，调用util中的方法获取配置文件中的数据
<br>data_config:excel及json文件存放处，存放测试用例
<br>main:整个工具执行主入口，用于程序运行及对接口返回结果进行进一步处理
<br>report:存放测试报告
<br>util:工具类，对excel及json文件进行解析操作，存放最基本的对文件的读写方法


相关配置：
data.get_data.py文件中getData类init方法可以传入Excel的文件路径以及sheet页。如不传入，默认执行工程中data_config下的case.xls文件
			 传参事例：self.opera_excel = operateExcel(file_name='路径', sheet_id=1)
excel用例中的request内容使用json进行管理，通过关键字进行关联，json文件路径可在data.get_data.py文件中getData类get_json方法传入。如不传入，默认使用工程中data_config下的request.json文件
			 传参事例：oper_json = operateJson(filename='路径')
			 
		
请求下发：
使用requests库构建请求。如下：
requests.post(url, json=data, headers=header)

excel管理：
如excel表头顺序或字段与样例不一致，可在data.data_config_excel.py中重新定义。

运行方式：
直接运行main下的run_main.py即可。

第三方包管理：
如：已引用的第三方包及版本列表：
requests==2.27.1
urllib3==1.26.8
BeautifulReport==0.1.3
可在用例工具运行机器上快速安装所需依赖包。
