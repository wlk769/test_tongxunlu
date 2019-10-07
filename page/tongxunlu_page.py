from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class TongXunPage(BaseAction):
    # 点击添加按钮
    add_button = By.ID,"com.android.contacts:id/floating_action_button"


    def click_add_button(self):
        self.click(self.add_button)

