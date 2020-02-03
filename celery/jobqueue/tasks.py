from celery import Celery
import requests
from jobqueue import app_info

app = Celery("hyip")
app.config_from_object("jobqueue.settings")

@app.task(name='jobqueue.tasks.crawl_easy_project_every_day')
def crawl_easy_project_every_day():
    result = requests.get(app_info.url.get_easy_project)
    result = result.json()
    for item in result['data']:
        crawl_easy_project.delay(**item)
    return len(result['data'])

@app.task(name='jobqueue.tasks.crawl_info_project')
def crawl_info_project(**kwargs):
    from jobqueue.other import CrawlInfoProject
    temp = CrawlInfoProject(**kwargs)
    temp.crawl()
    return True

@app.task(name='jobqueue.tasks.crawl_easy_project')
def crawl_easy_project(**kwargs):
    from jobqueue.easy import EasyProject
    temp = EasyProject(**kwargs)
    result = temp.crawl()
    return True

@app.task(name='jobqueue.tasks.check_scam_all')
def check_scam_all():
    result = requests.get(app_info.url.get_not_scam_project).json()
    for item in result['data']:
        check_scam.delay(item)
    return len(result['data'])

@app.task(name='jobqueue.tasks.check_scam')
def check_scam(project):
    from jobqueue.check_scam import CheckStatusProject
    temp = CheckStatusProject()
    result = temp.check(project)
    return "{} scam is {}".format(project['url'], result)

@app.task(name='jobqueue.tasks.crawl_project')
def crawl_project():
    from jobqueue.crawl_project import CrawlProjects
    temp = CrawlProjects()
    result = temp.crawl()
    return result


@app.task(name="jobqueue.tasks.check_selector")
def check_selector(**kwargs):
    from jobqueue.other import CheckSelector
    temp = CheckSelector(**kwargs)
    return temp.check()

@app.task(name="jobqueue.tasks.check_easy")
def check_easy(**kwargs):
    from jobqueue.easy import EasyProject
    temp = EasyProject(**kwargs)
    return temp.get_onyl_info_project()