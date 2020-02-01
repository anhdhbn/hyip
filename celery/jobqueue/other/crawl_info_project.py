
from urllib.parse import urlparse
import requests
import re
import datetime
import html
import time
from jobqueue import app_info
import cloudscraper
from .get_info_ssl import get_ssl_info_from_domain

def str2date(str):
    return datetime.datetime.strptime(str, "%Y-%m-%d").date()

def str2date_length(s):
    return datetime.datetime.strptime(s.strip(), "%d %b %Y %H:%M:%S").date()

def get_info_from_domain(url):
    parsed_uri = urlparse(url)
    domain = parsed_uri.netloc
    html2 = requests.get("https://www.whois.com/whois/{}".format(domain)).text
    matches = re.findall('df-value">(.*?)<', html2)
    if len(matches) < 4:
        return {
            'name': domain,
        }
    name = domain
    registrar = matches[1]
    from_date = str2date(matches[2])
    to_date = str2date(matches[3])
    return {
        'name': name, 
        'registrar': registrar, 
        'from_date': from_date.strftime('%Y-%m-%d'), 
        'to_date': to_date.strftime('%Y-%m-%d')
    }



def get_hosting_info_from_domain(url):
    parsed_uri = urlparse(url)
    domain = parsed_uri.netloc
    payload = {'action':'wx__domain_hostcheker','domain':domain}
    headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    session = requests.Session()
    res = session.post("https://hostingchecker.com/wp-admin/admin-ajax.php", data=payload)
    hosting = re.findall("is hosted on <strong>(.*?)<", res.text)
    if  len(hosting) == 0:
        return get_hosting_info_from_domain(url)
    else:
        return hosting[0]


def get_ip_info_from_domain(url):
    parsed_uri = urlparse(url)
    domain = parsed_uri.netloc
    address = requests.get("http://ip-api.com/json/{}".format(domain)).json()['query']
    Domains = requests.get("https://api.hackertarget.com/reverseiplookup/?q={}".format(domain)).text.splitlines()
    domains_of_this_ip = ",".join(Domains)
    return {
        'address':  address, 
        'domains_of_this_ip': domains_of_this_ip
    }

def check_easy_crawl(url):
    from jobqueue.easy import EasyProject
    temp = EasyProject(url=url)
    inves, paidout,  member = temp.get_info_project()
    return True if int(inves) != -1 and int(paidout) != -1 else False

def get_source(url):
    scraper = cloudscraper.create_scraper()
    html = scraper.get(url, timeout=30).text
    return html

class Object(object):
    pass

class CrawlInfoProject:
    def __init__(self, **kwargs):
        self.project = Object()
        self.domain = None
        self.ip = None
        self.ssl = None
        self.status = {}
        self.script = {}
        for k, v in kwargs.items():
            setattr(self.project, k, v)
        if ('status_project' in kwargs.keys()):
            self.status['status_project'] = self.project.status_project
            del self.project.status_project
        if ('script_type' in kwargs.keys()):
            self.script['script_type'] = self.project.script_type
            del self.project.script_type

    def crawl(self):
        self.domain = get_info_from_domain(self.project.url)
        self.ip = get_ip_info_from_domain(self.project.url)
        self.ssl = get_ssl_info_from_domain(self.project.url)
        self.project.hosting = get_hosting_info_from_domain(self.project.url)
        

        self.project.easy_crawl = check_easy_crawl(self.project.url)

        self.script['source_page'] = get_source(self.project.url)

        r = requests.post(app_info.url.post_create_project_by_crawler, json={
            'project': self.project.__dict__,
            'domain': self.domain,
            'ip':  self.ip,
            'ssl': self.ssl,
            'status': self.status,
            'script': self.script
        })
    
    def debug(self, mess):
        print(f"{self.project.url} {mess}")
    
    def _set_attr(self, obj, dic):
        for k, v in dic.items():
            setattr(obj, k , v)