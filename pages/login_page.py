from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config.config import TestData


class LoginPage(BasePage):
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "register--login-action")
    LOST_PASSWORD = (By.CLASS_NAME, "register--login-lostpassword")
    MY_PROFILE = (By.CLASS_NAME, "breadcrumb--title")
    LOGIN_OTHER_WAY = (By.CLASS_NAME, "input-title")
    LOGIN_WITH_GOOGLE = (By.CSS_SELECTOR, ".port1--hybrid--auth .socials-list .google-link")
    LOGIN_WITH_FACEBOOK = (By.CSS_SELECTOR, ".port1--hybrid--auth .socials-list .facebook-link")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_lost_paswword_link_exist(self):
        return self.is_visible(self.LOST_PASSWORD)

    def is_login_other_way_text_exist(self):
        return self.is_visible(self.LOGIN_OTHER_WAY)

    def is_login_with_google_link_exist(self):
        return self.is_visible(self.LOGIN_WITH_GOOGLE)

    def is_login_with_facebook_link_exist(self):
        return self.is_visible(self.LOGIN_WITH_FACEBOOK)

    def login_with_google(self):
        self.do_click(self.LOGIN_WITH_GOOGLE)

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
