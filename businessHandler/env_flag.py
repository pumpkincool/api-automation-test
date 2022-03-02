class GlobalEnv:
    flag = 'test'


def set_env_flag(flag):
    GlobalEnv.flag = flag


def get_env_flag():
    return GlobalEnv.flag
