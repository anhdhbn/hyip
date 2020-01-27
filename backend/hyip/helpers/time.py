import os

def get_max_age():
    return int(os.getenv('TOKEN_UPTIME', 24)) * 60

def get_expired_time():
    return (datetime.datetime.now() +
            datetime.timedelta(minutes=int(os.getenv('TOKEN_UPTIME', 24))))
