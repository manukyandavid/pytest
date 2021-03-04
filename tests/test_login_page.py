from pages.login_page import LoginPage
from config.config import TestData
import pytest


@pytest.mark.usefixtures("browser")
class TestLogin:

    def test_is_lost_paswword_link_visible(self):
        self.login_page = LoginPage(self.driver)
        flag = self.login_page.is_lost_paswword_link_exist()
        assert flag

    def test_is_login_other_way_visible(self):
        self.login_page = LoginPage(self.driver)
        flag = self.login_page.is_login_other_way_text_exist()
        assert flag

    def test_is_login_with_googe_visible(self):
        self.login_page = LoginPage(self.driver)
        flag = self.login_page.is_login_with_google_link_exist()
        assert flag

    def test_is_login_with_facebook_visible(self):
        self.login_page = LoginPage(self.driver)
        flag = self.login_page.is_login_with_facebook_link_exist()
        assert flag

    def test_login_page_title(self):
        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        assert self.login_page.is_visible(self.login_page.MY_PROFILE)


