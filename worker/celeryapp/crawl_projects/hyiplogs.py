  
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

class HyipLogs:
    def __init__(self, processes=None):
        self.sess = requests.session()
        self.pool = ThreadPool(processes=processes)
        self.get_page()

    def crawl(self):
        self.urls = list(itertools.chain(*self.pool.map(self.get_projecs_from_page, [i for i in range(1, self.page)])))
        return self.pool.map(self.crawl_project, self.urls)

    def get_page(self):
        url = "https://hyiplogs.com/hyips/?order=hlindex&sort=desc&str=&date%5Bfrom%5D=&date%5Bto%5D=&hlindex%5Bfrom%5D=&hlindex%5Bto%5D=&status%5B1%5D=1&page=1"
        txt = requests.get(url).text
        self.page = int(re.findall('data-page="(.*?)"', txt)[-1])

    def get_link_from_url(self, url):
        return get_link(url)

    def crawl_project(self, url):
        try:
            txt = requests.get("https://hyiplogs.com" + url).text
            soup = self.get_soup(txt)
            href = self.get_link_from_url(soup.select_one("div.cf div.name-box > a").get("href"))

            return Project(**{
                "url_crawl": href,
            })
        except Exception as e:
            print(e)

    def get_projecs_from_page(self, i):
        try:
            txt = requests.get(f"https://hyiplogs.com/hyips/?order=hlindex&sort=desc&str=&date%5Bfrom%5D=&date%5Bto%5D=&hlindex%5Bfrom%5D=&hlindex%5Bto%5D=&status%5B1%5D=1&page={i}").text
            soup = self.get_soup(txt)
            items = soup.select("div.item.ovh")
            return [item.select_one("div.name-box > a").get('href') for item in items]
        except Exception as e:
            print(e)
            return []

    def get_soup(self, txt):
        html = html_cvt.unescape(txt)
        return BeautifulSoup(html, "lxml")