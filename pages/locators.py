from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_REGISTER = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME_IN_THE_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    PRODUCT_NAME_IN_THE_CATALOG = (By.TAG_NAME, 'h1')
    PRODUCT_PRICE_IN_THE_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(3) strong')
    PRODUCT_PRICE_IN_THE_CATALOG = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BUSKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini > span > a')


class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')
    MESSAGE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner p')


