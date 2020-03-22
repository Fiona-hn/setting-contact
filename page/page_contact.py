import page
import allure
from base.base import Base


class PageContact(Base):

    # 点击添加联系人
    @allure.step(title="点击添加联系人")
    def page_click_add_contact(self):
        self.base_click(page.Add_contact)

    # 获取联系人姓名
    @allure.step(title="添加成功后获取联系人姓名")
    def page_get_name(self):
        # allure.attach("姓名元素", page.name, allure.attach_type.TEXT)
        return self.base_get_text(page.name)
