import configparser
# from pythonRequest.main.run_py import env_flag


class EnvInfo:
    def __init__(self, env_flag='test'):
        self.env_flag = env_flag
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
    

    