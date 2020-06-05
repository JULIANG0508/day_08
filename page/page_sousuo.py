from base.base import Base
from page.pageElements import PageElements


class PageSouSuo(Base):
    def __init__(self):
        super().__init__()

    def input_text(self,text):
        self.send_ele(PageElements.search_input,text)

    def get_result(self):
        results = self.search_eles(PageElements.search_result)
        return [i.text for i in results]
