import html as html_cvt
from bs4 import BeautifulSoup
from bs4.element import Comment, NavigableString, Tag
import cloudscraper

from celeryapp.crawl_data.base import CrawlBase
from .data import account, investment, withdrawal

class EasyCrawl(CrawlBase):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def get_info_project(self):
        scraper = cloudscraper.create_scraper()
        html = scraper.get(self.url_crawl, timeout=30).text
        html = html_cvt.unescape(html)
        soup = BeautifulSoup(html, "lxml")

        texts = soup.findAll(text=True)
        visible_texts = filter(self.tag_visible, texts)

        visible_texts = [item for item in visible_texts if item is not None]
        visible_texts = [item for item in visible_texts if self.check_condition(item)]

        richer_arr = []
        for item in visible_texts:
            richer_arr += self.richer(item)
        richer_arr = [item for item in richer_arr if item is not None]
        visible_texts += richer_arr
        
        total_investments = self.check_in_list(visible_texts, investment)
        total_paid_outs = self.check_in_list(visible_texts, withdrawal)
        total_members = self.check_in_list(visible_texts, account, int)
        if int(total_investments) == -1 and int(total_paid_outs) == -1:
            pass
        else:
            if abs(total_investments - total_paid_outs) <= 0.0001:
                total_investments = -1
                total_paid_outs = -1
            elif total_paid_outs != 0 and total_investments/total_paid_outs > 10000:
                total_investments = -1
                total_paid_outs = -1
        return total_investments, total_paid_outs, total_members

    def check_in_list_sorted(self, items, lst):
        result = []
        for item in items:
            check = item
            if isinstance(item, Tag):
                check = item.text
            
            for idx, word in enumerate(lst):
                if word.lower() in check.lower() or word.lower().replace(" ", "") in check.lower():
                    result.append((idx, item))
                    break

        result = sorted(result, key=lambda kv: kv[0])
        result = [item[1] for item in result]
        return result

    def get_parent_up_lever(self, children, num):
        current = children.parent
        for i in range(num):
            current = current.parent
        return current.children

    def check_in_list(self, items, lst, type=float):
        result = self.check_in_list_sorted(items, lst)
        if getattr(self, "debug"):
            print(result)
        for item in result:
            for i in range(3):
                for children in self.get_parent_up_lever(item, i):
                    check = children
                    if isinstance(children, Tag):
                        check = children.text
                    if self.check_condition(check):
                        txt = self.preprocess_data(check)
                        temp = self.check_num(txt, type)
                        if temp is not None:
                            return temp
        return type(-1)

    def tag_visible(self, element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True

    def check_condition(self, txt):
        check = txt
        if isinstance(txt, Tag):
            check = txt.text
        check = check.strip().replace("\n", "").replace("\t", "").replace("  ", "").strip()
        return len(check) <= 25 and (len(check) >= 4 or self.check_num(check, float) is not None)

    def check_num(self, s, type):
        try:
            return type(float(s))
        except:
            pass

    def richer(self, element, lv=1):
        if lv >= 3:
            return []
        if element.parent is not None:
            if self.check_condition(element.parent):
                return [element.parent] + self.richer(element.parent, lv=lv+1)
        return []