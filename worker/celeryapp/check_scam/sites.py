
import requests
import re
from bs4 import BeautifulSoup
import html as html_cvt

def get_soup(url):
    html = requests.get(url).text
    html = html_cvt.unescape(html)
    return BeautifulSoup(html, "lxml")

def isp(domain):
    url = "https://investorsstartpage.com/check/d/" + domain
    soup = get_soup(url)
    status = soup.select_one("div.hyipBox__label.hyipBox__label--green")
    if status is None:
        return False
    else:
        text = status.text.lower()
        return "paying" in status

def hyiplogs(domain):
    url = f"https://hyiplogs.com/project/{domain.replace('www', '')}/"
    soup = get_soup(url)
    lst_status = soup.select('div.mt10.mb15 > div')
    if(len(lst_status) == 0):
        return -1
    current_status = 4
    for status in lst_status:
        txt = status.text
        if "Paying" in txt:
            current_status = min(current_status, 0)
        if "Waiting" in txt or "Not tracked" in txt:
            current_status = min(current_status, 1)
        if "HIGH RISK" in txt or "Problem" in txt:
            current_status = min(current_status, 2)
        if "Not paying" in txt:
            current_status = min(current_status, 3)
    return current_status

arr_func = [hyiplogs]