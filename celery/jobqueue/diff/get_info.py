from jobqueue.driver import  Driver, handle_exceptions
import time

class DiffProject(Driver):
    # @handle_exceptions
    def get_info_project(self):
        self.driver.get(self.url)

        self.current_scroll_position = 0
        self.max_height = int(self.driver.execute_script("return document.body.scrollHeight"))
        self.height = int(self.driver.execute_script("return window.innerHeight"))

        investment, paid_out, member = -1, -1, -1
        # self.scroll()
        raise_exception = False
        while True:
            try:
                self.scroll_one()
                if self.investment_selector != "":
                    investment = self.safe_get_element_by_css_selector_filter(self.investment_selector, num_type=float)
                if self.paid_out_selector  != "":
                    paid_out = self.safe_get_element_by_css_selector_filter(self.paid_out_selector, num_type=float)
                if self.member_selector  != "":
                    member = self.safe_get_element_by_css_selector_filter(self.member_selector, num_type=int)
            except:
                raise_exception = True
            if not raise_exception or self.current_scroll_position > self.max_height:
                break
        return investment, paid_out, member

    def scroll_one(self):
        self.current_scroll_position += self.height
        self.driver.execute_script("window.scrollTo(0, {});".format(self.current_scroll_position))

    def get_only_info_project(self):
        investment, paid_out, member = self.get_info_project()
        self.quit()
        return {
            'total_investments': investment,
            'total_paid_outs': paid_out,
            'total_members': member,
        }
    
    def __del__(self):
        self.quit()
            