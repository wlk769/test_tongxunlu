import time
import pytest

from base.base_driver import init_driver
from page.page import Page


class TestTongXun:


    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)


    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize(("name","phone"),[("zhangsan","18888888888"),("lisi","13333333333"),("wangwu","17777777777")])
    def test_tongx(self,name,phone):

        self.page.tongxunlu.click_add_button()
        self.page.lianxi.input_name_a(name)
        self.page.lianxi.input_phone_b(phone)




