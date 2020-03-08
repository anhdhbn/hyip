import requests
import re
from bs4 import BeautifulSoup

class CrawlBase:
    def get_alexa_rank(self):
        from celeryapp.utils import get_domain
        domain = get_domain(self.url_crawl)
        txt = requests.get("http://data.alexa.com/data?cli=10&dat=s&url="+ domain).text
        if "REACH" in txt:
            result = BeautifulSoup(txt, "xml").find("REACH")['RANK']
            return int(result)
        return -1
    
    def save_data(self, **kwargs):
        from celeryapp import celery
        res = requests.post(celery.conf.URL['post_data_crawled'](self.id), json=kwargs)
        res.raise_for_status()
        return res.json()['data']

    def crawl(self):
        alexa_rank = self.get_alexa_rank()
        total_investments, total_paid_outs, total_members = self.get_info_project()
        return self.save_data(alexa_rank=alexa_rank, total_investments=total_investments, total_members=total_members, total_paid_outs=total_paid_outs)

    def get_only_info_project(self):
        total_investments, total_paid_outs, total_members = self.get_info_project()
        return {
            'total_investments': total_investments,
            'total_paid_outs': total_paid_outs,
            'total_members': total_members,
        }

    def preprocess_data(self, data):
        data = data.split("+")[0]
        def remove_at(i, s):
            return s[:i] + s[i+1:]
    
        def clear_text(s):
            if '.' in s:
                start = s.index('.')
                while True:
                    try:
                        index = s.index('.', start + 1)
                        s = remove_at(index, s)
                    except:
                        break
            return s
        return clear_text(re.sub(r"[^0-9\.]", "", data))

    def get_info_project(self):
        raise NotImplementedError

