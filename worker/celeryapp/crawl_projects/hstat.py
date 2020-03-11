  
from celeryapp.crawl_projects import Project
from celeryapp.utils import get_link
import requests
from bs4 import BeautifulSoup
import html as html_cvt
from requests import RequestException
import  re
from multiprocessing.dummy import Pool as ThreadPool
import itertools
from datetime import datetime

class HStat:
    def __init__(self, processes=None):
        self.sess = requests.session()
        self.pool = ThreadPool(processes=processes)
        self.get_page()

    def crawl(self):
        self.urls = list(itertools.chain(*self.pool.map(self.get_projecs_from_page, [i for i in range(1, self.page)])))
        return self.pool.map(self.crawl_project, self.urls)

    def get_page(self):
        url = "https://h-stat.com/paying/1"
        txt = self.sess.get(url).text
        token = re.findall(f'token = "(.*?)"', txt)[0]
        data = {
            "method": "get_projects",
            "page": 1,
            "project": "1",
            "language": 1,
            "category": "paying",
            "search": "",
            "token": token
        }
        result = self.sess.post("https://h-stat.com/index.php", data=data).json()
        self.token = token
        self.page = result['response']['page']['pages']


    def get_link_from_url(self, url):
        link = requests.get(f"https://{url}", timeout=30).url
        return get_link(link)

    def crawl_project(self, url):
        try:
            link = self.get_link_from_url(url)

            return Project(**{
                "url_crawl": link,
            })
        except requests.exceptions.RequestException :
            print(url)
        except requests.exceptions.HTTPError:
            print(url)
        except requests.exceptions.ConnectionError:
            print(url)
        except requests.exceptions.Timeout:
            print(url)
        except Exception as e:
            print(url, e)

    def get_projecs_from_page(self, i):
        try:
            data = {
                "method": "get_projects",
                "page": i,
                "project": "1",
                "language": 1,
                "category": "paying",
                "search": "",
                "token": self.token
            }
            result = self.sess.post("https://h-stat.com/index.php", data=data).json()['response']['projects']
            return [project['data'][4] for project in result]
        except Exception as e:
            print(e)
            return []

    def get_soup(self, txt):
        html = html_cvt.unescape(txt)
        return BeautifulSoup(html, "lxml")