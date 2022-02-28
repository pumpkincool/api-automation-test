# api-automation-test
本工具用于自动执行excel人工管理的接口测试用例，并将执行结果回写至excel中。开发语言为python,主要依赖库为requests。

各模块介绍：
<br>base：存放接口发送功能相关代码，根据接口类型进行数据组装并发送请求，增加对环境信息的处理逻辑
<br>data：解析data_config中的模型，进行数据读取及依赖处理，调用util中的方法获取配置文件中的数据
<br>data_config:excel及json文件存放处，存放测试用例，存放log的基础配置信息
<br>main:整个工具执行主入口，用于程序运行及对接口返回结果进行进一步处理
<br>report:存放测试报告
<br>util:工具类，对excel，json，mysql，log等进行处理，存放基础方法
<br>log:日志记录，如将日志打印在文件中，会在该目录下生成log.log文件
<br>env:环境信息，不同环境相关的数据库信息可存放在此处


相关配置：
data.get_data.py文件中getData类init方法可以传入Excel的文件路径以及sheet页。如不传入，默认执行工程中data_config下的case.xls文件
			 传参事例：self.opera_excel = operateExcel(file_name='路径', sheet_id=1)
excel用例中的request内容使用json进行管理，通过关键字进行关联，json文件路径可在data.get_data.py文件中getData类get_json方法传入。如不传入，默认使用工程中data_config下的request.json文件
			 传参事例：oper_json = operateJson(filename='路径')
env下env.ini文件支持对不同环境的数据库连接信息进行配置，如host，username，password，db等
	 
		
请求下发：
使用requests库构建请求。如下：
requests.post(url, json=data, headers=header)

excel管理：
如excel表头顺序或字段与样例不一致，可在data.data_config_excel.py中重新定义。

支持的断言：
excel文件期望结果列支持字符串以及sql语句，分别的编写方式如下：
sql： select xxx from xxx（需要加sql：前缀）
字符串格式直接写对应的字符串即可，支持同时检测多个字符串，多个字符串用分号；分割

运行方式：
直接运行main下的run_main.py即可，运行完成后会将结果回写到excel用例下。

第三方包管理：
将依赖包配置在requirements.txt文件下，格式如下:
BeautifulReport==0.1.3
requests==2.27.1
文件自动生成pip freeze >requirements.txt
依赖包安装：pip install -r requirements.txt
