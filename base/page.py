from page.page_shezhi import PageSheZhi
from page.page_sousuo import PageSouSuo


class Page:
    @classmethod
    def get_page_shezhi(self):
        return PageSheZhi()

    @classmethod
    def get_page_sousuo(self):
        return PageSouSuo()