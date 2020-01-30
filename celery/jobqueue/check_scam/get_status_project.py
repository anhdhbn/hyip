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

arr_func = [isp]