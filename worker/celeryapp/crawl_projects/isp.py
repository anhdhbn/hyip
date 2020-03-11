  
from celeryapp.crawl_projects import Project
from celeryapp.utils import *
import requests
from bs4 import BeautifulSoup
import html as html_cvt
from requests import RequestException
import  re
from multiprocessing.dummy import Pool as ThreadPool
import itertools
from datetime import datetime

class Isp:
    def __init__(self, processes=None):
        self.sess = requests.session()
        self.projects = []
        self.pool = ThreadPool(processes=processes)
        data = {
            "mod": "hyiplist",
            "act": "view",
            "n_podtv1": 1,
            "n_podtv15": 2
        }
        self.sess.post("https://investorsstartpage.com/hyiplis", data=data)
        self.step = 12
        self.page = self.get_before_page(self.get_end_page())

    def get_projecs_from_page(self, i):
        projects = []
        curr_url = f"https://investorsstartpage.com/hyiplist/n_page/{i}"
        html = self.sess.get(curr_url).text
        soup = self.get_soup(html)
        items = soup.select("div.content-wrapper__center div.hyip-info div.hyip-info__head-left > div.hyip-info__project > a.hyip-info__link")
        return [item.attrs['href'] for item in items]

    def crawl_project(self, link):
        try:
            url = self.get_link_from_url(f"https://investorsstartpage.com/{link}")

            return Project(**{
                "url_crawl": url,
            })
        except requests.exceptions.RequestException :
            print(link)
        except requests.exceptions.HTTPError:
            print(link)
        except requests.exceptions.ConnectionError:
            print(link)
        except requests.exceptions.Timeout:
            print(link)
        except Exception as e:
            print(link, e)

    def crawl(self):
        self.urls = list(itertools.chain(*self.pool.map(self.get_projecs_from_page, [i for i in range(1, self.page)])))
        return self.pool.map(self.crawl_project, self.urls)

    def get_soup(self, txt):
        html = html_cvt.unescape(txt)
        return BeautifulSoup(html, "lxml")

    def get_link_from_url(self, url):
        link = requests.get(url, timeout=30).url
        return get_link(link)

    def get_end_page(self):
        url_source = "https://investorsstartpage.com/hyiplist/n_page/"
        for i in range(1, 100):
            html = self.sess.get(f"{url_source}{i * self.step}").text
            if "не найдено" in html:
                return i * self.step

    def get_before_page(self, curr_page):
        url_source = "https://investorsstartpage.com/hyiplist/n_page/"
        for i in range(1, self.step * 2):
            html = self.sess.get(f"{url_source}{curr_page - i}").text
            if "не найдено" not in html:
                return curr_page - i