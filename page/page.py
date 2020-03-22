from page.page_add_contact import PageAddcontact
from page.page_contact import PageContact


class Page:

    def __init__(self, driver):
        self.driver = driver

    # 通讯录页面
    @property
    def page_contact(self):
        return PageContact(self.driver)

    # 添加联系人页面
    @property
    def add_contact(self):
        return PageAddcontact(self.driver)
