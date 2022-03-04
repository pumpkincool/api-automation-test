from datetime import datetime, timedelta
import time

class TimeUtil:
    
    @staticmethod
    def get_now():
        """
        获取当前时间
        :return: string, 如：'2022-02-24 17:54:04'
        """
        return str(datetime.now()).split('.')[0]
    
    @staticmethod
    def get_time_stamp():
        """
        获取当前时间
        :return: string, 如：'2022-02-24 17:54:04.630'
        """
        ct = time.time()
        local_time = time.localtime(ct)
        data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        data_secs = (ct - int(ct)) * 1000
        time_stamp = "%s.%03d" % (data_head, data_secs)
        return time_stamp
    
    @staticmethod
    def datetime_to_timestamp(dtime):
        """
        datetime转换为timestamp, 如：2015-04-19 12:20:00 转 1429417200
        :param dtime: datetime, 如：2015-04-19 12:20:00
        :return: int, 如：1429417200
        """
        return int(dtime.timestamp())
    
    @staticmethod
    def timestamp_to_datetime(tstamp):
        """
        timestamp转换为datetime, 如：1429417200 转 2015-04-19 12:20:00
        :param tstamp: int, 如：1429417200
        :return: datetime, 如：2015-04-19 12:20:00
        """
        return datetime.fromtimestamp(tstamp)
    
    @staticmethod
    def str_to_datetime(str_time):
        """
        string类型时间转换为datetime, 如：'2015-04-19 12:20:00' 转 2015-04-19 12:20:00
        :param str_time: string, 如：'2015-04-19 12:20:00'
        :return: datetime, 如：2015-04-19 12:20:00
        """
        return datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
        
    @staticmethod
    def datetime_to_str(dtime):
        """
        datetime时间转换为str类型, 如：2015-04-19 12:20:00 转 '2015-04-19 12:20:00'
        :param dtime: datetime, 如：2015-04-19 12:20:00
        :return: string, 如：'2015-04-19 12:20:00'
        """
        return dtime.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def datetime_opt(dtime, days=0, hours=0, seconds=0):
        """
        在datetime类型时间基础上进行加减操作，如：几天前 或 几天后的时间
        :param dtime: datetime, 如：2015-04-19 12:20:00
        :param days: int, 天数偏移量
        :param hours: int, 小时偏移量
        :param seconds: int, 秒偏移量
        :return: 偏移后的datetime时间
        """
        return dtime + timedelta(days)


if __name__ == '__main__':
    TimeUtil.get_now()
    TimeUtil.datetime_to_timestamp(datetime.now())
    TimeUtil.timestamp_to_datetime(1429417200)
    TimeUtil.str_to_datetime('2015-04-19 12:20:00')
    TimeUtil.datetime_to_str(TimeUtil().str_to_datetime('2015-04-19 12:20:00'))
    TimeUtil.datetime_opt(TimeUtil().str_to_datetime('2015-04-19 12:20:00'), days=3)
    
