from jobqueue.crawl_project import Project
from jobqueue import get_link, get_domain
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
            "n_podtv1": 1
        }
        self.sess.post("https://investorsstartpage.com/hyiplis", data=data)
        self.page = self.get_before_page(self.get_end_page())
        # self.page = 5

    def get_projecs_from_page(self, i):
        projects = []
        curr_url = f"https://investorsstartpage.com/hyiplist/n_page/{i}"
        html = self.sess.get(curr_url).text
        soup = self.get_soup(html)
        items = soup.select("div.content-wrapper__center div.hyip-info")

        for item in items:
            link = ""
            try:
                status = item.select_one("div.hyip-info__head-left > div").text
                status_project = 1

                link = item.select_one("div.hyip-info__head-left > div.hyip-info__project > a.hyip-info__link").attrs['href']
                url = self.get_link_from_url(f"https://investorsstartpage.com/{link}")
                
                plans = item.select_one("div.hyip-info__main li.hyip-info__info-row div.hyip-info__info-right > div").text
                if "isp:" in plans.lower():
                    plans = ""

                script = item.select_one("ul.hyip-info__list > li:nth-child(5)").text.lower()
                script_type = 0
                if "not licensed" in script:
                    script_type = 2
                elif "not defined" in script:
                    script_type = 1
                elif "licensed" in script:
                    script_type = 0

                projects.append(Project(**{
                    "status_project": 1,
                    "url": url,
                    "script_type": script_type,
                    "plans": plans,
                    "start_date": self.get_date(url)
                }))
            except requests.exceptions.RequestException :
                print(link)
            except requests.exceptions.HTTPError:
                print(link)
            except requests.exceptions.ConnectionError:
                print(link)
            except requests.exceptions.Timeout:
                print(link)
        return projects

    def crawl(self):
        self.projects = list(itertools.chain(*self.pool.map(self.get_projecs_from_page, [i for i in range(1, self.page)])))
        return self.projects

    def get_date(self, url):
        domain = get_domain(url)
        res = requests.get(f"https://hyiplogs.com/project/{domain}/").text
        if "sorry, this page not found" in res:
            return ""
        else:
            soup = BeautifulSoup(res, "lxml")
            start_date = soup.select_one("div.mt5.mb5.fl")
            if start_date is None:
                return ""
            else:
                arr = re.findall(r":(.*?)(\(|Scam|Problem|$)", start_date.text, re.DOTALL)        
                temp1, temp2 = arr[0]
                temp = temp1.strip()
                return str(datetime.strptime(temp, '%b %d, %Y').date())

    def get_soup(self, txt):
        html = html_cvt.unescape(txt)
        return BeautifulSoup(html, "lxml")

    def get_link_from_url(self, url):
        link = requests.get(url, timeout=30).url
        return get_link(link)

    def get_end_page(self):
        url_source = "https://investorsstartpage.com/hyiplist/n_page/"
        curr_page = 1
        while True:
            html = self.sess.get(f"{url_source}{curr_page}").text
            if "не найдено" in html:
                return curr_page - 1
            match = re.findall('hyiplist/n_page\/(.*?)"', html)[-1]
            new = int(match)
            if new < curr_page:
                return curr_page - 1
            else:
                curr_page = new

    def get_before_page(self, curr_page):
        url_source = "https://investorsstartpage.com/hyiplist/n_page/"
        while True:
            html = self.sess.get(f"{url_source}{curr_page}").text
            if "не найдено" in html:
                curr_page -= 1
            else:
                return curr_page
