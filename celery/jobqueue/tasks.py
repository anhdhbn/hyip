from celery import Celery

app = Celery("hyip")
app.config_from_object("jobqueue.settings")

@app.task(name='jobqueue.tasks.crawl_data_every_day')
def crawl_data_every_day():
    import requests
    from jobqueue import app_info
    result = requests.get("{}api/project/easy".format(app_info.host))
    result = result.json()
    for item in result['data']:
        url = item['url']
        id = item['id']
        crawl_easy_project.delay(url=url, id=id)
    return len(result['data'])

@app.task(name='jobqueue.tasks.crawl_easy_project')
def crawl_easy_project(**kwargs):
    from jobqueue.easy import EasyProject
    temp = EasyProject(**kwargs)
    result = temp.crawl()
    return True