
from urllib.parse import urlparse
import requests
import re
import datetime
import html
import time

def str2date(str):
    return datetime.datetime.strptime(str, "%Y-%m-%d").date()

def str2date_length(s):
    return datetime.datetime.strptime(s.strip(), "%d %b %Y %H:%M:%S").date()

def get_domain(url):
    parsed_uri = urlparse(url)
    return parsed_uri.netloc

def get_info_from_domain(url):
    parsed_uri = urlparse(url)
    domain = parsed_uri.netloc
    html2 = requests.get("https://www.whois.com/whois/{}".format(domain)).text
    matches = re.findall('df-value">(.*?)<', html2)
    name = domain
    registrar = matches[1]
    from_date = str2date(matches[2])
    to_date = str2date(matches[3])
    return name, registrar, from_date, to_date

def get_ssl_info_from_domain(url):
    parsed_uri = urlparse(url)
    domain = parsed_uri.netloc
    requests.get("https://www.ssllabs.com/ssltest/analyze.html?viaform=off&d={}".format(domain))
    html2 = ""
    url_ = "https://www.ssllabs.com/ssltest/analyze.html?d={}&latest".format(domain)
    while True:
        html2 = html.unescape(html2)
        check  =  re.findall('(analyze\.html.*?)"',  html2)
        if  len(check) > 1:
            url_ = "https://www.ssllabs.com/ssltest/" + check[-1]
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
    return ev, from_date, to_date, description

def get_hosting_info_from_domain(url):
    parsed_uri = urlparse(url)
    domain = parsed_uri.netloc
    payload = {'action':'wx__domain_hostcheker','domain':domain}
    headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    session = requests.Session()
    res = session.post("https://hostingchecker.com/wp-admin/admin-ajax.php", data=payload)
    Hosting = re.findall("is hosted on <strong>(.*?)<", res.text)[0]
    return Hosting


def get_ip_info_from_domain(url):
    parsed_uri = urlparse(url)
    domain = parsed_uri.netloc
    address = requests.get("http://ip-api.com/json/{}".format(domain)).json()['query']
    Domains = requests.get("https://api.hackertarget.com/reverseiplookup/?q={}".format(domain)).text.splitlines()
    domains_of_this_ip = ",".join(Domains)
    return address, domains_of_this_ip

