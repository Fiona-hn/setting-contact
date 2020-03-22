from time import sleep

from base.get_driver import get_driver
from page.page import Page
from base.get_data import get_data
import pytest


class TestAddContact:

    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(("name", "tel"), get_data("add_contact.yaml", "test_add_contact"))
    def test_add_contact(self, name, tel):
        self.page.page_contact.page_click_add_contact()
        self.page.add_contact.page_add_contact(name, tel)
        result_name = self.page.page_contact.page_get_name()
        assert result_name == name

