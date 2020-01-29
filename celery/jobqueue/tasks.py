from celery import Celery
import requests
from jobqueue import app_info

app = Celery("hyip")
app.config_from_object("jobqueue.settings")

@app.task(name='jobqueue.tasks.crawl_easy_project_every_day')
def crawl_easy_project_every_day():
    result = requests.get(app_info.url_get_easy_project)
    result = result.json()
    for item in result['data']:
        crawl_easy_project.delay(**item)
    return len(result['data'])

@app.task(name='jobqueue.tasks.crawl_easy_project')
def crawl_easy_project(**kwargs):
    from jobqueue.easy import EasyProject
    temp = EasyProject(**kwargs)
    result = temp.crawl()
    return True