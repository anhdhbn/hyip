
from urllib.parse import urlparse
import requests
import re
import datetime
import html
import time
from jobqueue import app_info

def str2date(str):
    return datetime.datetime.strptime(str, "%Y-%m-%d").date()

def str2date_length(s):
    return datetime.datetime.strptime(s.strip(), "%d %b %Y %H:%M:%S").date()

def get_info_from_domain(url):
    parsed_uri = urlparse(url)
    domain = parsed_uri.netloc
    html2 = requests.get("https://www.whois.com/whois/{}".format(domain)).text
    matches = re.findall('df-value">(.*?)<', html2)
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

def get_ssl_info_from_domain(url):
    parsed_uri = urlparse(url)
    domain = parsed_uri.netloc
    requests.get("https://www.ssllabs.com/ssltest/analyze.html?viaform=off&d={}".format(domain))
    html2 = ""
    url_ = "https://www.ssllabs.com/ssltest/analyze.html?d={}&latest".format(domain)
    use_ip_url = False

    while True:
        if not use_ip_url:
            html2 = html.unescape(html2)
            check  =  re.findall('(analyze\.html.*?)"',  html2)
            if  len(check) > 1:
                url_ = "https://www.ssllabs.com/ssltest/" + check[1]
                use_ip_url = True
        html2 = requests.get(url_).text
        if "Server Key and Certificate" in html2:
            break
        
        time.sleep(1)
    matches = re.findall('tableCell">.*,(.*)UTC.*<', html2)
    from_date = str2date_length(matches[0].strip())
    to_date = str2date_length(matches[1].strip())
    match = re.findall(r'Extended Validation</(.*?)>', html2)[0]
    ev = True if match == "font" else False
    Issuer = re.findall(r'Issuer.*?title=".*?">(.*?)<', html2, re.DOTALL)[0].strip()
    description = html.unescape(Issuer)
    return {
        'ev': ev, 
        'from_date': from_date.strftime('%Y-%m-%d'), 
        'to_date': to_date.strftime('%Y-%m-%d'), 
        'description': description
    }

def get_hosting_info_from_domain(url):
    parsed_uri = urlparse(url)
    domain = parsed_uri.netloc
    payload = {'action':'wx__domain_hostcheker','domain':domain}
    headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    session = requests.Session()
    res = session.post("https://hostingchecker.com/wp-admin/admin-ajax.php", data=payload)
    hosting = re.findall("is hosted on <strong>(.*?)<", res.text)[0]
    return hosting


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

class Object(object):
    pass

class CrawlProject:
    def __init__(self, **kwargs):
        self.project = Object()
        self.domain = None
        self.ip = None
        self.ssl = None
        for k, v in kwargs.items():
            setattr(self.project, k, v)
    def crawl(self):
        self.domain = get_info_from_domain(self.project.url)
        self.ip = get_ip_info_from_domain(self.project.url)
        self.ssl = get_ssl_info_from_domain(self.project.url)
        self.project.hosting = get_hosting_info_from_domain(self.project.url)
        
        self.project.easy_crawl = check_easy_crawl(self.project.url)

        r = requests.post(app_info.url_get_post_create_project, json={
            'project': self.project.__dict__,
            'domain': self.domain,
            'ip':  self.ip,
            'ssl': self.ssl
        })
    
    def _get_kwargs(self,  obj):
        pass
    
    def _set_attr(self, obj, dic):
        for k, v in dic.items():
            setattr(obj, k , v)