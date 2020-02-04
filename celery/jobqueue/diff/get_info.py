from jobqueue.driver import  Driver, handle_exceptions


class DiffProject(Driver):
    # @handle_exceptions
    def get_info_project(self):
        self.driver.get(self.url)
        self.scroll()
        
        investment = self.safe_get_element_by_css_selector_filter(self.investment_selector, num_type=float)
        paid_out = self.safe_get_element_by_css_selector_filter(self.paid_out_selector, num_type=float)
        member = self.safe_get_element_by_css_selector_filter(self.member_selector, num_type=int)
        return investment, paid_out, member

    def get_only_info_project(self):
        investment, paid_out, member = self.get_info_project()
        self.quit()
        return {
            'total_investment': investment,
            'total_paid_out': paid_out,
            'total_member': member,
        }
            