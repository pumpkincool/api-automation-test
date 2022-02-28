from pythonRequest.data.data_config_excel import *
import configparser


class EnvInfo:
    def __init__(self):
        self.env_flag = get_env_flag()
        self.config = configparser.ConfigParser()
        self.config.read('../env/env.ini')
        
    def get_host(self):
        return self.config.get(self.env_flag, 'host')
    
    def get_username(self):
        return self.config.get(self.env_flag, 'username')
    
    def get_password(self):
        return self.config.get(self.env_flag, 'password')
    
    def get_db(self):
        return self.config.get(self.env_flag, 'db')
    
    def get_dusername(self):
        return self.config.get(self.env_flag, 'dusername')
    
    def get_dpassword(self):
        return self.config.get(self.env_flag, 'dpassword')


if __name__ == '__main__':
    EnvInfo().get_host()
    

    