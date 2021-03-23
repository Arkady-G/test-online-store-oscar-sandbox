from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        page_url_login = self.browser.current_url
        assert 'login' in page_url_login, 'No Login page'

    def should_be_login_form(self):
        login_form = self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        assert login_form, '"login_form" is not displayed on the page.'

    def should_be_register_form(self):
        login_register = self.is_element_present(*LoginPageLocators.LOGIN_REGISTER)
        assert login_register, '"login_register" is not displayed on the page.'
