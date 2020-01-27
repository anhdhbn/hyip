from celery import Celery

app = Celery("hyip")
app.config_from_object("jobqueue.settings")

@app.task(name='jobqueue.tasks.crawl_data_every_day')
def crawl_data_every_day():
    import requests
    from jobqueue import app_info
    result = requests.get("{}api/project/all".format(app_info.host))
    result = result.json()

    for item in result['data']:
        id = item['id']
        InvesmentSelector = item['investment_selector']
        PaidOutSelector = item['paid_out_selector']
        MemberSelector = item['member_selector']
        Url = item['url']
        crawl_a_project.delay(id, InvesmentSelector, PaidOutSelector, MemberSelector, Url)

@app.task(name='jobqueue.tasks.crawl_a_project')
def crawl_a_project(*args):
    from jobqueue import Sites
    temp = Sites()
    
    try:
        total_investment, total_paid_out, total_account = temp.crawl(*args)
        temp.quit()
        alexa_rank = temp.get_alexa_rank()
        # print(f"\n{total_investment}\n{total_paid_out}\n{total_account}\n{alexa_rank}")
        temp.save_data(total_investment, total_paid_out, total_account, alexa_rank)
    except:
        temp.quit()