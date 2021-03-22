# pytest -v --tb=line --language=en test_login_page.py

from pages.login_page import LoginPage
# from pages.main_page import MainPage
import time


def test_should_be_login_url(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_should_be_login_form(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_should_be_register_form(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
