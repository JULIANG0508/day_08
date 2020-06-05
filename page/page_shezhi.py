from selenium.webdriver.common.by import By

from base.base import Base
from page.pageElements import PageElements


class PageSheZhi(Base):
    def __init__(self):
        super().__init__()

    def click_sousuobut(self):
        self.click_ele(PageElements.search_btn)


        
