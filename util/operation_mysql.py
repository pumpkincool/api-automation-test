import pymysql
from util.log import Logger


class operationMysql:

    def __init__(self, username, passwd, host, database):
        self.username = username
        self.passwd = passwd
        self.host = host
        self.database = database
        self.log = Logger.logger(__name__)

    def connectdb(self):
        conn = pymysql.connect(
            user=self.username,
            password=self.passwd,
            host=self.host,
            database=self.database,
            port=3306,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn

    def querydbrows(self, sql):
        cursor = self.connectdb().cursor()
        result = cursor.execute(sql)
        self.connectdb().cursor().close()
        self.connectdb().close()
        return result

    def querydbone(self, sql):
        cursor = self.connectdb().cursor()
        cursor.execute(sql)
        self.connectdb().cursor().close()
        self.connectdb().close()
        return cursor.fetchone()  # dict

    def querydball(self, sql):
        cursor = self.connectdb().cursor()
        try:
            cursor.execute(sql)
        except Exception as e:
            self.log.error('sql执行错误，请检查语句！')
            return None
        finally:
            self.connectdb().cursor().close()
            self.connectdb().close()
        return cursor.fetchall()  # list


if __name__ == '__main__':
    run = operationMysql('root', '123456', 'localhost', 'danica')
    res = run.querydball('select * from pet where id="80"')
    if res is None or len(res) == 0:
        print("res is none")
    else:
        print(res)
        print(type(res))
