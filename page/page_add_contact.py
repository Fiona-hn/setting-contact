import page
from base.base import Base
import allure


class PageAddcontact(Base):

    # 姓名输入框
    # 电话输入框

    # 输入姓名
    @allure.step(title="输入姓名")
    def page_input_name(self, name):
        allure.attach("姓名", name, allure.attach_type.TEXT)
        self.base_input(page.add_name, name)
        allure.attach("图片", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

    # 输入电话
    @allure.step(title="输入电话")
    def page_input_tel(self, tel):
        allure.attach("电话", tel, allure.attach_type.TEXT)
        self.base_input(page.add_tel, tel)

    # 组合事件
    def page_add_contact(self, name, tel):
        self.page_input_name(name)
        self.page_input_tel(tel)
        self.base_press_back()
