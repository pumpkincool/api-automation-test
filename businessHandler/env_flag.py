class global_env:
    flag = None


def set_env_flag(flag):
    global_env.flag = flag


def get_env_flag():
    return global_env.flag
