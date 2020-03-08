import os

class BaseConfig():
    __REDIS_HOST = os.getenv('REDIS_HOST', '')
    __REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', '')
    __REDIS_PORT = os.getenv('REDIS_PORT', '')

    REDIS_URL = 'redis://:{0}@{1}:{2}/0'.format(
        __REDIS_PASSWORD, __REDIS_HOST, __REDIS_PORT
    )


    MONGO_HOST = os.getenv("MONGO_HOST", 'localhost') 
    MONGO_PORT = os.getenv("MONGO_PORT", '27017') 
    MONGO_USER = os.getenv("MONGO_USER", '')
    MONGO_PASS = os.getenv("MONGO_PASS", '')
    MONGO_DB = os.getenv("MONGO_DB", 'hyip')

    MONGO_URL = f'mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}'

    __HUB_HOST=os.getenv("HUB_HOST", 'localhost')
    __HUB_PORT=os.getenv("HUB_PORT", '4444')
    HUB_URL= f'http://{__HUB_HOST}:{__HUB_PORT}/wd/hub'

    HEADLESS = True if os.getenv("HEADLESS") == "1" else False

    __API_PREFIX = 'api'
    global BACKEND_HOST
    BACKEND_HOST = os.getenv('BACKEND_HOST', 'http://localhost:5000/') + __API_PREFIX
    
    URL = {
        'get_easy_project': "{}/projects?type=easy".format(BACKEND_HOST),
        'get_diff_project': "{}/projects?type=diff".format(BACKEND_HOST),
        'get_all_project': "{}/projects?type=all".format(BACKEND_HOST),
        'get_not_scam_project': "{}/projects?type=notscam".format(BACKEND_HOST),
        'post_create_project': "{}/project".format(BACKEND_HOST),

        'get_status': lambda id_project: "{}/status/{}".format(BACKEND_HOST, id_project),
        'post_status': "{}/status".format(BACKEND_HOST),
        
        'get_check_exists_domain': lambda domain: "{}/domain/check-exists/{}".format(BACKEND_HOST, domain),
        
        'post_data_crawled': lambda id_project: "{}/crawldata/{}".format(BACKEND_HOST, id_project),        
    }

class DEV(BaseConfig):
    IS_PRODUCTION = False

class PROD(BaseConfig):
    IS_PRODUCTION = True
    SENTRY_DSN = os.getenv("SENTRY_DSN", "")

class TEST(BaseConfig):
    TESTING = True
    CELERY_ALWAYS_EAGER = True