# pytest -s test_product_page.py
import time

import pytest
from pages.product_page import ProductPage


number_offer = [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9]


@pytest.mark.parametrize('offer_link', number_offer)
def test_guest_can_add_product_to_basket(browser, offer_link):
    offer_link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number_offer}'
    product_page = ProductPage(browser, offer_link)
    product_page.open()
    product_page.guest_can_add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.product_name_in_the_message_compare_the_added_product()
    product_page.product_price_in_the_basket_compare_the_added_product()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.guest_can_add_product_to_basket()
    product_page.guest_cant_see_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.guest_cant_see_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, product_link)
    product_page.open()
    product_page.guest_can_add_product_to_basket()
    product_page.message_disappeared_after_adding_product_to_basket()


