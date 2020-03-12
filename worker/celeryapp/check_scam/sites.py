
import requests
import re
from bs4 import BeautifulSoup
import html as html_cvt

def get_soup(url):
    html = requests.get(url).text
    html = html_cvt.unescape(html)
    return BeautifulSoup(html, "lxml"), html

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
    soup, html = get_soup(url)
    lst_status = soup.select('div.mt10.mb15 > div')
    all_status = soup.select_one('div.mt10.mb15')
    if(len(lst_status) == 0):
        return -1
    current_status = 4
    for status in lst_status:
        txt = status.text
        if "HIGH RISK" in txt:
            current_status = min(current_status, 2)
        if "Not tracked" in txt:
            current_status = min(current_status, 1)

    

    regex = re.findall("(Paying|Waiting|Problem|Not paying) \((\d{1,2})\)", all_status.text)
    if len(regex) > 0:
        # print(regex)
        result = max(regex, key=lambda x: int(x[1]))
        status = result[0]
        if "Paying" == status:
            current_status = 0
        if "Waiting" == status:
            current_status = 1
        if "Problem" == status:
            current_status = 2
        if "Not paying" == status:
            current_status = 3
    

    return current_status

arr_func = [hyiplogs]