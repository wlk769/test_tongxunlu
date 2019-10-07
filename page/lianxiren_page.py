from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LianXiRenPage(BaseAction):
    #姓名
    input_name = By.XPATH,"//*[@text ='姓名' ]"
    #电话
    input_phone = By.XPATH,"//*[@text ='电话' ]"

    def input_name_a(self,text):
        self.input(self.input_name,text)

    def input_phone_b(self,phone):
        self.input(self.input_phone,phone)



