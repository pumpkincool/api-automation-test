from datetime import datetime


class TimeUtil:
    
    @staticmethod
    def get_now(self):
        """
        获取当前时间
        :param self:
        :return: string, 如：2022-02-24 17:54:04
        """
        return str(datetime.now()).split('.')[0]
    
    @staticmethod
    def datetime_to_timestamp(self, dtime):
        """
        datetime转换为timestamp, 如：2015-04-19 12:20:00 转 1429417200
        :param self:
        :param dtime: datetime, 如：2015-04-19 12:20:00
        :return: int, 如：1429417200
        """
        return int(dtime.timestamp())
    
    @staticmethod
    def timestamp_to_datetime(self, tstamp):
        """
        timestamp转换为datetime, 如：1429417200 转 2015-04-19 12:20:00
        :param self:
        :param tstamp: int, 如：1429417200
        :return: datetime, 如：2015-04-19 12:20:00
        """
        return datetime.fromtimestamp(tstamp)
    

if __name__ == '__main__':
    TimeUtil().get_now()
    TimeUtil().datetime_to_timestamp(datetime.now())
    TimeUtil().timestamp_to_datetime(1429417200)
