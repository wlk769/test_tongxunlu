from page.lianxiren_page import LianXiRenPage
from page.tongxunlu_page import TongXunPage


class Page:
    def __init__(self,driver):
        self.driver = driver
    @property
    def lianxi(self):
        return LianXiRenPage(self.driver)

    @property
    def tongxunlu(self):
        return TongXunPage(self.driver)

