import sys
import os
from util.time_util import TimeUtil

log_level = 5


class LogUtil:
    def __init__(self):
        self.now_time = TimeUtil.get_time_stamp()
        self.filename = os.path.basename(__file__)
        self.line = sys._getframe().f_lineno
    
    def info_log(self, value):
        if log_level > 3:
            print("\033[32m[%s][info][%s:%s]%s\033[0m" % (self.now_time, self.filename, self.line, value))
     
    def error_log(self, value):
        if log_level != 0:
            print("\033[31m[%s][error][%s:%s]%s\033[0m" % (self.now_time, self.filename, self.line, value))
     
    def warning_log(self, value):
        if log_level > 1:
            print("\033[33m[%s][warning][%s:%s]%s\033[0m" % (self.now_time, self.filename, self.line, value))
    
    def debug_log(self, value):
        if log_level > 5:
            print("\033[34m[%s][debug][%s:%s]%s\033[0m" % (self.now_time, self.filename, self.line, value))
