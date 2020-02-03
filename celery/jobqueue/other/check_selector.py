import cloudscraper
from bs4 import BeautifulSoup
import html as html_cvt

class CheckSelector:
    def __init__(self, **kwargs):
        self.params = {}
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.scraper = cloudscraper.create_scraper()
    def check(self):
        soup = self.get_soup()
        investment = self.select(soup, self.investment_selector)
        paid_out = self.select(soup, self.paid_out_selector)
        member = self.select(soup, self.member_selector)

        return {
            'total_investment': investment,
            'total_paid_out': paid_out,
            'total_member': member,
        }

    def select(self, soup, selector):
        result = soup.select_one(selector)
        return result.text if result is not None else None

    def get_soup(self):
        html = self.scraper.get(self.url, timeout=30).text
        html = html_cvt.unescape(html)
        return BeautifulSoup(html, "lxml")