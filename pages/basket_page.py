from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def guest_go_basket_page(self):
        self.guest_can_go_to_basket_page()
        self.guest_cant_see_product_in_basket_opened_from_main_page()

    def guest_cant_see_product_in_basket_opened_from_main_page(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), 'The basket is not empty'

    def guest_can_message_that_the_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), 'No message that the basket is ' \
                                                                                     'empty '
