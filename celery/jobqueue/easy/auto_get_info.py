import html as html_cvt
import time
from bs4 import BeautifulSoup
from bs4.element import Comment, NavigableString, Tag
import re
import cloudscraper
from jobqueue import app_info
import os
from urllib.parse import urlparse
import requests

def read_file(filename):
    with open(filename) as f:
        content = f.readlines()
    return [x.strip() for x in content]

investment = read_file(os.path.join(app_info.path, "easy", "investment.txt"))
paid_out = read_file(os.path.join(app_info.path, "easy", "withdrawal.txt"))
member = read_file(os.path.join(app_info.path, "easy", "account.txt"))


class EasyProject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def crawl(self):
        alexa_rank = int(self.get_alexa_rank())
        total_investment, total_paid_out, total_member = self.get_info_project()
        self.save_data(alexa_rank=alexa_rank, total_investment=total_investment, total_member=total_member, total_paid_out=total_paid_out)

    def save_data(self, **kwargs):
        try:
            from jobqueue import app_info
            res = requests.post(app_info.url.post_data_crawled(self.id), json=kwargs)
            res.raise_for_status()
        except:
            print("Data error {}".format(self.url))

    def get_alexa_rank(self):
        parsed_uri = urlparse(self.url)
        domain = parsed_uri.netloc
        txt = requests.get("http://data.alexa.com/data?cli=10&dat=s&url="+ domain).text
        return BeautifulSoup(txt, "xml").find("REACH")['RANK']

    def get_only_info_project(self):
        total_investment, total_paid_out, total_member = self.get_info_project()
        return {
            'total_investment': total_investment,
            'total_paid_out': total_paid_out,
            'total_member': total_member,
        }

    def get_info_project(self):
        scraper = cloudscraper.create_scraper()
        html = scraper.get(self.url, timeout=30).text
        html = html_cvt.unescape(html)
        soup = BeautifulSoup(html, "lxml")

        texts = soup.findAll(text=True)
        visible_texts = filter(self._tag_visible, texts)

        visible_texts = [item for item in visible_texts if item is not None]
        visible_texts = [item for item in visible_texts if len(item) <= 25 and len(item) >= 4]
        return self._check_in_list(visible_texts, investment), self._check_in_list(visible_texts, paid_out), self._check_in_list(visible_texts, member, int)


    def _tag_visible(self, element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True

    def _check_num(self, s, type):
        try:
            return type(s)
        except ValueError:
            pass

    def _get_parent_up_lever(self, children, num):
        current = children.parent
        for i in range(num):
            current = current.parent
        return current.children
    
    def _check_in_list(self, items, lst, type=float):
        result = []
        for item in items:
            if any(word in item.lower() for word in lst):
                result.append(item)

        for item in result:
            for i in range(3):
                for children in self._get_parent_up_lever(item, i):
                    check = children
                    if isinstance(children, Tag):
                        check = children.text
                    
                    if len(check) <= 25 and len(check) >= 4:
                        txt = re.sub("[^0-9\.]", "", check)
                        temp = self._check_num(txt, type)
                        if temp is not None:
                            return temp
        return type(-1)